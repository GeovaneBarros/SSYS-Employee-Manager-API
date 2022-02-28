import sqlite3
import server
from config import DATABASE_NAME


def adicionar_valores_banco(operacao, sistemas, usuario):
    conn = sqlite3.connect(DATABASE_NAME)    
    cur = conn.cursor()    
    cur.execute(f"insert into usuario values{tuple(usuario.values())}")
    for sistema in sistemas:
        cur.execute(f"insert into controle values('{operacao}','{sistema}')")
    conn.commit()
    conn.close()

def cadastrar_usuario(usuario:dict, sistemas:list):
    adicionar_valores_banco('cadastrar', sistemas, usuario)
    server.controle()

def excluir_usuario(usuario:dict, sistemas:list):
    adicionar_valores_banco('excluir', sistemas, usuario)
    server.controle()
