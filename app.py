from flask import Flask
app = Flask(__name__)

@app.route('/ola')
def indedx():
    return '<h2>Programação de aplicação web é a melhor disciplina do mundo!<h2>'