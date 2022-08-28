from time import sleep


def sep():
    print('-='*15)


def contador(i, f, p):
    sep()
    print(f'Contagem de {i} até {f} de {p} em {p}')
    for c in range(i, f, p):
        print(f'{c} ', end='', flush=True)
        sleep(0.5)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, -2)
sep()
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
