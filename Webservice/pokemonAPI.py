import json
#from Metier.Pokedex import Pokedex
import requests
import numpy as np
from Metier.Pokemon import Pokemon
from Metier.Statistique import Statistique
from Metier.Type import Type
from Metier.Attaques import Attaques


class PokemonAPI():

    def getPokemon(self, num,lvl = 1):
        #On récupère le nom du pokemon en anglais pour ensuite récupèrer les autres informations
        r=requests.get("https://pokeapi.co/api/v2/pokemon-species/" + str(num))
        X = r.text
        Y2 = json.loads(X)
        noun = Y2["name"]
        prenom = Y2["names"][4]["name"]

        #On requête l'API avec le nom du pokemon en anglais
        r2 = requests.get("https://pokeapi.co/api/v2/pokemon/" + noun)


        #On vérifie que la récupération c'est bien passé
        if r2.status_code!=200:
            return "Le nom du pokémon est invalide"


        #On récupère les données sous forme d'un dictionnaire
        X2=r2.text
        Y=json.loads(X2)


        #Je récupère les statistique du pokemon, uniquement les pv, attaque, défense et vitesse.
        stat = Statistique(Y["stats"][0]["base_stat"], Y["stats"][1]["base_stat"], Y["stats"][2]["base_stat"], Y["stats"][5]["base_stat"])

        #On cherche à savoir le pokemon possède 1 ou 2 types
        if len(Y["types"])==2:
            typ = [Type(Y["types"][0]["type"]["name"]),Type(Y["types"][1]["type"]["name"])]
        else:
            typ = [Type(Y["types"][0]["type"]["name"])]

        #Je vais générer une liste de 4 nombre compris entre 1 et le nombre d'attaques que le pokemon possède. Ensuite je vais vérifier que les attaques infligent au moins des dégats,
        # dans un soucis de simplification à l'aide du module numpy, car certaines attaques possèdent des effets spéciaux.
        n = len(Y["moves"])
        attaques = []

        #Géneration de 4 nombres aléatoire
        Att=np.random.randint(0,n,4)

        #Sous_fonctions
        def doublons(L):
            for i in range(len(L)-1):
                if L[i] in L[i+1:]:
                    return False
            return True


        #Vérification des dommages effectifs des attaques
        for i in range (4):
            state = False
            while (state == False):
                url_att = Y["moves"][Att[i]]["move"]["url"]
                r3 = requests.get(url_att)
                X3 = r3.text
                Y3 = json.loads(X3)
                if Y3["power"] != None and doublons(Att) == True:
                    state = True

                else :
                    Att[i] = np.random.randint(0,n)


        #Récupération des différentes attaques avec l'API
        for i in range (4):
            url_att = Y["moves"][Att[i]]["move"]["url"]
            r4= requests.get(url_att)
            X4 = r4.text
            Y4 = json.loads(X4)
            degats = Y4["power"]
            nom_att = Y4["names"][3]["name"]
            j = 0
            while (Y4["flavor_text_entries"][j]["language"]["name"] != "fr"):
                j+=1
            descr = Y4["flavor_text_entries"][j]["flavor_text"]
            typ0 = Y4["type"]["name"]
            typ1 = Type(typ0)
            attaques.append(Attaques(nom=nom_att,description= descr, type=typ1, degats=degats))


        #Ici je récupère l'expérience que vaut le pokemon
        Exp = Y["base_experience"]
        pokemon=Pokemon(nom=prenom, stat=stat, niveau=lvl, experience=Exp ,types=typ,attaques=attaques)
        return pokemon



################ TEST

"""Z = PokemonAPI().getPokemon(365)
print(Z.nom,Z.experience,Z.types[0].nom)"""


