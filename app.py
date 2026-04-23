from flask import Flask, render_template, request, redirect, url_for
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

@app.route('/dados')
def dados():
    return render_template('dados.html')


@app.route('/recebedados', methods = ['GET','POST'])
def recebedados():
    nome = request.form.get('nome')
    sobrenome = request.form['sobrenome']
    email = request.form['email']
    nasc = request.form['data']
    escola = request.form.getlist('escola') #get é usado pra pegar um item. getlist pega uma lista de itens. Útel neste exemplo porque é um checkbox, ou seja, pode receber mais que um valor.

    return render_template('recebedados.html', nome = nome, sobrenome = sobrenome, email = email, nasc = nasc, escola = escola)

@app.route('/compras')
def compras():
    return render_template('compras.html')

@app.route('/recebecompras', methods = ['POST'])
def recebecompras():
    itens = request.form.getlist('item')
    return render_template('recebecompras.html', itens = itens)


@app.route('/verificaridade/<int:idade>')
def verificar(idade):
    if idade>=18:
        return f"Você tem {idade} anos. Portanto, você é maior de idade"
    else:
        return f"Você tem {idade} anos. Portanto, você é menor de idade"
    
@app.route('/verificaridade2/<int:idade>')
def verificaridade2(idade):
    return render_template('idade.html', idade=idade)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/verificar_login', methods = ['POST'])
def verificar_login():
    usuario = request.form.get('login')
    senha = request.form.get('senha')

    if usuario == 'admin' and senha == '12345':
        return render_template('acesso.html')
    else:
        return render_template('acesso_negado.html')

@app.route('/exemplolaco')
def exemplolaco():
    return render_template('exemplolaco.html')
    
@app.route('/produtos')
def produtos():
    itens = [
        {'nome' : 'teclado', 'preco' : '200', 'img' : 'https://www.lognetinfo.com.br/imagens/250x250/23419A.jpg'},
        {'nome' : 'smartphone', 'preco' : '1500', 'img' : 'https://imgs.pontofrio.com.br/55071143/1g.jpg'},
        {'nome' : 'Pen-drive', 'preco' : '50', 'img' : 'https://img.kalunga.com.br/fotosdeprodutos/243483z_1.jpg'},
        {'nome' : 'Pen-drive', 'preco' : '50', 'img' : 'https://m.media-amazon.com/images/I/41ajsKjg9EL._AC_UF894,1000_QL80_.jpg'},
        {'nome' : 'smartphone', 'preco' : '1500', 'img' : 'https://trocafone.vtexassets.com/arquivos/ids/283737/iphone-14-meia-noite-traseira.jpg?v=639094496053700000'}
    ]

    qnt_itens = len(itens)
    return render_template('produtos.html', itens = itens, qtd = qnt_itens)


if __name__ == '__main__':
    app.run()