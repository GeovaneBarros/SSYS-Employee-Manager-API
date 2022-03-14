from isigi import *
def show_menu():
    '''
        This function is used to show the list of operations available to the user.
    '''
    print('__________________')
    print('cadastrar usuario')
    print('excluir usuario')
    print('atualizar usuario')
    print('__________________')

def fill_user():
    '''
        This function is used to fill in the information of a new user
    '''
    user = {
        'name': input('Nome: '),
        'email': input('Email: '),
        'department': input('Departamento: '),
        'salary': input('Salário: '),
        'birth_date': input('Data nascimento (utilize formato YYYY-mm-dd): ')
    }
    return user

systems_list = ['api_employe', '99pop', 'uber']
operation = ''

while operation != 'sair':
    show_menu()
    operation = input('Digite sua opção: ')
    
    if operation == 'cadastrar usuario':
        cadastrar_usuario(fill_user(), systems_list)

    elif operation == 'excluir usuario':
        user = {
        'name': input('Nome: '),
        'email': '',
        'departament': '',
        'salary': 0,
        'birth_date': input('Data nascimento (utilize o formato YYYY-mm-dd): ')
        }
        excluir_usuario(user, systems_list)
        
    elif operation == 'atualizar usuario':
        
        new_user = fill_user()
    else:
        print('Operação não cadastrada')