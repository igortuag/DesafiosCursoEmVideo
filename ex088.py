from random import randint
from time import sleep
opt = list()
jogos = list()
print('-='*15)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-='*15)
quant = int(input('Quantos jogos você quer que eu sortei?'))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in opt:
            opt.append(num)
            cont += 1
        if cont >= 6:
            break
    opt.sort()
    jogos.append(opt[:])
    opt.clear()
    tot += 1
print('-=' * 3, f' SORTEANDO {quant} JOGOS', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)