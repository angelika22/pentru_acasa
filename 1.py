#Se introduc succesiv numere nenule până la introducerea numărului 0. Să se afişeze suma tuturor numerelor introduse.
n=eval(input("dati numarul ="))
s=0
while n!=0:
    s+=n
    n=eval(input("dati numarul ="))
print("suma numerilor este ", s)