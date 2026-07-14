from datetime import datetime
ano_nascimento = int(input('Ano de nascimento:'))
ano_atual=datetime.now().year
idade=ano_atual-ano_nascimento

if idade >= 16:
    print(f'Tens {idade} anos. Ja podes votar')

else:
    print(f'Tens {idade} anos. Ainda nao podes votar')