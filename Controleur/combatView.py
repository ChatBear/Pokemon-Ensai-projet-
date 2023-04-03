from Controleur.abstractView import AbstractView
from Metier.joueur import Joueur
from Metier.dresseur import Dresseur
import numpy as np
from PyInquirer import prompt, Separator
import pandas as pd
class CombatView(AbstractView):
    def __init__(self, session, duel):
        # ajout d'un attribut
        super().__init__(session)
        self.questions = [
            {"type": "list",
             "name": "action",
             "message": "Que souhaitez-vous faire ?",
             "choices":["Attaquer le pokémon adverse",
                        Separator(),
                        "Attraper le pokémon adverse",
                        Separator(),
                        "Prendre la fuite",
                        ]}]
        self.duel = duel

    def afficher_dresseur(self,L):
        #L represente une liste de dresseur
        index = np.arange(len(L))
        columns = ["nom","niveau","Pokemon","Gain"]
        List = []
        for dresseur in L:
            List2 =[dresseur.nom,dresseur.pokemon.niveau,dresseur.pokemon.nom,dresseur.gain]
            List.append(List2)
        df = pd.DataFrame(List,index,columns)
        print(df)
        i = int(input("\nVeuillez choisir le numéro du dresseur que vous voulez affronter "))
        print("\nVous affrontez le " + L[i].nom + "\n\t" + L[i].phrase + "\n")

        return L[i]

    def display_info(self):
        super().display_info()
        if self.duel == True:
            with open('assets/arene', 'r', encoding="utf-8") as asset:
                print(asset.read())
        else:
            with open('assets/herbes', 'r', encoding="utf-8") as asset:
                print(asset.read())

    def make_choice(self):

        ras = False
        from Controleur.actionView import ActionView
        from Service.combat import Combat
        from Webservice.pokemonAPI import PokemonAPI

        next_view = ActionView(self._session)
        if self.duel == True:
            joueur = self._session.joueur_actif
            from DAO.pokemonDAO import PokemonDAO
            pokemonDAO = PokemonDAO()
            id = pokemonDAO.recup_ID(joueur,joueur.pokemon.nom)
            joueur.pokemon = pokemonDAO.recuperer(id)
            from DAO.dresseurDAO import DresseurDAO
            List_dresseur = DresseurDAO().recuperer(self._session.joueur_actif)
            joueur = self._session.joueur_actif
            if List_dresseur == None:
                return next_view
            dresseur = self.afficher_dresseur(List_dresseur)
            print(dresseur.pokemon.nom)
            combat = Combat(self._session.joueur_actif.pokemon, dresseur.pokemon,joueur,self.duel)
            while ras == False:
                ras = combat.attaquer(self._session.joueur_actif, self.duel)
            from DAO.inventaireDAO import InventaireDAO
            inventaireDAO = InventaireDAO()
            inventaire = inventaireDAO.recuperer(self._session.joueur_actif)
            if ras[1] == True:
                dresseur.verser_gain(inventaire)
            else:
                 self._session.joueur_actif.verser_gain(inventaire, dresseur.gain)
            inventaireDAO.update_argent(inventaire.argent, self._session.joueur_actif)

        else:
            #Génération d'un pokemon aléatoire parmi les 3 premières génération
            i = np.random.randint(1,365)
            joueur = self._session.joueur_actif
            lvl = joueur.pokemon.niveau


            pokemonAPI = PokemonAPI()
            pokemon =  pokemonAPI.getPokemon(i,lvl)



            from DAO.pokedexDAO import PokedexDAO
            PokedexDAO().remplir(joueur,pokemon,False, False)
            print("\nVous affrontez le pokémon " + pokemon.nom + " au niveau " + str(pokemon.niveau))



            joueur = self._session.joueur_actif
            print("\nVotre pokémon actif est " + joueur.pokemon.nom + " au niveau " + str(joueur.pokemon.niveau))

            combat = Combat(joueur.pokemon, pokemon,joueur)
            while ras == False:
                response = prompt(self.questions)
                if response["action"] == "Attaquer le pokémon adverse":
                    ras = combat.attaquer(self._session.joueur_actif,False)
                elif response["action"] == "Attraper le pokémon adverse":
                    question= [
                        {"type": "list",
                         "name": "choix",
                         "message": "Quel Type de Pokéball souhaitez vous utiliser?",
                         "choices": ["Pokéball",
                                     Separator(),
                                     "Superball",
                                     Separator(),
                                     "Hyperball"
                                     ]}]
                    reponse = prompt(question)
                    ras = combat.attraper(joueur, reponse["choix"])
                else :
                    ras = combat.fuire(self._session.joueur_actif)
        return next_view








