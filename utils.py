import json

def load_data(filename):
    with open("static/data/" + filename) as file:
        return json.load(file)


def load_template(file):
    with open('static/templates/'+file) as file:
        return file.read()