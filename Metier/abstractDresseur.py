from abc import ABC, abstractmethod

class AbstractDresseur(ABC):
    """
    Cette classe est la classe abstraite dont hériteront les joueurs du jeux ainsi que les dresseurs à affronter pour terminer le jeu
    """
    def __init__(self,nom,pokemon):
        """
        Constructeur commun aux joueurs et aux dresseurs
        :param nom: le nom du joueur ou du dresseur
        :param pokemon: le pokemon actif du joueur ou du dresseur
        """
        self.nom =nom
        self.pokemon=pokemon

    @abstractmethod
    def verser_gain(self):
        pass

