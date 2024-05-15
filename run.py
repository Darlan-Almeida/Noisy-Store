from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        cargo = request.form['cargo']
        # Aqui você pode adicionar o processamento dos dados recebidos
        return f"Nome: {nome}, E-mail: {email}, Telefone: {telefone}, Cargo: {cargo}"
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
