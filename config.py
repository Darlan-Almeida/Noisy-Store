from dotenv import load_dotenv
import os
import pg8000
from urllib.parse import urlparse

class Config:

    load_dotenv()
    # URL de conexão fornecida
    url = os.environ.get('URL')
    result = urlparse(url)
    print(result.username)


    DB_CONFIG = {
        'user' : result.username,
        'password' : result.password,
        'database' : result.path[1:],
        'host' : result.hostname
    }