peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
IMC = peso / (altura * altura)

print("Seu IMC é: {:.2f}".format(IMC))

if (IMC < 18.49 ):
    print("Abaixo do peso")
elif (IMC < 24.99):
    print("Peso normal")
elif (IMC < 29.99):
    print("Acima do peso")
else:
    print("Obesidade")

