import random

opcoes = ["Pedra", "Papel", "Tesoura"]

while True:

    computador: str = random.choice(opcoes)

    print("=== JOKENPO ===")
    print("[ 0 ] Pedra\n[ 1 ] Papel\n[ 2 ] Tesoura\n[ 3 ] Sair")
    jogador_escolha = int(input("Qual é a tua jogada? "))

    if jogador_escolha == 3:
        print('Saindo do jodo...Até mais!')
    break

    if jogador_escolha not in [0, 1, 2]:
        print("Opção inválida!")
        continue

    jogador = opcoes[jogador_escolha]

    print(f"\nComputador jogou: {computador}")
    print(f"Jogador jogou: {jogador}\n")

    if jogador == computador:
        print("EMPATE!")
    elif (jogador == "Pedra" and computador == "Tesoura") or \
         (jogador == "Papel" and computador == "Pedra") or \
         (jogador == "Tesoura" and computador == "Papel"):
        print("JOGADOR VENCEU!")
    else:
        print("COMPUTADOR VENCEU!")