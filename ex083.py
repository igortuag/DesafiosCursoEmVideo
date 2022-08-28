expressao = list(input('Digite a expressão: '))
par = 0
for v in expressao:
    if v == "(":
        par += 1
    elif v == ")":
        par -= 1
    if par < 0:
        print('Expressão incorreta')
        break
if par == 0:
    print('Expressão correta')
else:
    print('Expressão incorreta')