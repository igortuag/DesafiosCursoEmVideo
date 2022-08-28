p = 0
m = 0
j = 0
h = 0
while True:
    print('-'*30)
    print('     CADASTRE UMA PESSOA')
    print('-' * 30)
    i = int(input('Idade: '))
    s = str(input('Sexo: [M/F]')).upper().strip()
    p += 1
    if i >= 18:
        m += 1
    if s == 'M':
        h += 1
    if s == 'F' and i < 20:
        j += 1
    print('-' * 30)
    c = str(input('Quer continuar? [S/N]')).upper().strip()
    if c == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {m}')
print(f'Ao todo temos {h} homens cadastrados')
print(f'E temos {j} mullhers com menos de 20 anos')
