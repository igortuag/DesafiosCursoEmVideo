n = int(input('Digite um número para calcular seu fatorial: '))
print('Calculando {}! ='.format(n), end=' ')
fatorial = 1
while n > 1:
    print(n, end=' x ')
    fatorial = fatorial * n
    n -= 1
print('1 = {}'.format(fatorial))