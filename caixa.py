valor= int(input('Valor do saque: '))
if valor <= 0:
    print('Valor invalido!')
else:
    notas100= valor // 100
    resto= valor % 100
    notas50=resto // 100
    resto=resto % 50
    notas10=resto // 10

    print('Notas de 100: ',notas100)
    print('Notas de 50: ',notas50)
    print('Notas de 10: ',notas10)