from datetime import datetime

class CompteBancaire:
    
    def __init__(self, titulaire: str, solde_initial: float) -> None:
        self.titulaire = titulaire  # public
        self._solde = solde_initial # protected
        self.__historique = []      # private
        self.__date_creation = datetime.now()
        self.__taux_interet = 0.05
        
    def deposer(self, montant: float) -> None:
        """Méthode publique pour déposer de l'argent

        Args:
            montant (float): Le montant à déposer
        """
        if montant > 0:
            self._solde += montant
            self.__ajouter_transaction(f"Dépôt: {montant} euros")
        else:
            print("Montant invalide pour le dépôt.")
            
            
    def retirer(self, montant: float) -> None:
        if 0 < montant <= self._solde:
            self._solde -= montant
            self.__ajouter_transaction(f"Retrait: {montant} euros")
        else:
            print("Montant invalide pour le retrait.")
          
    def _calculer_interet(self) -> float:
        return self._solde * self.__taux_interet
    
    def afficher_solde(self):
        print(f"Le solde de {self.titulaire} est de {self._solde}")
    
    def appliquer_interet (self):
        interet = self._calculer_interet()
        self._solde += interet
        self.__ajouter_transaction(f"Interêt appliqués: {interet} euros")
        print(f"Interêt appliqués, nouveau solde: {self._solde} euros")
            
    def __ajouter_transaction(self, description):
        self.__historique.append(description)
        
    def afficher_historique(self):
        print("Historique des transactions")
        for transaction in self.__historique:
            print(" -", transaction)
            
    def date_creation(self):
        return self.__date_creation
    
    def set_date_creation(self, nouvelle_date):
        self.__date_creation = nouvelle_date
    
    date_creation = property(date_creation, set_date_creation)
    
    @property
    def taux_interet(self) -> float:
        return self.__taux_interet
    
    @taux_interet.setter
    def taux_interet(self, nouveau_taux) -> None:
        self.__taux_interet = nouveau_taux