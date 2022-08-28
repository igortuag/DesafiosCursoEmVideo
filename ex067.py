while True:
    print('-'*30)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)
    c = 1
    if n < 0:
        break
    while c <= 10:
        print(f'{n} x {c:2} = {n * c:2}')
        c += 1
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')