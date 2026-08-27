
import os
from createdb import get_db_connection

def load_data(filename=None):
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

