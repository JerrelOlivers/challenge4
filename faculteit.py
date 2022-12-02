def faculteit(x):
    if x == 1:
        return 1
    else:
        return (x * faculteit(x - 1))
x = int(input("Kies je getal: "))
print("De faculteit van", x, "=", faculteit(x))