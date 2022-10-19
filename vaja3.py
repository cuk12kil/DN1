a = input("vnesi prvo stevilo:")
a = int(a)

b = input("vnesi drugo stevilo:")
b= int(b)

c = input("vnesi tretje stevilo:")
c= int(c)

print("Sestevek a = "+str(a) + "  tipa  " + str(type(a)))
print("Sestevek a = "+str(b) + "  tipa  " + str(type(b)))
print("Sestevek a = "+str(c) + "  tipa  " + str(type(c)))

if (a == b and c <= a) :
    print("druga vrednost je enaka prvi vrednosti in tretja vrednost manjša ali enaka prvi")

else :
    print("pogoj ne drzi")

