from flask import Flask, render_template_string, request, redirect
from createdb import create_database
import views
from utils import delete_note, get_note_by_id, update_note


app = Flask(__name__)

app.static_folder = 'static'
create_database()

@app.route('/')
def index():

    return render_template_string(views.index())

@app.route('/submit', methods=['POST'])
def submit_form():
    titulo = request.form.get('titulo')  
    detalhes = request.form.get('detalhes')  

    views.submit(titulo, detalhes)
    return redirect('/')

@app.route('/delete/<int:note_id>')
def delete(note_id):
    delete_note(note_id)
    return redirect('/')

@app.route('/update/<int:note_id>')
def edit(note_id):
    note = get_note_by_id(note_id)
    if note:
        return render_template_string(views.edit(note))
    return redirect('/')

@app.route('/update', methods=['POST'])
def update():
    note_id = request.form.get('id')
    titulo = request.form.get('titulo')
    detalhes = request.form.get('detalhes')
    
    update_note(note_id, titulo, detalhes)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)