# Sortie

# Affichage d'une simple chaine
print("Bonjour", "tout", "le", "monde")

# Affichage des variables
nom = "Geerts"
prenom = "Quentin"
age = 28

print("Nom:", nom)
print("Prénom:", prenom)

# Affichage d'expression et résultats de calcul
print("La somme de 5 et de 3 vaut", 5 + 3)

# Interpolation de chaine
print(f"Bonjour {nom} {prenom}, vous avez {age} ans.")

# Modification du séparateur et fin de ligne
print("Ceci", "est", "un", "message", sep = " | ", end = "❤️")
# Affichage: Ceci | est | un | message❤️

print()

# Entrée

nom = input("Entrez votre nom :")
print("bonjour", nom)

age = input("Entrez votre âge :")
print(f"Vous avez {age} ans.")

# Conversion de type

# str → int => int()
nombre = input("Entrez un nombre:")
nombre = int(nombre)

# str → float => float()
# int, float → str => str()

nombre = int(input("Entrez un nombre :"))
carre = nombre ** 2