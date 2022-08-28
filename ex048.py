tot = 0
v = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        tot += c
        v += 1
print('A soma de todos os {} valores solicitados é {}'.format(v,tot))