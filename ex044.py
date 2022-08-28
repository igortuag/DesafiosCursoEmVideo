print("="*10 + " LOJAS DO TUAG " +"="*10)
c = float(input("Preços das compras: R$"))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
{ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
o = int(input("Qual é a opção? "))
if o == 1:
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(c,c*0.9))
elif o == 2:
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(c, c * 0.95))
elif o == 3:
    print("Sua compra será parcelada em 2x de R${:.2f} sem JUROS".format(c / 2))
elif o == 4:
    p = int(input("Quantas parcelas?"))
    print("Sua compra será parcelada em {}x de R${:.2f} COM JUROS".format(p, (c*1.2) / p))
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(c, c*1.2))