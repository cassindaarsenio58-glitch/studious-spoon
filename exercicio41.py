import os

pasta_atual = input("Digite o nome atual da pasta: ").strip()
pasta_nova = input("Digite o novo nome para a pasta: ").strip()

if not os.path.exists(pasta_atual):
    print(f"Erro: A pasta original '{pasta_atual}' não existe.")

elif os.path.exists(pasta_nova):
    print(f"Erro: Já existe uma pasta ou arquivo com o nome '{pasta_nova}'.")

else:
    os.rename(pasta_atual, pasta_nova)
    print(f"Sucesso: Pasta renomeada de '{pasta_atual}' para '{pasta_nova}'.")