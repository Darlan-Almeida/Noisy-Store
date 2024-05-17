import pg8000
from urllib.parse import urlparse
from config import Config

try:    
    connection = pg8000.connect(**Config.DB_CONFIG)
    cursor = connection.cursor()

    # Se a conexão for bem-sucedida, exibir uma mensagem
    print("Conexão bem-sucedida ao banco de dados PostgreSQL!")

    query = "INSERT INTO Clientes (nome, email, telefone, cargo) VALUES (%s, %s, %s, %s) RETURNING id"
    values = ('nome', 'email', 'telefone', 'cargo')
    cursor.execute(query, values)

    connection.commit()

    # Fechar a conexão
    connection.close()

except Exception as e:
    # Se houver algum erro durante a conexão, exibir a mensagem de erro
    print("Erro ao conectar ao banco de dados PostgreSQL:", e)
