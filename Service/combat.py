from Metier.Pokemon import Pokemon
import numpy as np
from Metier.Statistique import Statistique
from DAO.inventaireDAO import InventaireDAO
from Metier.joueur import Joueur
from Metier.Type import Type
from Metier.Attaques import Attaques


class Combat():
    def __init__(self, pokemon1, pokemon2,joueur,duel = False) :
        from DAO.pokemonDAO import PokemonDAO
        from DAO.pokedexDAO import PokedexDAO

        pokemonDAO = PokemonDAO()
        if duel == True:
            admin = "admin"
            Id2 = pokemonDAO.recup_ID(joueur,pokemon2.nom,admin=admin)
        else:
            Id2 = pokemonDAO.recup_ID(joueur,pokemon2.nom)
        Id1 = pokemonDAO.recup_ID(joueur, pokemon1.nom)

        self.pokemon1 = pokemonDAO.recuperer(Id1)
        lvl = pokemon2.niveau
        for i in range (1,lvl+1):

            pokemonDAO.update_pkm_stat(i,id_pkm=Id2)
            pokemonDAO.update_niveau(i,id=Id2)
        self.pokemon2 = pokemonDAO.recuperer(Id2)


        self.id1 = Id1
        self.id2 = Id2



    def attaquer(self, joueur, duel):
        #Cette Méthode est un seul tour d'attaque
        pv1 = self.pokemon1.stat.pv
        pv2 = self.pokemon2.stat.pv

        if self.pokemon1.stat.vitesse > self.pokemon2.stat.vitesse:
            attaque1 = self.pokemon1.use_attaque()
            Tip = Type('grass')
            print(self.pokemon1.nom + " a " + str(pv1) + "PV")
            print('\n')
            print(self.pokemon2.nom + " a " + str(pv2) + "PV")
            print('\n')
            print(self.pokemon1.nom + " utilise " + attaque1.nom)
            degats_finaux = Tip.calcul_dmg_type(self.pokemon1,self.pokemon2,attaque1)
            print('\n')
            print(self.pokemon1.nom + " inflige " + str(degats_finaux))
            pv2 -= degats_finaux
            if pv2 <= 0 :
                print('\n')
                print(self.pokemon1.nom + " gagne le combat")
                lvl = self.pokemon1.niveau
                self.pokemon1.gain_exp(self.pokemon2.experience)


                while lvl < self.pokemon1.niveau:
                    lvl += 1
                    print("Félicitations, vous êtes passé au niveau "+str(lvl))
                    from DAO.pokemonDAO import PokemonDAO
                    Pkm = PokemonDAO()


                    Pkm.update_pkm_stat(lvl, id_pkm=self.id1)



                from DAO.pokemonDAO import PokemonDAO
                PokemonDAO().update_experience(self.pokemon2.experience,self.id1,self.pokemon1.niveau)

                if duel == True:
                    return True,True
                return True
            i = np.random.randint(0, 4)
            attaques2 = self.pokemon2.attaques[i]
            print('\n')
            print(self.pokemon2.nom + " utilise " + attaques2.nom)
            Tip = Type('grass')
            degats_finaux = Tip.calcul_dmg_type(self.pokemon2, self.pokemon1, attaques2)
            pv1 -= degats_finaux
            print('\n')
            print(self.pokemon2.nom + " inflige " + str(degats_finaux))
            if pv1 <= 0:
                print('\n')
                print(self.pokemon2.nom + "gagne le combat")

                if duel == True:
                    return True,False
                return True

        else:
            print(self.pokemon1.nom + " a " + str(pv1) + "PV")
            print('\n')
            print(self.pokemon2.nom + " a " + str(pv2) + "PV")
            print('\n')
            i = np.random.randint(0,4)
            attaques2 = self.pokemon2.attaques[i]
            Tip = Type('grass')
            print(self.pokemon2.nom + " utilise " + attaques2.nom)
            degats_finaux = Tip.calcul_dmg_type(self.pokemon2,self.pokemon1,attaques2)
            print('\n')
            print(self.pokemon2.nom + " inflige " + str(degats_finaux))
            pv1 -= degats_finaux
            if pv1 <= 0 :
                print('\n')
                print(self.pokemon2.nom + " gagne le combat ")
                if duel == True:
                    return True,False
                return True
            attaque1 = self.pokemon1.use_attaque()
            Tip = Type('grass')
            degats_finaux = Tip.calcul_dmg_type(self.pokemon1,self.pokemon2,attaque1)
            print('\n')
            print(self.pokemon1.nom + " utilise " + attaque1.nom)
            print('\n')
            print(self.pokemon1.nom + " inflige " + str(degats_finaux))
            pv2 -= degats_finaux
            if pv2 <= 0:
                print('\n')
                print(self.pokemon1.nom + " gagne le combat")
                lvl = self.pokemon1.niveau
                self.pokemon1.gain_exp(self.pokemon2.experience)
                while lvl < self.pokemon1.niveau:
                    lvl +=1

                    from DAO.pokemonDAO import PokemonDAO
                    Pkm = PokemonDAO()

                    Pkm.update_niveau(lvl, self.pokemon1.nom)
                    Pkm.update_pkm_stat(lvl,nompkm= self.pokemon1.nom)

                from DAO.pokemonDAO import PokemonDAO
                pokemonDAO = PokemonDAO()
                self.pokemon1 = pokemonDAO.update_experience(self.pokemon1.nom, self.pokemon2.experience)

                if duel == True:
                    return True,True
                return True
        print('\n')
        print(self.pokemon1.nom + " a " + str(pv1) + "point de vie")
        print('\n')
        print(self.pokemon2.nom + " a " + str(pv2) + "point de vie")
        self.pokemon1.stat.pv = pv1
        self.pokemon2.stat.pv = pv2
        return False



    def attraper(self, joueur, pokeball):
        #Pv_actuel représente les pv du pokemon pendant le combat, je prends un autre argument que pokemon1.stat.pv car je ne souhaite pas modifier cette argument, parce qu'il change l'objet en lui
        #et cela ne me plaît pas trop
        from DAO.inventaireDAO import InventaireDAO
        inventaireDAO = InventaireDAO()
        inventaire = inventaireDAO.recuperer(joueur)
        if inventaire.nb_pokeball[pokeball]<1:
            print("\nVous n'avez plus de ce type de Pokéball dans votre stock")
            return False
        else :
            inventaire.nb_pokeball[pokeball]-=1
            inventaireDAO.update_pokeball(inventaire.nb_pokeball["Pokéball"], inventaire.nb_pokeball["Superball"], inventaire.nb_pokeball["Hyperball"], joueur)
            if pokeball == "Pokéball":
                taux = 0.4
            if pokeball == "Superball":
                taux = 0.6
            if pokeball == "Hyperball":
                taux = 0.8
            seuil_theorique = np.random.uniform(0,1) #Seuil à partir duquel on considère que le pokemon est capturé
            if taux >= seuil_theorique:
                print("\nFélicitations, vous avez attrapé le pokémon " + self.pokemon2.nom)
                from DAO.pokemonDAO import PokemonDAO
                pokemonDAO = PokemonDAO()
                pokemonDAO.update_attraper(self.id2)##########
                return True
            #else:
            print("\nVous n'avez pas réussi à attraper le pokémon")
            return False



    def fuire(self, joueur):
        #J'explique le fonctionnement de la fuite parce que j'ai l'impression que vous n'aviez pas compris. Pouvoir fuire un pokémonn n'est pas donnée
        # C'est aléatoire dépendant du niveau des deux pokemons.
        lvl1 = self.pokemon1.niveau
        lvl2 = self.pokemon2.niveau
        if lvl1>lvl2 - np.random.uniform(0,5):
            print("\nVous avez réussi à prendre la fuite !")
            from DAO.pokedexDAO import PokedexDAO
            pokedexDAO = PokedexDAO()
            pokedexDAO.remplir(joueur, self.pokemon2, False)
            return True
        else :
            print("\nVous n'avez pas pu fuire")
            return False



