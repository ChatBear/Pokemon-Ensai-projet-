#from DAO.inventaireDAO import inventaireDAO
import pandas as pd
import numpy as np
from PyInquirer import prompt

class Inventaire():
    def __init__(self, argent=0, nb_pokeball=0, captures=None, pokedex=None):
        self.argent=argent
        self.nb_pokeball=nb_pokeball
        self.captures=captures
        self.pokedex=pokedex


    def afficher_argent(self):
        print("\nVous avez {} € dans votre porte-monnaie !".format(self.argent))

    def afficher_pokeball(self):
        index = ["Pokéball(s)", "Superball(s)", "Hyperball(s)"]
        columns = ["quantité"]
        liste = [self.nb_pokeball["Pokéball"],self.nb_pokeball["Superball"],self.nb_pokeball["Hyperball"] ]
        df = pd.DataFrame(liste, index=index, columns=columns)
        print("\nVoici votre stock de pokéballs pour capturer de nouveaux pokémons!\n", df, "\n")


    def changer_pokemon(self, joueur):
        self.captures.afficher_pokedex()
        question = [{
        'type': 'input',
        'name': 'choix_pokemon',
        'message': 'Quel pokémon voulez-vous utiliser lors de vos différents combats ?',
    }
]
        liste = self.captures.pokemons.values()
        liste_noms =[]
        for pok in liste:
            liste_noms.append(pok.nom)
        reponse = prompt(question)
        if not (reponse["choix_pokemon"] in liste_noms):
            print("\nCe Pokémon n'existe pas parmi ceux que vous avez capturés!")
        else :
            from DAO.inventaireDAO import InventaireDAO
            inventaireDAO = InventaireDAO()
            id_pok = inventaireDAO.update_pkm_actif(reponse["choix_pokemon"], joueur)
            from DAO.pokemonDAO import PokemonDAO
            pokemonDAO = PokemonDAO()
            new_pok = pokemonDAO.recuperer(id_pok)
            joueur.pokemon = new_pok
            print("\nL'échange de pokémons s'est bien déroulé!")