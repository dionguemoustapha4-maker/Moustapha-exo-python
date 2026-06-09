mot = input("Donne un mot : ")
compteur = 0
for lettre in mot:
    if lettre in "aeiouy":
        compteur = compteur + 1
print("Nombre de voyelles : " + str(compteur))
phrase = input("Donne une phrase : ")
mots = phrase.split(" ")
print("Nombre de mots : " + str(len(mots)))
mot_long = mots[0]
for mot in mots:
    if len(mot) > len(mot_long):
        mot_long = mot
print("Mot le plus long : " + mot_long)