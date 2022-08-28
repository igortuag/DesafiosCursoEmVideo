print('Gerador de PA')
print('-='*10)
n = int(input('Priemrio termo: '))
r = int(input('Razão da PA: '))
u = (n + r*9)
while n <= u:
    print('{} → '.format(n), end='')
    n += r
print('FIM')
