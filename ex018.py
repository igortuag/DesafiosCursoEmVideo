from math import sin, cos, tan, radians
ang = float(input("Digite o número que você deseja: "))
rad = radians(ang)
print("O ângulo de {} tem o SENO de {:.2f} \n"
      "O ângulo de {} tem o COSSENO de {:.2f} \n"
      "O ângulo de {} tem a TANGENTE de {:.2f}"
      .format(ang, sin(rad), ang, cos(rad), ang, tan(rad)))