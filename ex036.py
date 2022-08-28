v = int(input("Valor da casa: R$"))
s = int(input("Salário do comprador: R$"))
p = int(input("Quantos anos de financiamento? "))
print("Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}".format(v, p, (v/(12*p))))
if (v/(12*p)) > 0.3*s:
    print("Empréstimo NEGADO!")
else:
    print("Empréstimo pode ser CONCEDIDO!")
