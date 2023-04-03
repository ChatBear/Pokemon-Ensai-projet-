from DAO.pokedexDAO import PokedexDAO
from Metier.Pokemon import Pokemon
from Metier.Statistique import Statistique
import pandas as pd
import numpy as np

class Pokedex():
    def __init__(self, dict=None, pkm = None):
        if pkm == None:
            self.pokemons = dict
        else :
            self.pokemons = pkm

    def afficher_pokedex(self):
        index = np.arange(len(self.pokemons))
        columns = ["nom", "niveau","type 1", "type 2", "pv", "attaque", "défense", "vitesse"]
        liste = []
        for value in self.pokemons.values():
            liste.append(Pokedex.afficher_pokemon(self,pokemon=value, afficher=False))
        df = pd.DataFrame(liste, index = index, columns = columns)
        print(df, "\n")


    def afficher_pokemon(self,pokemon, afficher=True):
        names = pokemon.nom
        niveau = pokemon.niveau
        type1 = pokemon.types[0].nom
        type2 = type1
        if len(pokemon.types) > 1:
            type2 = pokemon.types[1].nom
        pv = pokemon.stat.pv
        attaque = pokemon.stat.attaque
        defense = pokemon.stat.defense
        vitesse = pokemon.stat.vitesse
        if afficher == True :
            print(names,niveau,type1,type2, pv, attaque, defense, vitesse)
        return(names,niveau,type1,type2, pv, attaque, defense, vitesse)

"""from Webservice.pokemonAPI import PokemonAPI
pkm = {"Pokemon 1":PokemonAPI.getPokemon(6,1),"Pokemon 2": PokemonAPI.getPokemon(4,1),"Pokemon 3" :PokemonAPI.getPokemon(7,1)}
print(pkm)
print(pkm.values())
print(pkm.keys())
index = []
for key in pkm.keys():
    index.append(key)
print(index)
Pokedex(pkm=pkm).afficher_pokedex()"""