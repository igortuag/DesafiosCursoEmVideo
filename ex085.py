num = [[], []]
dado = list()
for c in range (1, 8):
    dado = int(input(f'Digite o valor numero {c}: '))
    if dado % 2 == 0:
        num[0].append(dado)
    else:
        num[1].append(dado)
print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'Os valores imapres foram {num[1]}')
print(f'Os valores pares foram {num[0]}')