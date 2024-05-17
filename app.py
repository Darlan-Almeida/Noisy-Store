from flask import Flask, render_template, request
from controllers import bd_controller
import jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
)

@app.route('/', methods=['GET', 'POST'])
@limiter.limit("10 per hour")
@limiter.limit("20 per day")
def index():
    print(Limiter)
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        cargo = request.form['cargo']

        try:
            result = bd_controller.inserir_dados(nome, email, telefone, cargo)
            return 'Usuário Cadastrado'
        except Exception as e:
            return jsonify({"error": str(e)}), 500

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
