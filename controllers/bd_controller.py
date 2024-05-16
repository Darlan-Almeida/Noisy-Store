import pg8000
from config import Config

def inserir_dados(nome, email, telefone, cargo):
    connection = pg8000.connect(**Config.DB_CONFIG)
    cursor = connection.cursor()
    
    try:
        query = "INSERT INTO Clientes (nome, email, telefone, cargo) VALUES (%s, %s, %s, %s) RETURNING id"
        values = (nome, email, telefone, cargo)
        cursor.execute(query, values)

        connection.commit()

        # Recupera o ID do usuário inserido
        cursor.close()
        connection.close()
        
        return "usuario cadastrado"
    except:
        return "Erro"

    
def autenticacao(matricula, nome):
    connection = pg8000.connect(**Config.DB_CONFIG)
    cursor = connection.cursor()