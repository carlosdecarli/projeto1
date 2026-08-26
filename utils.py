import json
import os

def load_data(filename):
    with open("static/data/" + filename) as file:
        return json.load(file)


def load_template(file):
    with open('static/templates/'+file) as file:
        return file.read()

def add_note(titulo, detalhes):
    filepath = os.path.join('static', 'data', 'notes.json')
    notes = load_data('notes.json')
    notes.append({'titulo': titulo, 'detalhes': detalhes})
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(notes, file, ensure_ascii=False, indent=2)
