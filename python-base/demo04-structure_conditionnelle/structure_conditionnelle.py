# Structure conditionnelle


# Structure du if

"""
if condition:
    # bloc d'instructions à exécuter si la condition est vraie
"""

age = 18
if age >= 18:
    print("Vous êtes majeur.")
    
# Structure du if avec else

"""
if condition:
    # bloc d'instructions à exécuter si la condition est vraie
else:
    # bloc d'instructions à exécuter si la condition est fausse
"""

age = 18
if age >= 18:
    print("Vous êtes majeur.")
else:
    print("Vous êtes mineur.")
        
# Structure du if, elif et else

"""
if condition1:
    # bloc d'instructions à exécuter si la condition1 est vraie
elif codition2:
    # bloc d'instructions à exécuter si la condition2 est vraie
elif codition3:
    # bloc d'instructions à exécuter si la condition3 est vraie
else:
    # bloc d'instructions à exécuter si toutes les autres conditions sont fausses
"""

age = 18
if age >= 18:
    print("Vous êtes majeur.")
elif age >= 13:
    print("Vous êtes adolescent.")
else:
    print("Vous êtes mineur.")
    
# Utilisation de conditions multiples avec les opérateurs logiques

temperature = 25
ensoleille = True

if (temperature > 20 and ensoleille):
    print("Il faut beau et chaud dehors.")
elif temperature > 20 or ensoleille:
    print("Il fait chaud ou il y a du soleil")
else:
    print("Il fait froid et il n'y a pas de soleil")
    
    
# Opérateur ternaire

age = 18

statut = "Majeur" if age >= 18 else "Mineur"

# Match (A partir de Python 3.10)

"""
match parameter:
    case pattern1:
        # code for pattern 1
    case pattern2:
        # code for pattern 2
    .
    .
    case patterN:
        # code for pattern N
    case _:
        # default code block
"""

choix = input("Entrez un choix:")

match choix:
    case "1":
        print("Menu 1")
    case "2":
        print("Menu 2")
    case "3":
        print("Menu 3")
    
    case _:
        print("Quitter")


def type_variable (valeur):
    
    match valeur:
        
        case int():
            print("La valeur est un entier")
        case str():
            print("La valeur est une string")
        case list():
            print("La valeur est un ensemble d'éléments")
        case _:
            print("Type non reconnu")
            

type_variable(5)
type_variable("5")
type_variable([5, 3, 3])
type_variable(2.4)

def verification_valeur (nombre):
    
    if type(nombre) != int and type(nombre) != float: return
    
    match nombre:
        case x if x > 0:
            print("Le nombre est positif")
        case x if x < 0:
            print("Le nombre est négatif")
        case 0:
            print("Zéro")
        case _:
            print("Valeur non supportée")
            
            
verification_valeur(5)
verification_valeur(-5)
verification_valeur(0)
verification_valeur('a')