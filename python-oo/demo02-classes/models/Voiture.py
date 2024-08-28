class Voiture:
    
    # Constructeur
    def __init__(self, marque, modele) -> None:
        self.marque = marque
        self.modele = modele
        
    # Méthodes d'instance
    def afficher_details(self):
        print(f"Marque: {self.marque}, modèle: {self.modele}")