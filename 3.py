#Se citesc numere de la tastatură până la introducerea unui număr impar divizibil cu 3. Să se afişeze suma tuturor numerelor pare introduse.
a=0
b=0
while not((a%2!=0) and (a%3==0)):
    a=eval(input("dati un numar: "))
    if a%2==0:
        b+=a
print("suma tuturor numere pare este ", b)