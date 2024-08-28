from models.Forme import Forme

class Rectangle (Forme):
    
    def __init__(self, largeur, hauteur) -> None:
        super().__init__()
        self.largeur = largeur
        self.hauteur = hauteur
        self.nom = "Rectangle"
        
    def aire(self):
        return self.hauteur * self.largeur
    
    def perimetre(self):
        return 2 * (self.hauteur + self.largeur)
    
    def __str__(self) -> str:
        return f"{super().__str__()}, hauteur = {self.hauteur}, largeur = {self.largeur}"
        