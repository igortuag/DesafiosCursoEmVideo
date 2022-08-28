p = float(input("Qual é seu peso? (Kg) "))
h = float(input("Qual é sua altura? (m) "))
imc = p / (h**2)
print("O IMC dessa pessoa é de {:.1f}".format(imc))
if imc < 18.5:
    print("Você está abaixo do peso normal")
elif imc < 25:
    print("PARABÉNS, você está na faixa de PESO NORMAL")
elif imc < 30:
    print("Você está com Sobrepeso")
elif imc < 40:
    print("Você está em OBESIDADE")
else:
    print("Você está em OBESIDADE MÓRBIDA, cuidado!")