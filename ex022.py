nome = str(input("Digite seu nome completo: ")).strip()
print("Analisando seu nome...")
print("Seu nome em maiúsculas é {}".format(nome.upper()))
print("Seu nome em mainúsculas é {}".format(nome.lower()))
snome = nome.split()
jnome = "".join(snome)
print("Seu nome tem ao todo {} letras".format(len(jnome)))
print("Seu primeiro nome é {} e ele tem {} letras".format(snome[0], len(snome[0])))