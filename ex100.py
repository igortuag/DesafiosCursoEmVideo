from random import randint


def sortear():
    print('Sorteando 5 valores da lista: ', end='')
    c = 0
    while c < 5:
        s = randint(0, 9)
        print(f'{s} ', end='', flush=True)
        sorteio.append(s)
        c += 1
    print()


def soma(lista):
    total = 0
    for v in lista:
        if v % 2 == 0:
            total += v
    print(f'Somando os valores pares de {lista}, temos {total}')

sorteio = list()
sortear()
soma(sorteio)