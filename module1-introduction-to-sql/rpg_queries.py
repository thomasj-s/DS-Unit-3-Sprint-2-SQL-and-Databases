import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')

cursor = conn.cursor()

## Question 1
## How many total Characters are there?

query1 = '''
SELECT
	COUNT(DISTINCT(character_id)) AS unique_ids
FROM charactercreator_character
'''
answer1 = cursor.execute(query1).fetchall()
print (f'How many total Characters are there? : {answer1}')

## Question 2
## How many of each specific subclass?

query2 = '''
SELECT
	(SELECT(COUNT(DISTINCT(character_ptr_id))) FROM charactercreator_mage) AS mages,
	(SELECT(COUNT(DISTINCT(character_ptr_id))) FROM charactercreator_thief) AS thieves,
    (SELECT(COUNT(DISTINCT(character_ptr_id))) FROM charactercreator_fighter) AS fighters,
    (SELECT(COUNT(DISTINCT(character_ptr_id))) FROM charactercreator_cleric) AS clerics
'''
answer2 = cursor.execute(query2).fetchall()
print (f'How many of each specific subclass? : {answer2}')

## Question 3
## How many total Items?

query3 = '''
SELECT 
	COUNT(DISTINCT(item_id)) as unique_items
FROM armory_item
'''
answer3 = cursor.execute(query3).fetchall()
print (f'How many total Items? : {answer3}')

## Question 4
## How many of the Items are weapons? How many are not?

query4 = '''
SELECT 
	total_items - total_weapons AS total_non_weapon_items,
	total_weapons
	FROM(
	SELECT
		COUNT(DISTINCT(item_ptr_id)) AS total_weapons,
		COUNT(DISTINCT(item_id)) AS total_items
		FROM armory_item
		LEFT JOIN armory_weapon
		ON item_ptr_id = item_id
)
'''
answer4 = cursor.execute(query4).fetchall()
print (f'How many of the Items are weapons? How many are not? : {answer4}')

## Question 5
## How many Items does each character have? (Return first 20 rows)

query5 = '''
SELECT
	character_id,
	COUNT(item_id) as item_count
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20
'''
answer5 = cursor.execute(query5).fetchall()
print (f'How many Items does each character have? (Return first 20 rows) : {answer5}')

## Question 6
## How many Weapons does each character have? (Return first 20 rows)

query6 = '''
SELECT
	items.character_id,
	COUNT(weapons.item_ptr_id) AS number_of_weapons
FROM charactercreator_character_inventory as items
LEFT JOIN armory_weapon AS weapons
ON weapons.item_ptr_id = items.item_id
GROUP BY character_id
LIMIT 20
'''
answer6 = cursor.execute(query6).fetchall()
print (f'How many Weapons does each character have? (Return first 20 rows) : {answer6}')

## QUESTION 7
## On average, how many Items does each Character have?

query7 = '''
SELECT AVG(item_count) AS Average_items_per_character
FROM(
	SELECT
		character_id,
		COUNT(item_id) as item_count
	FROM charactercreator_character_inventory
	GROUP BY character_id
)
'''
answer7 = cursor.execute(query7).fetchall()
print (f'On average, how many Items does each Character have? : {answer7}')


## Question 8
## On average, how many weapons does each character have?

query8 = '''
SELECT AVG(number_of_weapons) as Average_weapons_per_character
FROM (
	SELECT
		items.character_id,
		COUNT(weapons.item_ptr_id) AS number_of_weapons
	FROM charactercreator_character_inventory as items
	LEFT JOIN armory_weapon AS weapons
	ON weapons.item_ptr_id = items.item_id
	GROUP BY character_id
)
'''
answer8 = cursor.execute(query8).fetchall()
print (f'On average, how many weapons does each character have? : {answer8}')

conn.close()