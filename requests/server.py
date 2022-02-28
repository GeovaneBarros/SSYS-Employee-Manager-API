import sqlite3
import json
import requests
from config import *


def list_to_dict(list_keys, list_values):
    content = {}
    for i in range(len(list_keys)):
        content[list_keys[i]] = list_values[i]

    return content

def chamar_funcoes(list_operacoes, usuario):
    for item in list_operacoes:
        if item[0] == 'cadastrar':
            if item[1] == 'api_employe':
                cadastro_api_employe(usuario)
            if item[1] == 'uber':
                cadastro_uber(usuario)
            if item[1] == '99pop':
                cadastro_pop(usuario)
        if item[0] == 'excluir':
            if item[1] == 'api_employe':
                excluir_api_employe(usuario)
            if item[1] == 'uber':
                excluir_uber(usuario)
            if item[1] == '99pop':
                excluir_pop(usuario)

def controle():
    conn = sqlite3.connect('banco.db')
    cur = conn.cursor()
    usuario_banco = list(cur.execute('select * from usuario'))[0]
    usuario = list_to_dict(USUARIO_COLUMNS, usuario_banco)

    controle_banco = list(cur.execute('select * from controle'))
    chamar_funcoes(controle_banco, usuario)

    cur.execute('delete from controle')
    cur.execute('delete from usuario')
    conn.commit()
    conn.close()



def cadastro_api_employe(usuario:dict):
    print(requests.post(url=URL_EMPLOYE, data=usuario).text)


def cadastro_uber(usuario:dict):
    pass

def cadastro_pop(usuario:dict):
    pass

def excluir_api_employe(usuario:dict):
    usuario = {
        'name': usuario['name'],
        'birth_date': usuario['birth_date']
    }
    content = requests.get(URL_EMPLOYE, params=usuario)

    id = json.loads(content.text)[0]['id']
    url = URL_EMPLOYE+f'{id}/'
    print(requests.delete(url=url).text)

def excluir_uber(usuario:dict):
    pass

def excluir_pop(usuario:dict):
    pass