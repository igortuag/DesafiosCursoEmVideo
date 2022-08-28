print('='*30)
print('     10 TERMOS DE UMA PA')
print('='*30)
n = int(input("Primeiro termo: "))
r = int(input("Razão: "))
for c in range (n, n + r*10, r):
    print('{} →'.format(c), end=' ')
print('Acabou')