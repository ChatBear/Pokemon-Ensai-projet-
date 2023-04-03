import hashlib
from Metier.joueur import Joueur
from Service.inscription import Inscription
from DAO.joueurDAO import JoueurDAO
from Controleur.session import Session

class Connexion():
    def __init__(self):
        pass

    def check_mdp(self, pseudo, utilisateur_mdp):
        joueur = JoueurDAO.recuperer_pseudo(pseudo) #Utilise la fonction recuperer de JoueurDAO qui à partir du pseudo devrait recupérer toutes les infos sur le joueur dans un dictionnaire
        mdp_bdd = joueur[0][1] #recuperation du mot de passe enregistré dans la base
        hashed_mdp_bdd, salt = mdp_bdd.split(':') #On sépare le mot de passe du sel
        contenu = salt + utilisateur_mdp
        h = hashlib.new('md5')
        h.update(contenu.encode('utf-8'))
        return hashed_mdp_bdd== h.hexdigest()

    def check_pseudo(self, pseudo):
        reponse = False
        if JoueurDAO.recuperer_pseudo(pseudo) != []:
            reponse = True
        return reponse

    def sign_in(self, pseudo,password, session):
        joueurDAO=JoueurDAO()
        search = joueurDAO.recuperer(pseudo, password) #Recherche le joueur dans base de données par son pseudo
        search.connect() #Connecte le joueur
        session.joueur_actif= search #Mise à jour de la session


