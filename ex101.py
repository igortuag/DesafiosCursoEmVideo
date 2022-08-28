from datetime import date


def voto(idade):
    print(idade)
    if idade < 16:
        voto = 'não vota'
    elif idade < 18 or idade > 70:
        voto = 'voto opcional'
    else:
        voto = 'voto obrigatório'
    return voto


print("-" * 30)
ano = int(input('Em que ano nasceu? '))
id = date.today().year - ano
print(f'Com {id} anos: {voto(id).upper()}.')
