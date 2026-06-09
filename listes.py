nombres = [12, 15, 8, 19, 14]

plus_grand = nombres[0]

for nombre in nombres:
    if nombre > plus_grand:
        plus_grand = nombre

print("Le plus grand nombre est : " + str(plus_grand))