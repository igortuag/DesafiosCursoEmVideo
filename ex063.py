print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
q = int(input('Quantos termos você quer mostrar? '))
print('~'*30)
c = 0
a = 0
s = 1
print('{} → {} → '.format(a,s), end='')
while c <= (q - 3):
    d = a + s
    print('{} → '.format(d), end='')
    a = s
    s = d
    c += 1
print('FIM')
print('-'*30)