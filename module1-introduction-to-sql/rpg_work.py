

import sqlite3
import os
"""
- How many total Characters are there?
- How many of each specific subclass?
- How many total Items?
- How many of the Items are weapons? How many are not?
- How many Items does each character have? (Return first 20 rows)
- How many Weapons does each character have? (Return first 20 rows)
- On average, how many Items does each Character have?
- On average, how many Weapons does each character have?

"""

def connect_to_db(db_name="rpg_db.sqlite3"):
    return sqlite3.connect(db_name)

def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()
GET_CHARACTERS = """
SELECT count(character_id) FROM charactercreator_character;
-- how many total characters are there
"""
GET_CHARACTERS = """
SELECT count(character_id) FROM charactercreator_character;
-- how each specific sub class
"""




if __name__ == "__main__":
    conn = connect_to_db()
    curs = conn.cursor()
    results = execute_query(curs, GET_CHARACTERS)
    print(results)


