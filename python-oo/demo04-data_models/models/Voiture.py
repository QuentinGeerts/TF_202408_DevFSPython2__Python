from typing import Any


class Voiture:
    """Classe représentant une voiture"""
    def __init__(self, marque, modele, puissance) -> None:
        self.marque = marque
        self.modele = modele
        self.__annee = 2024
        self.__puissance = puissance
        
    def __str__(self) -> str:
        return f"{self.marque} {self.modele}"
    
    def __repr__(self) -> str:
        return f"Voiture(marque={self.marque}, modele={self.modele})"
    
    def __lt__(self, v2) -> bool:
        return self.puissance < v2.puissance
    
    def __gt__(self, v2) -> bool:
        return self.puissance > v2.puissance
    
    def __eq__(self, v2) -> bool:
        return self.puissance == v2.puissance
    
    def __ne__(self, v2) -> bool:
        return not (self == v2);
    
    @property
    def puissance(self):
        return self.__puissance