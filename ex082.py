lista = list()
pares = list()
impares = list()
o = 's'
while o in 'sS':
    lista.append(int(input('Digite um número: ')))
    o = str(input('Quer continuar? [S/N] '))
for v in lista:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'Os valores foram {lista}')
print(f'Os valores pares foram {pares}')
print(f'Os valores impares foram {impares}')