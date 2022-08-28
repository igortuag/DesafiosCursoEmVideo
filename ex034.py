salario = int(input("Qual o salrário do funcionário? R$"))
if salario <= 1250:
    print("Quem ganhava R${} passa a ganhar R${:.2f} agora.".format(salario, salario*1.15))
else:
    print("Quem ganhava R${} passa a ganhar R${:.2f} agora.".format(salario, salario*1.10))