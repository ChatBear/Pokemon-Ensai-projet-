from Controleur.abstractView import AbstractView
from PyInquirer import prompt, Separator

class ActionView(AbstractView):
    def __init__(self, session):
        super().__init__(session)
        self.questions = [
            {"type": "list",
             "name": "action",
             "message": "Que souhaitez-vous faire ?",
             "choices":["Acceder à mon inventaire",
                        Separator(),
                        "Explorer les hautes herbes",
                        Separator(),
                        "Rencontrer des dresseurs",
                        Separator(),
                        "Acheter des pokéballs",
                        Separator(),
                        "Me déconnecter"]}]

    def display_info(self):
        super().display_info()

    def make_choice(self):
        response = prompt(self.questions)
        if response["action"] == "Acceder à mon inventaire":
            from Controleur.infoView import InfoView
            next_view = InfoView(self._session)
        elif response["action"] == "Explorer les hautes herbes":
            from Controleur.combatView import CombatView
            next_view = CombatView(self._session, False)
        elif response["action"] == "Rencontrer des dresseurs":
            from Controleur.combatView import CombatView
            next_view =  CombatView(self._session, True)
        elif response["action"] == "Acheter des pokéballs":
            from Controleur.achatView import AchatView
            next_view =  AchatView(self._session)
        else:
            from DAO.joueurDAO import JoueurDAO
            joueurDAO = JoueurDAO()
            joueurDAO.update(self._session.joueur_actif.nom, False)
            self._session.joueur_actif = None
            from Controleur.accueilView import AccueilView
            next_view = AccueilView(self._session)
        return next_view