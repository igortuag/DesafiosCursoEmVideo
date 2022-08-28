palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO',
            'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO',
            'PROGRAMADOR', 'FUTURO')
for c in palavras:
    print(f'\nNa palavra {c} temos ', end='')
    for l in c:
        if l in 'AEIOU':
            print(l, end=' ')
