from flask import Flask
app = Flask(__name__)

@app.route('/')
def indedx():
    return 'Programação de aplicação web é a melhor disciplina do mundo'