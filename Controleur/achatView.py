from Controleur.abstractView import AbstractView

from PyInquirer import prompt, Separator

class AchatView(AbstractView):
    def __init__(self, session):
        super().__init__(session)
        # regarder quels types de questions sont adéquats
        self.question1 = [
            {"type": "list",
             "name": "action",
             "message": "Quel Type de Pokéball souhaitez vous acheter ?",
             "choices":["Acheter une pokéball",
                        Separator(),
                        "Acheter une superball",
                        Separator(),
                        "Acheter une hyperball",
                        Separator(),
                        "Revenir plus tard"
            ]}]
        self.question2 = [
            {'type': 'input',
            'name': 'quantite',
            'message': 'Combien en voulez-vous ?'
            }]

    def display_info(self):
        super().display_info()
        with open('assets/boutique', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        from Controleur.actionView import ActionView
        from Service.achat import Achat
        achat = Achat(self._session.joueur_actif)
        next_view = ActionView(self._session)
        ras = False
        i=0
        while ras == False:
            if i != 0:
                with open('assets/border.txt', 'r', encoding="utf-8") as asset:
                    print(asset.read())
            i += 1
            achat.afficher_inv()
            response1 = prompt(self.question1)
            if response1["action"] == "Revenir plus tard":
                ras = True
            else:
                if response1["action"] == "Acheter une pokéball":
                    type = "pokeball"
                elif response1["action"] == "Acheter une superball":
                    type = "superball"
                elif response1["action"] == "Acheter une hyperball":
                    type = "hyperball"
                response2 = prompt(self.question2)
                quantite=response2["quantite"]
                achat.acheter(type, quantite, self._session.joueur_actif)
        return next_view
