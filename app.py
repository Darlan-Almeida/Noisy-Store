from flask import Flask, render_template, request
from controllers import bd_controller
import jsonify
from collections import defaultdict
import time


app = Flask(__name__)
request_counts = defaultdict(list)


@app.route('/', methods=['GET', 'POST'])
def index():
    client_ip = request.remote_addr
    current_time = time.time()
    
    # Limpe as requisições antigas (maximo de 05 requisições por hora)
    
    request_counts[client_ip] = [timestamp for timestamp in request_counts[client_ip] if current_time - timestamp < 3600]

    print(request_counts)
    
    if request.method == 'POST':
        if len(request_counts[client_ip]) >= 5:
            return "Limite de envio de formulário excedido"
        
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        cargo = request.form['cargo']
        
        try:
            result = bd_controller.inserir_dados(nome, email, telefone, cargo)
            # Adiciona o timestamp atual à lista de requisições deste IP
            request_counts[client_ip].append(current_time)
            return 'Usuário Cadastrado'
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return render_template('main.html')

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
