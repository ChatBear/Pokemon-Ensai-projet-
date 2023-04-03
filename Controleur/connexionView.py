from Controleur.abstractView import AbstractView

from PyInquirer import prompt

from Controleur.actionView import ActionView

class ConnexionView(AbstractView):
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
]

    def display_info(self):
        super().display_info()

    def make_choice(self):
        i=3
        ras = False
        while ras == False:
            if i!=3 and i!=0:
                with open('assets/border.txt', 'r', encoding="utf-8") as asset:
                    print(asset.read())
            if i == 0:
                from Controleur.accueilView import AccueilView
                next_view = AccueilView(self._session)
                print("\nVous avez echoué à vous connecter 3 fois : Peut-être n'avez vous pas encore de compte?")
                ras = True
            else:
                print("Bienvenue dans le menu de connexion!")
                response = prompt(self.questions)
                pseudo = response["pseudo"]
                password = response["password"]
                from Service.connexion import Connexion
                connexion = Connexion()
                if connexion.check_pseudo(pseudo) == True and connexion.check_mdp(pseudo,password) == True:
                    from DAO.joueurDAO import JoueurDAO
                    joueurDAO=JoueurDAO()
                    identifiant=joueurDAO.recuperer_pseudo(pseudo)
                    pass_hash=identifiant[0][1]
                    connexion.sign_in(pseudo, pass_hash, self._session)
                    next_view = ActionView(self._session)
                    ras = True
                else:
                    print('\nVotre pseudo ou mot de passe est erroné!')
                    i = i - 1
        return next_view
