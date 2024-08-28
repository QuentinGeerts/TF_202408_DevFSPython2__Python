# Methodes

# Procédure: Ne retourne rien
# Fonction: Retourne quelque chose

# 1. Méthode simple sans argument

def saluer():
    print("Bonjour tout le monde !")

# Appel de la méthode
saluer()

# 2. Méthode avec arguments

def saluer_utilisateur(prenom):
    print(f"Bonjour {prenom} !")
    
# Appel de la méthode
saluer_utilisateur("Quentin")

# 3. Méthode avec valeur de retour

def additionner(a, b):
    return a + b

# Appel de la méthode
resultat = additionner(5, 3)
print(f"5 + 3 = {resultat}")

# 4. Méthode avec paramètres par défaut

def saluer_utilisateur (prenom = "Invité"):
    print(f"Bonjour {prenom} !")
    
# Appel de la méthode
saluer_utilisateur();
saluer_utilisateur("Mister Quentin");
saluer_utilisateur(prenom = "Mister Quentin");

# 5. Méthode avec plusieurs retours

def diviser_et_reste(a, b):
    quotient = a // b
    reste = a % b
    return quotient, reste

# Appel de  la méthode
q, r = diviser_et_reste(10, 3)
print(f"Quotient: {q}, reste: {r}")

# 6. Méthode avec des arguments variables

# - Avec *args (nombre indéterminé d'arguments)
def addition_tout(*args):
    return sum(args)

# Appel de la fonction avec un nombre variable d'arguments
print(addition_tout(1, 2, 3, 4)) # Affichage: 10
print(addition_tout(10, 20)) # Affichage: 30

# - Avec **kwargs (nombre indéterminé d'arguments nommés)
def afficher_infos(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
        
# Appel de la fonction avec des arguments nommés
afficher_infos(nom='Quentin', age=28, ville="Virelles")