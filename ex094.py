pessoa = dict()
galera = list()
opc = ''
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: '))
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    opc = str(input('Quar Continuar? [S/N]: '))
    galera.append(pessoa.copy())
    if opc in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas')
média = soma / len(galera)
print(f'A média de idade é de {média:5.2f} anos.')
print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print('')
print('Lista das pessoas que estão acima da média: ', end='')
for p in galera:
    if p['idade'] >= média:
        print(f'{p["nome"]} ', end='')
print('')