import sqlite3

def create_database():

    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()

    create_table = '''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
    '''

    cursor.execute(create_table)

    conn.commit()
    conn.close()
    
def add_user(name, age):
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
    existing = cursor.fetchone()

    if existing:
        print("User already exists!")
    else:
        cursor.execute("INSERT INTO users(name, age) VALUES(?, ?)", (name, age))
        conn.commit()

    conn.close()


create_database()   
add_user("ali", 20)        

print("Database ready and user added successfully")