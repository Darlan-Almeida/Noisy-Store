from dotenv import load_dotenv
import os

class Config:

    load_dotenv()

    DB_CONFIG = {
        'host': os.environ.get("HOST"),
        'database': os.environ.get("DATABASE"),
        'user': os.environ.get("USER"),
        'password': os.environ.get("PASSWORD")
    }
    
    DEBUG = True
