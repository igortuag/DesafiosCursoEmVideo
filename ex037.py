n = int(input("Digite um número inteiro: "))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
o = int(input('Sua opção: '))
if o == 1:
    print("O númeor {} convertido para BÍNARIO é {}".format(n, bin(n)[2:]))
if o == 2:
    print("O númeor {} convertido para OCTAL é {}".format(n, oct(n)[2:]))
if o == 3:
    print("O númeor {} convertido para HEXADECIMAL é {}".format(n, hex(n)[2:]))
