m = 0
velho = 0
jovens = 0
nome = ''
for c in range(1,5):
    print("----- {}ª PESSOA -----".format(c))
    n = str(input('Nome: '))
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).strip().upper()
    m += i / 4
    if s == "M":
        if i > velho:
            velho = i
            nome = n
    if s == 'F':
        if i < 20:
            jovens += 1
print('A média de idade do grupo é de {:.1f} anos'.format(m))
print('O homem mais velho tem {} anos e se chama {}'.format(velho,nome))
print('Ao todo são {} mulher com menos de 20 anos'.format(jovens))
