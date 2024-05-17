import pg8000
from config import Config


def inserir_dados(nome, email, telefone, cargo):
    try:
    
        connection = pg8000.connect(**Config.DB_CONFIG)
        cursor = connection.cursor()


        query = "INSERT INTO Clientes (nome, email, telefone, cargo) VALUES (%s, %s, %s, %s) RETURNING id"
        values = (nome, email, telefone, cargo)
        cursor.execute(query, values)

        connection.commit()

        # Fechar a conexão
        connection.close()
        # Se a conexão for bem-sucedida, exibir uma mensagem
        print("Operacção bem-sucedida ao banco de dados PostgreSQL!")

    except Exception as e:
        # Se houver algum erro durante a conexão, exibir a mensagem de erro
        print("Erro no banco de dados PostgreSQL:", e)

