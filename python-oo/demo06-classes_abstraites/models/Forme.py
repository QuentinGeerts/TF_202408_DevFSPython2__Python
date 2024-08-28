from abc import ABC, abstractmethod

class Forme (ABC):
    """Classe abstraite représente une forme générique"""
    
    def __init__(self) -> None:
        self.nom = None
    
    @abstractmethod
    def aire (self):
        """Méthode abstraite pour calculer l'aire de la forme."""
        pass
    
    @abstractmethod
    def perimetre (self):
        """Méthode abstraite pour calculer le périmètre de la forme."""
        pass
    
    def __str__(self) -> str:
        return f"{self.nom}: aire = {self.aire()}, périmètre = {self.perimetre()}"