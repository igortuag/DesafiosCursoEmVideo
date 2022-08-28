c = 'S'
valores = list()
v = 0
while c in 'Ss':
    v = int(input('Digite um valor: '))
    if v in valores:
        print('Valor duplicado! Náo vou adicionar...')
    else:
        print('Valor adicionado com sucesso...')
        valores.append(int(v))
    c = str(input('Quer continuar? '))
print('-='*20)
print(f'Você digitou os valores {sorted(valores)}')