from random import randint
print('Sou seu computador...')
c = randint(0, 10)
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
p = int(input('Qual é seu palpite? '))
t = 1
while p != c:
    if c > p:
        print('Mais... Tente mais uma vez.')
    else:
        print('Menos... Tente mais uma vez.')
    p = int(input('Qual é seu palpite? '))
    t += 1
print('Acertou com {} tentativas. Parabéns!'.format(t))