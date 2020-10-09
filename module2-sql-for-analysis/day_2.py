

import psycopg2
import sqlite3


#My credentials
dbname = "ijxbvrms"
user = "ijxbvrms"
password = "NOb6lIlWJb3wYhRQJMKGGf3OEg37LPHt"
host = "postgres://ijxbcrms:NOb6lIlWJb3wYhRQJMKGGf3OEg37LPHt@topsy.db.elephantsql.com:5432/ijxbcrms"

pg_conn = psycopg2.connect(dbname=dbname,
                                        user = user,
                                        password = password,
                                        host = host)

pg_curs = psycopg2.execute(pg_conn)



create_table_statement = """
CREATE TABLE  test_table (
    id  SERIAL PRIMARY KEY,
    name  varchar(40), NOT NULL,
    data   JSONB
);
"""
insert_statement = """
INSERT INTO test_table (name, date) VALUES
(
    'Carls',
    null,
),
(
    'mani with a JSON',
    "{'a': 1, 'b': ['yin', 'yan', 42], c: true}":: JSONB
);
"""
for yin in characters:
    ex_insert_character = """
        INSERT INTO charactercreator_creator
        (name, level, exp, hp, strenght, intellegence, dexerity, wisdom)
    """

copied_path =  55 # TODO
sl_conn = copied_path
if "__name__" == "__main__":
    pass