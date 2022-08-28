ne = ('zero',"um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
      "déz", 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis',
      'dezesete', 'dezenove', 'vinte')
n = int(input('Digite um número entre 0 e 20: '))
while n < 0 or n > 20:
    n = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {ne[n]}')