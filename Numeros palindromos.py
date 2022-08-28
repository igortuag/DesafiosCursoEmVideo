palindromos = list()
for c in range (0, 10000):
    n = str(c)
    s = n.split()
    j = ''.join(s)
    i = ''
    for d in range(len(j) - 1, -1, -1):
        i += j[d]
    if j == i:
        palindromos.append(c)
print(palindromos)
