from datetime import date
ano = date.today().year
jovem = 0
velho = 0
for c in range (1, 8):
    p = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    if (ano - p) >= 18:
        velho += 1
    else:
        jovem += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(velho))
print('E também tivemos {} pessoas menores de idade'.format(jovem))