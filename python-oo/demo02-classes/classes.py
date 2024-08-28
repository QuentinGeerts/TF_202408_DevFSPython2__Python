from models.Voiture import Voiture

# Création des objets
v1 = Voiture("Kia", "Ceed")
v2 = Voiture("Opel", "Corsa")

# Appel de la méthode afficher_details pour l'affichage des informations de CHAQUE instance
v1.afficher_details()
v2.afficher_details()