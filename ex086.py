num = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        num[c][l] = int(input(f'Digite um valor [{c}, {l}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{num[l][c]:5}]', end='')
    print()
