from isigi import *

def show_options():
    print('__________________')
    print('cadastrar usuario')
    print('excluir usuario')
    print('atualizar usuario')
    print('__________________')

def informacoes_usuario():
    usuario = {
        'name': input('Nome: '),
        'email': input('Email: '),
        'department': input('Departamento: '),
        'salary': input('Salário: '),
        'birth_date': input('Data nascimento (utilize formato YYYY-mm-dd): ')
    }
    return usuario

lista_sistemas = ['api_employe', '99pop', 'uber']

op = ''
while op != 'sair':
    show_options()
    op = input('Digite sua opção: ')
    if op == 'cadastrar usuario':
        usuario = informacoes_usuario()
        cadastrar_usuario(usuario, lista_sistemas)

    elif op == 'excluir usuario':
        usuario = {
        'name': input('Nome: '),
        'email': '',
        'departament': '',
        'salary': 0,
        'birth_date': input('Data nascimento (utilize o formato YYYY-mm-dd): ')
        }
        excluir_usuario(usuario, lista_sistemas)
        
    elif op == 'atualizar usuario':
        usuario = informacoes_usuario()
    else:
        print('Operação não cadastrada')