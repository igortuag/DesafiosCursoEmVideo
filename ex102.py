def fatorial(n, show=False):
    """
    fatorial(n, show=False)
        -> Calcula o fatorial de um número.
        :param n: O número a ser calculado.
        :param show: (opcional) Mostrar ou não a conta.
        :return: O valor do Fatorial de um número n.
    """
    tot = 0
    v = 1
    while True:
        tot += n
        if n == 0:
            print(f'= {tot}')
            break
        if show:
            if v == 1:
                print(n, end=' ')
                v = 2
            else:
                print(f'x {n} ', end='')
        n -= 1
fatorial(20, True)