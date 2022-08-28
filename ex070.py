print('-'*30)
print('     LOJAS SUPER BARATÃO')
print('-'*30)
caro = barato = soma = 0
nbarato = ''
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    if soma == 0:
        barato = preço
    if preço > 1000:
        caro += 1
    if preço < barato:
        barato = preço
        nbarato = produto
    soma += preço
    opção = str(input('Quer continuar [S/N] ')).upper().strip()
    if opção == "N":
        break
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {caro} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nbarato} que custa {barato:.2f}')