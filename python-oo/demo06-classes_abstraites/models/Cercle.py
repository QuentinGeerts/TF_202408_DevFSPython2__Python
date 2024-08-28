from models.Forme import Forme
import math

class Cercle (Forme):
    
    def __init__(self, rayon) -> None:
        super().__init__()
        self.rayon = rayon
        self.nom = "Cercle"
        
    def aire(self):
        return math.pi * self.rayon ** 2
    
    def perimetre(self):
        return 2 * math.pi * self.rayon

    def __str__(self) -> str:
        return f"{super().__str__()}, rayon = {self.rayon}"