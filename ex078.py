valores = list()
mai = men = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = valores[c]
    else:
        if valores[c] < men:
            men = valores[c]
        if valores[c] > mai:
            mai = valores[c]
print(f'Vocë digitou os valores {valores}')
print(f'O maior valor digitado foi {mai} nas posições: ', end='')
for p, c in enumerate(valores):
    if c == mai:
        print(f'{p}... ', end='')
print(f'\nO menor valor digitado foi {men} nas posições: ', end='')
for p, c in enumerate(valores):
    if c == men:
        print(f'{p}... ',end='7')
