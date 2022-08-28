a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))
if a < b + c and b < a + c and c < a + b:
    print("Os segmentos acima PODEM FORMAR triângulo ", end='')
    if a == b == c:
        print("EQUILATERO!")
    elif a == b or a == c or c == b:
        print("ISÓSCELES!")
    elif a != b != c != a:
        print("ESCALENO!")

else:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo!")
