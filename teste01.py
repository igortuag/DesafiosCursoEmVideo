n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print(f'O que você deseja fazer com os número {n1} e {n2}')
opc = int(input('Digite 1 para soma 2 para subtração 3 para multiplicação e 4 para divisão'))
if opc == 1:
    print(f'A soma de {n1} + {n2} = {n1+n2}')
elif opc == 2:
    print(f'A subtração de {n1} - {n2} = {n1-n2}')
elif opc == 3:
    print(f'A multiplicação de {n1} * {n2} = {n1*n2}')
elif opc == 4:
    print(f'A divisão de {n1} / {n2} = {n1/n2}')
else:
    print('Opção invalida')