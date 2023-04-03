from Controleur.abstractView import AbstractView

from PyInquirer import prompt, Separator

class InfoView(AbstractView):
    def __init__(self, session):
        super().__init__(session)
        self.questions = [
            {"type": "list",
             "name": "action",
             "message": "Que souhaitez-vous faire ?",
             "choices":["Afficher le contenu de mon Pokédex",
                        Separator(),
                        "Afficher la liste des pokémons capturés",
                        Separator(),
                        "Afficher mon stock de Pokéballs",
                        Separator(),
                        "Afficher le contenu de mon portemonnaie",
                        Separator(),
                        "Changer mon Pokémon actif",
                        Separator(),
                        "Revenir à l'accueil"]}]

    def display_info(self):
        super().display_info()
        with open('assets/pokeball', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        response = prompt(self.questions)
        from Controleur.actionView import ActionView
        from DAO.inventaireDAO import InventaireDAO
        next_view = InfoView(self._session)
        inventaireDAO = InventaireDAO()
        inventaire = inventaireDAO.recuperer(self._session.joueur_actif)
        if response["action"] == "Afficher le contenu de mon Pokédex":
            print("\nIci sont stockées les informations sur les pokémons que vous avez déjà rencontrés :")
            inventaire.pokedex.afficher_pokedex()
        elif response["action"] == "Afficher la liste des pokémons capturés":
            print("\nVoici les caractèrisques des pokémons que vous avez déjà capturés :")
            inventaire.captures.afficher_pokedex()
        elif response["action"] == "Afficher mon stock de Pokéballs":
            inventaire.afficher_pokeball()
        elif response["action"] == "Afficher le contenu de mon portemonnaie":
            inventaire.afficher_argent()
        elif response["action"] == "Changer mon Pokémon actif":
            inventaire.changer_pokemon(self._session.joueur_actif)
        else:
            next_view = ActionView(self._session)
        return next_view