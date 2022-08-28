from random import choice
from time import sleep
print("\033[33m-=-"*20)
print("\033[34mVou pensar em um número entre 0 e 5. Tente adivinhar...")
print("\033[33m-=-"*20)
n = (0, 1, 2, 3, 4, 5)
c = choice(n)
p = int(input("\033[30mEm que número eu pensei? "))
print("\033[35mPROCESSANDO...")
sleep(1.5)
if p == c:
    print("\033[33mPARABÉNS! Você conseguiu me vencer!")
else:
    print("\033[31mGANHEI! Eu pensei no número {} e não no {}!".format(c,p))