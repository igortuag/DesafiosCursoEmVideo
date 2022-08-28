jogo = []
print(jogo)
for i in range(0, 8):
    for j in range(0, 8):
        jogo[i][j] = int(input(f'Digite um valor [{i}, {j}]: '))
print(jogo)