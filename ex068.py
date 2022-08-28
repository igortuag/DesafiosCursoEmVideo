v = 0
print('-=' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
from random import randint
while True:
    print('-=' * 20)
    nj = int(input('Diga um valor: '))
    ej = str(input('Par ou Ímpar? [P/I] ')).upper()
    nc = randint(0, 10)
    print('-' * 40)
    print(f'Você jogou 8 e o computador 4. Total de {nj + nc} DEU ', end='')
    if (nj + nc) % 2 == 0:
        print('PAR')
        er = 'P'
    else:
        print('IMPAR')
        er = 'I'
    print('-' * 40)
    if ej == er:
        print('Você VENCEU!')
        v += 1
    else:
        print(f'GAME OVER! Você venceu {v} vezes.')
        break
    print('Vamos jogar novamente...')