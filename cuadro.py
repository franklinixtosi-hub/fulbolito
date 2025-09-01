import sqlite3


conn = sqlite3.connect('palabras.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS palabras (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        palabra TEXT NOT NULL,
        descripcion TEXT NOT NULL
    )
''')
conn.commit()

def pala():
    cursor.execute("SELECT palabra, descripcion FROM palabras ORDER BY RANDOM() LIMIT 1")
    return cursor.fetchone()



