def sair():
    resp=input('Deseja sair.Sim/S ou Nao/N').upper()
    return resp == 'Sim' or resp =='S'
while True:
    n1=float(input('Digite um numero: '))
    n2=float(input('Digite outro numero: '))
    if n1 > n2:
        print('Maior numero:',n1)
    elif n2 > n1:
        print('Maior numero: ',n2)
    else:
        print('Os  numeros sao iguais')
    if sair():
        print('Fim do programa')
        break