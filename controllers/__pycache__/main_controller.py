from flask import render_template, request, redirect, url_for
from app.services.user_service import create_user

def index():
    if request.method == 'POST':
        name = request.form['nome']
        email = request.form['email']
        phone = request.form['telefone']
        role = request.form['cargo']
        
        create_user(name, email, phone, role)
        
        return redirect(url_for('success'))
    
    return render_template('form.html')

def success():
    return "Formulário enviado com sucesso!"
