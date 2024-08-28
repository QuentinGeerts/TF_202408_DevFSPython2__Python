# Gestion des erreurs

try:
    # Code susceptible de lever plusieurs types d'erreurs
    nombre = int(input("Entrez un nombre :"))
    resultat = 10 / nombre
    
    if nombre < 0: raise ValueError("Le nombre ne peut pas être négatif.")
except ValueError as e:
    print("Erreur: Vous devez entrer un nombre.")
except ZeroDivisionError:
    print("Erreur: Division par 0 impossible")
except Exception as e:
    print(f"Erreur inattendue: {e}")
else:
    print(f"Résultat de la division : {resultat}")
finally:
    print("Fin de l'opération")

# Lever une exception manuellement
def verifier_age(age):
    if (age < 0):
        raise ValueError("L'âge ne peut pas être négatif")
    else:
        print(f"L'âge est de {age}")
        

try:
    verifier_age(-5)
except ValueError as e:
    print(f"Erreur captuée: {e}")
    