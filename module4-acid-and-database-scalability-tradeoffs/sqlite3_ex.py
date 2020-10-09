import sqlite3


conn = sqlite3.connect("ex_db.sqlite3")


# how can we make this more 
def create_table(conn):
    curs = conn.cursor()
    #make sql create statement
    create_table = """
        CREATE TABLE Students(
            id INTEBER PRIMAY KEY AUTOINCREMENT,
            name CHAR(20),
            fav_num INTEGER
        )    
    """
def insert_data(conn):
    curs = conn.cursor()
    my_data = [
        ("George", 7),
        ("Stephen", 88)
    ]

# for 