#Elaborați un program care va calcula suma, produsul și media aritmetică a numerelor de la 1 la n, pentru n introdus de la tastatură.
n=eval(input("n= "))
a=1
b=0
c=1
while a<=n:
    b+=a
    c*=a
    a+=1
print(f"suma {b}, produsul {c}, media aritmetica {b/n}")