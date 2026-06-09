nombre = int(input("Donne un nombre : "))
if nombre % 2 == 0:
    print("pair")
else:
    print("impair")
    age = int(input("Quel est ton âge ? "))
if age < 12:
    print("enfant")
elif age < 18:
    print("adolescent")
elif age < 65:
    print("adulte")
else:
    print("senior")