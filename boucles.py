n = int(input("Donne un nombre : "))
somme = 0
i = 1
while i <= n:
    somme = somme + i
    i = i + 1
print("La somme de 1 à " + str(n) + " est : " + str(somme))
nombre = int(input("Donne un nombre : "))
i = 1
while i <= 10:
    print(str(nombre) + " x " + str(i) + " = " + str(nombre * i))
    i = i + 1