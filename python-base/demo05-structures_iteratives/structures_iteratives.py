# Structures itératives


# 1. La boucle for

"""
for variable in séquence:
    # bloc d'instructions
"""

fruits = ["pomme", "banane", "cerise"]

for fruit in fruits:
    print(fruit)
    
message = "bonjour"
for lettre in message:
    print(lettre)
    
# boucle for avec "enumerate()"

for index, fruit in enumerate(fruits):
    print('index:', index)
    print('valeur:', fruit)
    
# boucle for avec "range()"

for i in range(5):
    print(i)
    
for i in range(0, 5, 2):
    print(i)

# 2. La boucle while

"""
while condition:
    # Bloc d'instructions à exécuter tant que la condtion est vraie
"""

compteur = 0

while compteur < 5:
    print(compteur)
    compteur += 1
    
# boucle while avec une condition d'arrêt

reponse = "oui"

while reponse.lower() == "oui":
    
    reponse = input("Voulez-vous continuer ? (oui/non)")
    if (reponse.lower() == "oui"): 
        print("Vous avez choisi de continuer.")
    else:
        print("Vous avez choisi de ne pas continuer.")
        

# 3. Mot-clefs break et continue

# Exemple avec break

for i in range(10):
    if i == 5:
        break; # La boucle s'arrête lorsque i vaut 5
    print(i)

# Exemple avec break

for i in range(10):
    if i == 5:
        continue; # La boucle ignore l'itération lorsque i vaut 5
    print(i)

# 4. Boucles imbriquées

for i in range(3):
    for j in range(2):
        print(f"[{i}, {j}]")