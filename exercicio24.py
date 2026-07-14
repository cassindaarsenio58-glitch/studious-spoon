import os

pasta_eliminar = input('Digite o nome da pasta: ').strip()

if os.path.exists(pasta_eliminar):
    try:
        os.rmdir(pasta_eliminar)
        print(f'Sucesso: A pasta',{pasta_eliminar},'foi eliminado')

    except OSError:

        print(f'ERRO: A pasta ',{pasta_eliminar},'não esta vazia ou não pode ser eliminada')

    else: 

        print(f'Erro: A pasta ',{pasta_eliminar},'não existe')