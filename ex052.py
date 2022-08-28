n = int(input('Digite um número: '))
v = 0
for c in range(1, n + 1, 1):
    if n % c == 0:
        print("\033[33m{}".format(c), end=' ')
        v += 1;
    else:
        print("\033[31m{}".format(c), end=' ')
print("\n\033[30mO numero {} foi divisível {} vezes".format(n,v))
if v == 2:
    print('E por isso ele É PRIMO')
else:
    print('E por isso ele NÃO É PRIMO')