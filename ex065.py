o = ''
c = 0
soma = 0
maior = -9**99
menor = 9**99
while o != 'N':
    n = int(input('Digite um número: '))
    c += 1
    soma += n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    o = str(input('Quer continuar? [S/N] ')).strip().upper()
print('Você digitou {} números e a média foi {:.2f}'.format(c, soma / c))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))