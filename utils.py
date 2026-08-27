import os
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('banco.db')
    conn.row_factory = sqlite3.Row  # Permite acessar colunas por nome
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
    init_db()  # Garante que o banco existe
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

def delete_note(note_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM note WHERE id = ?', (note_id,))
    conn.commit()
    conn.close()

def get_note_by_id(note_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, content FROM note WHERE id = ?', (note_id,))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        return {
            'id': row['id'],
            'titulo': row['title'],
            'detalhes': row['content']
        }
    return None

def update_note(note_id, titulo, detalhes):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'UPDATE note SET title = ?, content = ? WHERE id = ?',
        (titulo, detalhes, note_id)
    )
    conn.commit()
    conn.close()

