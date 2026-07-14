nome=chr (input('Nome do aluno: '))
n1=int(input('Nota 1: '))
n2=int(input('Nota 2: '))
media=(n1+n2)/2
print(f'Media do aluno {nome}: {media:.1f}')
if media >=7.0:
    print('O aluno teve um bom aproveitamento')
else:
    print('O aluno não teve um bom aproveitamento')