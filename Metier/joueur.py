#from Service.inventaire import Inventaire
from Metier.abstractDresseur import AbstractDresseur

class Joueur(AbstractDresseur):
    def __init__(self, nom, password,  pokemon, etat=False, progression=0):
        """
        constructeur des joueurs (utilisateurs) du jeu
        :param nom: le pseudo du joueur
        :param password: le mot de passe hashé
        :param pokemon: le pokmon actif du joueur
        :param etat: Booléen qui permet de signifier si le joueur est connecté au jeu
        :param progression: le niveau d'avancement du joueur dans le jeu
        """
        super().__init__(nom, pokemon)
        self.etat = etat
        self.progression = progression
        self.password = password  #On stocke le mot de passe hasher

    def verser_gain(self, Inventaire, perte):
        """
        Cette fonction réduit l'argent du joueur lorsqu'il perd un combat
        :param Inventaire: L'incentaire du joueur
        :param perte: La somme perdue par le joueur
        :return: renvoie un message
        """
        if Inventaire.argent <= perte:
            Inventaire.argent = 0 #Si le joueur a moins d'argent que ce qu'il a perdu au combat, il perd tout son argent
        else:
            Inventaire.argent -= perte
            print("Vous avez perdu {} €".format(perte))

    def progresser(self):
        """ Cette fonction a pour rôle de faire évoluer la progression du joueur """
        self.progression += 1
        print("BRAVO!! Vous êtes maintenant au niveau %s",self.progression)

    def connect(self):
        """Cette fonction permet de modifier l'état du joueur afin de signifier qu'il est actuellement connecté au jeu"""
        self.etat = True
        from DAO.joueurDAO import JoueurDAO
        joueurDAO =JoueurDAO()
        joueurDAO.update(self.nom, self.etat)



