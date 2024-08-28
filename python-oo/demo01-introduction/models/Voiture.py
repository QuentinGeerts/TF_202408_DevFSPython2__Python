# Définition d'un classe
class Voiture:
    
    # Constructeur
    def __init__(self, marque: str, modele: str) -> None:
        """ Constructeur d'une voiture """
        self.marque = marque
        self.modele = modele
    
if __name__ == "__main__":
    voiture = Voiture("Kia", "Ceed")
    print("Voiture:", voiture)
    
def saluer():
    print("Bonjour !")