from Metier.abstractDresseur import AbstractDresseur
from Metier.joueur import Joueur
from Service.inventaire import Inventaire
#from pokemon.Metier.abstractDresseur import AbstractDresseur

class Dresseur(AbstractDresseur):
    def __init__(self,nom,pokemon,phrase,gain,niveau, statut=False):
        """
        Constructeur des dresseurs qui sont enregistrés dans la base et que les joueurs doivent affronter pour terminer le jeu
        :param nom: nom du dresseur
        :param pokemon: le pokemon du dresseur
        :param phrase: Chaque dresseur a une phrase qui lui est spécifique( comme une accroche)
        :param gain: les gains gagné par le joueur lorsqu'il bat le dressuer
        :param niveau: Le niveau du joueur dans la file des dresseurs
        :param statut: Booléen indiquant si le dresseur a été débloqué
        """
        super().__init__(nom,pokemon)
        self.phrase=phrase
        self.gain=gain
        self.statut=statut
        self.niveau= niveau


    def verser_gain(self,Inventaire):
        """
        Cette fonction permet de verser les gains dans l'inventaire du joueur lorsqu'il réussit à vaincre le dresseur
        :param Inventaire: L'inventaire du joueur ayant vaincu le dresseur
        :return: renvoie une phrase de félicitations mentionnant la somme gagné par le joueur
        """
        Inventaire.argent += self.gain
        print("Vous avez remporté {} €".format(self.gain))

    #def debloquer_dresseur(self,progression):
        #if progression == self.niveau -1 :
            #self.statut = True


