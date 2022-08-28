lista = list()
o = 's'
while o in 'sS':
    lista.append(int(input('Digite um número')))
    o = str(input('Quer continuar? [S/N] '))
print(f'Você digitou {len(lista)} números')
lista.sort(reverse=True)
print(f"Em ordem2 decrecente são: {lista}")
if 5 in lista:
    print('O Valor 5 foi digitado!')
else:
    print('O valor 5 não foi digitado')

