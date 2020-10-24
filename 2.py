#Se citesc pe rând temperaturile medii ale fiecărei luni a unui an, ca numere întregi. Să se afişeze cu două zecimale media anuală a temperaturilor pozitive şi a celor negative. 
s_p=0
s_n=0
nr_p=0
nr_n=0
l=1
while l<=12:
    t=eval(input("dati temperatura lunii: "))
    if t>=0:
        s_p+=t
        nr_p+=1
    if t<0:
        s_n+=t
        nr_n+=1
    l+=1
print(f"media anuala a temperaturiloe pozitive este {round(s_p/nr_p, 2)}, media anuala a temperaturilor negative este {round(s_n/nr_n, 2)}")
        