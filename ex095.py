time = list()
jog = dict()
gols = list()
opc = ""
while True:
    jog.clear()
    jog['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas paridas {jog["nome"]} jogou? '))
    jog['total'] = 0
    gols.clear()
    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {c}? ')))
    jog['gols'] = gols[:]
    jog['total'] = sum(gols)
    time.append(jog.copy())
    while True:
        opc = str(input('Quer continuar? [S/N] ')).upper()[0]
        if opc in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if opc in 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jog.keys():
    print(f'{i:<15}', end= '')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    busca = int(input('Mostrar dados de qual jogador?(999 para parar) '))
    if busca == 999:
        break
    if busca > len(time) - 1:
        print(f'Erro! Não existe jogador com código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<< Volte Sempre >>')