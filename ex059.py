o = 0
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
while o != 5:
    print('''   [ 1 ] Somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sai do programa''')
    o = int(input('>>> Qual é a sua opção?'))
    if o == 1:
        print('A soma de {} com {} vale: {}'.format(n1, n2, n1 + n2))
    elif o == 2:
        print('A multiplicação de {} com {} vale: {}'.format(n1, n2, n1 * n2))
    elif o == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        elif n1 < n2:
            print('{} é maior que {}'.format(n2, n1))
        else:
            print('Os números são iguais')
    elif o == 4:
        print('Digite novos números')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif o == 5:
        print('Saindo...')
    else:
        print('Opção invalida, tente novamente')