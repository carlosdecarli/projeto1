import os
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('banco.db')
    conn.row_factory = sqlite3.Row 
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS note (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def load_data(filename=None):
    init_db()  
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, content FROM note ORDER BY id')
    rows = cursor.fetchall()
    conn.close()
    
    notes = []
    for row in rows:
        notes.append({
            'id': row['id'],
            'titulo': row['title'],
            'detalhes': row['content']
        })
    return notes

def load_template(filename):
    filepath = os.path.join('static', 'templates', filename)
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def add_note(titulo, detalhes):
    init_db()  
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO note (title, content) VALUES (?, ?)',
        (titulo, detalhes)
    )
    conn.commit()
    conn.close()

