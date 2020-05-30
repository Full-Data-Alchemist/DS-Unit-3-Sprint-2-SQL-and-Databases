#app/ rpg_queries.py

import os
import sqlite3

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "rpg_db.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)
connection.row_factory = sqlite3.Row
print(f"CONNECTION: { connection}")

cursor = connection.cursor()
print(f"CURSOR: {cursor}")

query = "SELECT count(name) FROM charactercreator_character;"

results = cursor.execute(query).fetchall()
print(f"result: {results}")

for row in results:
    print(row["count(name)"])