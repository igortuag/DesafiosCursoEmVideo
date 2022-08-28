valores = []
for c in range (0, 5):
    v = int(input('Digite um valor: '))
    if c == 0:
        valores.append(v)
        print('Adicionado no final da lista')
    else:
        for val in range(0, len(valores)):
            if valores[val] >= v:
                valores.insert(val, v)
                print(f'Adicionado na posição {val} da lista')
                break
            elif val == len(valores) - 1:
                valores.append(v)
                print('Adicionado no final da lista')
print(valores)