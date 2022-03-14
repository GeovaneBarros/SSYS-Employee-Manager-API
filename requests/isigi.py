import sqlite3
import server
from config import DATABASE_NAME


def add_values_to_database(operation, systems, user):
    '''
        This function adds values ​​of operations and users to the database for processing on the server.
    '''

    conn = sqlite3.connect(DATABASE_NAME)    
    cur = conn.cursor()    
    cur.execute(f"insert into usuario values{tuple(user.values())}")
    for system in systems:
        cur.execute(f"insert into controle values('{operation}','{systems}')")
    conn.commit()
    conn.close()

def cadastrar_usuario(user:dict, systems:list):
    add_values_to_database('cadastrar', systems, user)
    server.controle()

def excluir_usuario(user:dict, systems:list):
    add_values_to_database('excluir', systems, user)
    server.controle()
