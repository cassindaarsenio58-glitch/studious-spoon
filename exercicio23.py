import os 

nome_pasta =input('Digite o nome da pasta que deseja criar:  ').strip()

if os.path.exists(nome_pasta):

    print(f'Aviso: A pasta',{nome_pasta},'já existe')

else: 

    os.makedirs(nome_pasta)
    print(f'Sucesso: A pasta',{nome_pasta},'foi criado.')
