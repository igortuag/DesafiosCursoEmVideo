n = int(input())
for i in range(0, n):
    numeros = input()
    numero = numeros.split()
    A = int(numero[0])
    B = int(numero[1])
    if A > B:
        p = A
        l = B
    else:
        p = B
        l = A
    while True:
        if p % l == 0:
            mdc = l
            break
        else:
            l = l - 1
    print(mdc)