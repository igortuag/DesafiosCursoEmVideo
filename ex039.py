sexo = str(input("Você é homem (h) ou mulher (m)? "))
if sexo == "m":
    print("Você não precisa se alistar")
elif sexo == "h":
    from datetime import date
    nasc = int(input("Ano de nascimento: "))
    ano = date.today().year
    idade = ano - nasc
    print("Quem nasceu em {} tem {} anos em {}.".format(nasc, idade, ano))
    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        print("Ainda falta {} anos para o alistamento".format(18-idade))
        print("Seu alistamento será em {}.".format(ano+18-idade))
    else:
        print("Você já deveria ter se alistado há {} anos.".format(idade-18))
        print("Seu alistamento foi em {}.".format(ano+18-idade))

