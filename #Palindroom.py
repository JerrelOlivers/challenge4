#Palindroom
x = input("Vul je woord in: ").lower()
def Palindroom(x):
    return x == x [::-1]

if x == x [::-1]:
    print("Dit is een palindroom")
    
else:
    print("Dit is geen palindroom")

    