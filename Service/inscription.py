import hashlib
import secrets
from Metier.Pokemon import Pokemon
from Webservice.pokemonAPI import PokemonAPI
from Metier.Pokedex import Pokedex
#from Metier.joueur import Joueur
from DAO.pokedexDAO import PokedexDAO
from PyInquirer import prompt, Separator
import os
from DAO.joueurDAO import JoueurDAO

class Inscription():
    def __init__(self):
        pass

    @staticmethod
    def hashage(mdp):
        salt = secrets.token_hex(16) #On génere un sel à un nombre aléatoire hexadécimale à l’aide de la fonction secrets.token_hex().
        contenu = salt + mdp
        contenu= contenu.encode('utf-8')  # avant de hacher le texte il faut l'encoder d'abord avec de l'utf-8
        h= hashlib.new('md5') #ici on choisit le type de hachage qu'on veut utiliser, en occurence ici 'md5'
        h.update(contenu) ##puis on effectue le type de hachage choisit sur notre mdp
        return h.hexdigest() + ':' + salt #Le contenu haché est finalement renvoyé avec le sel utilisé pour le hahsher

    @staticmethod
    def check_mdp(mdp):
        SpecialSym = ['$', '@', '#', '%']
        val = True

        if len(mdp) < 6:
            print('\nLa longueur du mot de passe doit être au moins de 6 caractères\n')
            val = False

        if len(mdp) > 20:
            print('\nLa longueur du mot de passe ne doit pas dépasser 20 caractères\n')
            val = False

        if not any(char.isdigit() for char in mdp):
            print('\nLe mot de passe doit contenir au moins un chiffre\n')
            val = False

        if not any(char.isupper() for char in mdp):
            print('\nLe mot de passe doit contenir au moins une majuscule\n')
            val = False

        if not any(char.islower() for char in mdp):
            print('\nLe mdp doit contenir au moins une minuscule\n')
            val = False

        if not any(char in SpecialSym for char in mdp):
            print('\nLe mot de passe doit contenir un de ces caractères $ @ # % \n')
            val = False
        return val

    @staticmethod
    def check_pseudo(pseudo):
        reponse=True
        if pseudo == '':
            reponse = False
            print("\nVous devez impérativement entrer un pseudo pour vous inscrire\n")
        joueurDAO = JoueurDAO()
        if len(joueurDAO.recuperer_pseudo(pseudo))!= 0:
            print("\nCe pseudo existe déja. Ressaisisez en un autre !\n")
            reponse = False
        return reponse

    def choix_pkm(self):
        pkm = {"Pokémon 1":PokemonAPI().getPokemon(1,1),"Pokémon 2": PokemonAPI().getPokemon(4,1),"Pokémon 3" : PokemonAPI().getPokemon(7,1)}
        pokedex = Pokedex(pkm=pkm)
        print("\n")
        pokedex.afficher_pokedex()

        question = [
            {"type": "list", "name": "choix_pkm", "message": "Avant de commencer le jeu, vous devez choisir le pokémon qui vous accompagnera pour le début de votre aventure !",
             "choices": ["Bulbizarre", Separator(), "Salamèche", Separator(), "Carapuce"]}]
        response = prompt(question)
        if response['choix_pkm'] == "Bulbizarre":
            return pkm["Pokémon 1"]
        elif response['choix_pkm'] == "Salamèche":
            pkm["Pokémon 2"].niveau = 1
            return pkm["Pokémon 2"]
        else:
            return pkm["Pokémon 3"]
















