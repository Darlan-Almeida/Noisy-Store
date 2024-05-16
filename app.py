from flask import Flask, render_template, request
from controllers import bd_controller


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        cargo = request.form['cargo']

        try:
            usuario = bd_controller.inserir_dados(nome, email, telefone, cargo)
            return f"Nome: {nome}, E-mail: {email}, Telefone: {telefone}, Cargo: {cargo}"        
        except:
            return KeyError

    return render_template('home.html')
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        matricula = request.form['nome']
        senha = request.form['email']
        try:
            #precisa criar autenticação
            #administrador = bd_controller.autenticacao(matricula, senha)
            #return render_template("dashboard.html")
            pass
        except:
            return KeyError
    return render_template("admin.html")

if __name__ == '__main__':
    app.run(debug=True)
