from typing import List

pessoa = list()
dado = list()
o = 'S'

while o in 'Ss':
    dado.append(str(input('Nome: ')))
    dado.append(str(input('Peso: ')))
    pessoa.append(dado[:])
    dado.clear()
    o = input('Deseja continuar? [S/N] ')

print(f'Ao todo você cadastrou {len(pessoa)} pessoas.')

menor = maior = 0
for p in pessoa:
    if maior == 0:
        maior = p[1]
    if menor == 0:
        menor = p[1]
    if p[1] > maior:
        maior = p[1]
    if p[1] < menor:
        menor = p[1]

print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for d in pessoa:
    if d[1] == maior:
        print(d[0], end=', ')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
for d in pessoa:
    if d[1] == menor:
        print(d[0], end=', ')