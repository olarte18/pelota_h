#input
h=int(input("digite el valor de h: "))

#processing
ch=h/5
m=0

while h>ch:
    h= h-(0.10*h)
    m=m+1

#output
print("la pelota rebotara la 5 parte de la altura inicial en el rebote: "+str(m))
