from utils import load_data, load_template, add_note

def index():
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(id=dados['id'], title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data()
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)

def submit(titulo, detalhes):
    add_note(titulo, detalhes)

def edit(note):
    template = load_template('edit.html')
    return template.format(
        note_id=note['id'],
        titulo=note['titulo'],
        detalhes=note['detalhes']
    )