import random
import time

totaal = int(0)
y = int(input("Hoeveel dobbelstenen wil je gooien?: "))
print("De dobbelstenen worden gegooid.... ")
time.sleep(1)
print("rammel rammel")
time.sleep(1)
print("rammel rammel")
time.sleep(1)
print("rammel rammel")
time.sleep(1)
print("Je gooit.... ")
for i in range (y):
    eind1 = (random.randint(1,6))
    print("Je rolt: ", eind1,)
    totaal += eind1
print("Je totaal is: ", totaal,)