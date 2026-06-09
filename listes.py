nombres = [12, 15, 8, 19, 14]
plus_grand = nombres[0]
for nombre in nombres:
    if nombre > plus_grand:
        plus_grand = nombre
print("Le plus grand nombre est : " + str(plus_grand))
notes = [12, 15, 8, 19, 14]
total = 0
for note in notes:
    total = total + note
moyenne = total / len(notes)
print("Moyenne : " + str(moyenne))
compteur = 0
for note in notes:
    if note > moyenne:
        compteur = compteur + 1
print("Notes au-dessus de la moyenne : " + str(compteur))