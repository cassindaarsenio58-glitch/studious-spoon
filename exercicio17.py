velocidade =float(input('Qual é a velocidade do carro (km/h)'))
if velocidade > 80:
    excesso =velocidade-80
    multa= excesso *5
    print(f'Foste multado por excesso de velocidade')
    print(f'Valor da multa: {multa:.2f}')
else: 
    print('Velocidade permitida. Conduz com cuidado')