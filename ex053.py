frase = str(input('Digite uma frase: ')).strip().upper()
s = frase.split()
j = ''.join(s)
i = ''
for c in range(len(j) - 1, -1, -1):
    i += j[c]
print('O inverso de {} é {}'.format(j, i))
if j == i:
    print('Portanto a frase é um palíndromo!')
else:
    print('Logo, a frase não é um palíndromo!')
