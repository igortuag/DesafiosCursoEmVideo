jog = dict()
jog['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas paridas {jog["nome"]} jogou? '))
gols = list()
jog['total'] = 0
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
jog['gols'] = gols[:]
jog['total'] = sum(gols)
print('-='*30)
print(jog)
print('-='*30)
for k, v in jog.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jog["nome"]} jogou {partidas}.')
for c in range (0, partidas):
    print(f'=> Na partida {c}, fez {jog["gols"][c]} gols.')