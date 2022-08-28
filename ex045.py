from random import choice
from time import sleep
oj = int(input(''''Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é a sua jogada? '''))
op = (0, 1 , 2)
oc = choice(op)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
print("-="*10)
print("Computador jogou ", end="")
if oc == 0:
    print("PEDRA")
elif oc == 1:
    print("PAPEL")
elif oc == 2:
    print("TESOURA")
print("Jogador jogou ", end="")
if oj == 0:
    print("PEDRA")
elif oj == 1:
    print("PAPEL")
elif oj == 2:
    print("TESOURA")
print("-="*10)
if oc == oj:
    print("DEU EMPATE")
elif oc == 0 and oj == 2 or oc == 1 and oj == 0 or oc == 2 and oj == 1:
    print("COMPUTADOR VENCE!")
else:
    print("JOGADOR VENCE")
