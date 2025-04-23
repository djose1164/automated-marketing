import mariadb as mdb
from dotenv import load_dotenv
import os

load_dotenv()

def get_db():
    conn = mdb.connect(
        username=f"{os.getenv('username')}",
        host=f"{os.getenv('host')}",
        password=f"{os.getenv('password')}",
        database=f"{os.getenv('database')}"
    )
    return conn

def get_cur():
    return get_db().cursor()