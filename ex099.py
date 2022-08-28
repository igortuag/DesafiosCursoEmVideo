from time import sleep


def analise(*valor):
    print('-='*30)
    print('Analisando os valores passados...')
    maior = 0
    for v in valor:
        print(f' {v}', end='', flush=True)
        sleep(0.5)
        if maior < v:
            maior = v
    print(f'Foram informados {len(valor)} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


analise(2, 9, 4, 5, 7, 1)
analise(4, 7, 0)
analise(1, 2)
analise(6)
analise()