s = str(input('Iforme seu sexo: [M/F] ')).upper().strip()
while s not in 'MF':
    s = str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper().strip()
print('Sexo {} registrado com sucesso'.format(s))