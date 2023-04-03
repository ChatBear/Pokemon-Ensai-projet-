from Controleur.abstractView import AbstractView

from PyInquirer import prompt

class InscriptionView(AbstractView):
    def __init__(self, session):
        super().__init__(session)
        self.questions = [{
        'type': 'input',
        'name': 'pseudo',
        'message': 'Veuillez entrer un pseudo',
    },
    {
        'type': 'password',
        'message': 'Entrez votre mot de passe',
        'name': 'password'
    },
    {
        'type': 'password',
        'message': 'Confirmez votre mot de passe',
        'name': 'password_confirmation'
    }
]

    def display_info(self):
        super().display_info()

    def make_choice(self):
        ras = False
        i=1
        while ras == False:
            if i != 1:
                with open('assets/border.txt', 'r', encoding="utf-8") as asset:
                    print(asset.read())
            i+=1
            print("Bienvenue dans le menu pour valider votre inscription!\n\n Votre mot de passe doit contenir entre 6 et 20 caractères dont au moins :\n\tUne majuscule\n\tUn chiffre\n\tEt un des symboles $ @ # %\n\n")
            response = prompt(self.questions)
            pseudo = response["pseudo"]
            password = response["password"]
            confirmation = response["password_confirmation"]
            from Service.inscription import Inscription
            inscription = Inscription()
            ras = inscription.check_pseudo(pseudo)
            if ras == True :
                if password == confirmation:
                    ras = inscription.check_mdp(password)
                    if ras == True:
                        pkm = inscription.choix_pkm()
                        passw_hash = inscription.hashage(password)
                        from DAO.joueurDAO import JoueurDAO
                        joueurDAO = JoueurDAO()
                        joueurDAO.creer(pseudo, passw_hash)
                        from Metier.joueur import Joueur
                        joueur = Joueur(pseudo,passw_hash, pkm)
                        from DAO.pokedexDAO import PokedexDAO
                        pokedexDAO = PokedexDAO()
                        pokedexDAO.remplir(joueur, joueur.pokemon, True, True)
                        print("\nVotre inscription a bien été validée ! \nVous pouvez commencer la partie!\n")
                        from Controleur.connexionView import ConnexionView
                        next_view = ConnexionView(self._session)
                        return next_view
                else:
                    print("\nMot de passe incorrect! Il ne correspond pas à votre mot de passe de confirmation. \nVeuillez recommencer.\n")
                    ras = False

