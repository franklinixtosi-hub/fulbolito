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

def inpal(palabra, descripcion):
    cursor.execute("INSERT INTO palabras (palabra, descripcion) VALUES (?, ?)", (palabra.lower(), descripcion))
    conn.commit()

def elipal(palabra):
    cursor.execute("DELETE FROM palabras WHERE palabra = ?", (palabra.lower(),))
    conn.commit()