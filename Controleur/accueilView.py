# coding=utf-8
from Controleur.abstractView import AbstractView

from PyInquirer import prompt, Separator

# est ce que l'on a besoin de la classe Acceuil du coup? cf Inscription et connexion
class AccueilView(AbstractView):
    def __init__(self, session):
        super().__init__(session)
        self.questions = [{"type": "list", "name": "authentification", "message": "Bienvenue dans notre application pokemon!", "choices":["Me créer un compte", Separator(), "Me connecter", Separator(), "Quitter le jeu"]}]

    def display_info(self):
        super().display_info()

    def make_choice(self):
        response = prompt(self.questions)
        if response["authentification"] == "Me connecter":
            from Controleur.connexionView import ConnexionView
            next_view =  ConnexionView(self._session)
        elif response["authentification"] == "Me créer un compte":
            from Controleur.inscriptionView import InscriptionView
            next_view = InscriptionView(self._session)
        else:
            next_view = None
        return next_view


