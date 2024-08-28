# Encapsulation

from models.CompteBancaire import CompteBancaire
from datetime import datetime
# public : 
# → Accessible partout
# protected : _
# → Accessible partout mais destiné à un usage interne
# private : __
# → Accessible uniquement dans la classe

# Création d'un compte bancaire
compte = CompteBancaire("Quentin", 1000)

print(compte.date_creation)
# compte.date_creation = datetime.now() # Impossible car la propriété est en lecture seule
print(compte._solde)

# Taux interet
compte.taux_interet = 0.10
print(f"Taux interet du compte : {compte.taux_interet}")

# Effectuer des transactions
compte.deposer(500)
compte.deposer(200)
compte.retirer(50)
compte.retirer(150)
compte.deposer(600)
compte.retirer(50)

# Appliquer les interêts
compte.appliquer_interet()

# Afficher le solde et l'historique du compte
compte.afficher_solde()
compte.afficher_historique()

# Tentatives d'accès aux membres privés
# print(compte.__historique) # provoque une erreur
# compte.__ajouter_transaction("Test") # provoque une erreur