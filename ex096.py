def terreno (l, c):
    a = l * c
    print(f'A área de um terreno{l}x{c} é de {a}m².')

largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
terreno(largura, comprimento)