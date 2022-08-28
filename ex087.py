num = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        num[c][l] = int(input(f'Digite um valor [{c}, {l}]: '))
print('-=' * 30)
somac3 = 0
maior = 0
soma = 0
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{num[l][c]:5}]', end='')
        if c == 2:
          somac3 += num[l][c]
        if c == 1:
            if num[l][c] > maior:
                maior = num[l][c]
        if num[l][c] % 2 == 0:
            soma += num[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores da terceira coluna é {somac3}.')
print(f'O maior valor da segunda linha é {maior}')
