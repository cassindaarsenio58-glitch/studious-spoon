cigarros_por_dia= int (input('Quantidade de cigarros fumadospor dia: '))
anos_fumado= int (input ('Quantos anos ja fumou'))

total_cigarros = cigarros_por_dia* (anos_fumado*365)
minutos_perdidos= total_cigarros *10
dias_perdidos= minutos_perdidos /1440
print(f'Um fumante perdera aproximadamnete {dias_perdidos:.1f} dias de vida')