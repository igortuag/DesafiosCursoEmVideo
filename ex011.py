l = float(input("Largura da parede: "))
a = float(input("Altura da parede: "))
print("Sua parede tem a dimensão de {}x{} e sua área é de {}m². \n"
      "Para pintar essa parede, você precisará de {}l de tinta".format(l, a, l*a, l*a/2))