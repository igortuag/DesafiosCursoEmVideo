from datetime import datetime
trab = dict()
trab['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
trab['idade'] = datetime.now().year - nasc
trab['ctps'] = int(input('Carteira de Trbalho (0 não tem): '))
if trab['ctps'] != 0:
    trab['contratação'] = int(input('Ano de Contratação: '))
    trab['salario'] = int(input('Salário: R$'))
    trab['aposentadoria'] = trab['idade'] + ((trab['contratação'] + 35) - datetime.now().year)
for k, v in trab.items():
    print(f' - {k} tem o valor {v}')
