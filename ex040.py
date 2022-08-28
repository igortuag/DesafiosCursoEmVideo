n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
m = (n1 + n2) / 2
print("Tirando {} e {}, a média do aluno é {}".format(n1, n2, m))
if m < 5:
    print("O aluno está reprovado!")
elif 5 <= m < 7:
    print("O aluno está de recuperação!")
elif m > 7:
    print("O aluno está aprovado!")
