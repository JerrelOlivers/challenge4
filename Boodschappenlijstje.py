lijstje = []
lijstje.sort(reverse= False) 
producten_nodig = True
while producten_nodig == True:
    
    producten_toevoegen = input("Welk product wil je toevoegen?:  ")
    lijstje.append(producten_toevoegen)
    print("Je boodschappenijstje heeft de volgende producten:  ")
    print("-----")
    for product in lijstje:
        print("-  " + product)
    print("-----")
    
    antwoord = input("Wilt u nog wat anders toevoegen?:  (y/n)  ")
    if antwoord == "n":
        producten_nodig = False
print("Je lijstje ziet er zo uit:  ")
print("-----")
for item in producten_nodig:
    print("-  " + item)
print("-----")