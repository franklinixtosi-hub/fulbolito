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


