num = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')), int(input('Digite outro valor: ')),
     int(input('Digite outro valor: ')), int(input('Digite outro valor: ')))
n9 = 0
p3 = 0
p3i = 0
for c, n in enumerate(num):
    if n == 9:
        n9 += 1
    if n == 3 and p3i == 0:
        p3 = c + 1
        p3i += 1
print(f'Ao todo apareceram {n9} números 9')
if p3 > 0:
    print(f'O primeiro 3 apareceu na posição número {p3}')
else:
    print('O número 3 não apareceu')
print('Os valores pares são: ', end='')
for c, n in enumerate(num):
    if n % 2 == 0:
        print(n, end=' ')
