menor = float(input('Peso da 1° pessoa: '))
maior = menor
for c in range(2, 6):
    p = float(input('Peso da {}° pessoa: '.format(c)))
    if p > maior:
        maior = p
    if p < menor:
        menor = p
print('O maior peso lido foi de {:.2f}Kg'.format(maior))
print('O menor peso lido foi de {:.2f}Kg'.format(menor))