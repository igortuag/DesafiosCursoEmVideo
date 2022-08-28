n = int(input("\033[35mMe diga um número qualquer: "))
if n % 2 == 0:
    print("\033[30mO número {} é \033[34mPAR".format(n))
else:
    print("\033[30mO número {} é \033[34mÍMPAR".format(n))