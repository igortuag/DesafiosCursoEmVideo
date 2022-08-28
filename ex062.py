print('Gerador de PA')
print('-='*10)
n = int(input('Priemrio termo: '))
r = int(input('Razão da PA: '))
u = (n + r*9)
while n <= u:
    print('{} → '.format(n), end='')
    if n == u:
        print('PAUSA')
        m = int(input('Quantos termos você quer mostrar a mais? '))
        u += m*r
    n += r
print('FIM')
