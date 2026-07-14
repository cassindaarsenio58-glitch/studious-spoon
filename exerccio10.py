largura = float (input('Largura de parede (m):'))
altura = float (input('Altura de parede (m): '))
area= largura * altura
tinta = area/2
print(f'Area ser pintada: {area:.2f}m2')
print(f'Quantidade de tinta necessaria: {tinta:.1f} litros')