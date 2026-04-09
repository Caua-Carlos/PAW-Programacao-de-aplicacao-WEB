from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def indedx():
    return render_template('index.html')

@app.route('/email')

@app.route('/faleconosco')

def contato():
    return render_template('contato.html', nome ="Cauã Carlos", email = "carlos.caua@escolar.ifrn.edu.br", numero = "84 988888888")
   
@app.route("/usuario", defaults = {"nome" : "desconhecido", "sobrenome" : "desconhecido"})

@app.route("/usuario/<nome>/<sobrenome>")
def usuario(nome, sobrenome):
    return render_template('usuario.html', nome = nome, sobrenome = sobrenome)

@app.route("/semestre", defaults = {"x" : 0 })
def semesttre(x):
    atual = x
    anterior = 0
    return render_template("semestre.html", atual = atual, anterior = anterior )

@app.route("/semestre/<int:x>")
def semestre(x):
    atual = x
    if atual > 0:
        anterior = x-1
        return render_template("semestre.html", atual = atual, anterior = anterior)
    elif atual == 0:
        anterior = "Não há semestre anterior"
        return render_template("semestre.html", atual = atual, anterior = anterior )
    
@app.route('/perfil/<usuario>')
def perfil(usuario):
    return render_template('perfil.html', usuario = usuario)



if __name__ == '__main__':
    app.run()