print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
v = int(input('Que valor você quer sacar? '))
total = v
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        break
if totced > 0:
    print(f'{totced} cédulas de 50')
ced = 20
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        break
if totced > 0:
    print(f'{totced} cédulas de 20')
ced = 10
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        break
if totced > 0:
    print(f'{totced} cédulas de 10')
ced = 1
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        break
if totced > 0:
    print(f'{totced} cédulas de 1')
print('Obrigado volte sempre!')