v = int(input("Qual é a velocidade atual do carro? "))
if v > 80:
    m = (v-80)*7
    print("\033[31mMULTADO! Você excedeu o limite permitido que é de 80Km/h \n"
          "Você deve pagar uma multa de \033[33mR${:.2f}".format(m))
print("\033[32mTenha um bom dia! Dirija com segurança!")