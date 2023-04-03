from DAO.pool_connexion import PoolConnection
from Metier.Pokemon import Pokemon
import psycopg2

class InventaireDAO():

    def recuperer(self, joueur):
        """permet de créer une instance de la classe Inventaire pour le joueur"""
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            requete_sql1 = """SELECT argent, nb_pokeball, nb_superball, nb_hyperball FROM Joueur WHERE pseudo='{}';""".format(joueur.nom)
            curseur.execute(requete_sql1)
            info = curseur.fetchall()
            requete_sql2 = """SELECT id_pokemon FROM Pokemon WHERE id_pokedex = '{}' AND capture = true;""".format(joueur.nom)
            curseur.execute(requete_sql2)
            rows=curseur.fetchall()
            dict1={}
            from DAO.pokemonDAO import PokemonDAO
            pok=PokemonDAO()
            for i in range(len(rows)):
                key = "Pokémon "+str(i+1)
                dict1[key]=pok.recuperer(id_pkm=rows[i][0])
            from DAO.pokedexDAO import PokedexDAO
            pkdexDAO=PokedexDAO()
            dict2 = pkdexDAO.recuperer(joueur)
            dict3 = {"Pokéball":info[0][1], "Superball": info[0][2], "Hyperball":info[0][3]}
            from Metier.Pokedex import Pokedex
            from Service.inventaire import Inventaire
            inventaire=Inventaire(info[0][0], dict3, Pokedex(dict=dict1), Pokedex(dict=dict2))
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return inventaire


    def update_pokeball(self,pokeball, superball, hyperball, joueur):
        #P pour pokeball
        #S pour Superball
        #H pour Hyperball
        #PS pour pseudo

        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute("UPDATE joueur  SET nb_pokeball = {},nb_superball = {},nb_hyperball = {} WHERE pseudo = '{}';".format(pokeball, superball, hyperball, joueur.nom))
            connexion.commit()
        except psycopg2.Error as error:
            AbstractDao.connection.rollback()
            raise error
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)

    def update_argent(self,argent,joueur):
        #PS pour pseudo et ar pour argent

        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute("UPDATE Joueur SET argent = {} WHERE pseudo = '{}';".format(argent, joueur.nom))
            connexion.commit()
        except psycopg2.Error as error:
            PoolConnection.connection.rollback()
            raise error
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)

    def update_pkm_actif(self,nom, joueur):
        connexion = PoolConnection.getConnexion()
        curseur  = connexion.cursor()
        try:
            #Je récupère le nom du pokémon actif
            curseur.execute("SELECT id_pokemon FROM Pokemon WHERE actif = True AND id_pokedex = '{}';".format(joueur.nom))
            result = curseur.fetchall()
            curseur.execute("UPDATE Pokemon SET actif = False WHERE id_pokemon = {};".format(result[0][0]))
            #Je change le pokemon actif et et je le remplace par celui donné en argument dans la méthode
            curseur.execute("SELECT id_pokemon FROM Pokemon WHERE nom_pkm = '{}' AND id_pokedex = '{}';".format(nom,joueur.nom))
            result = curseur.fetchall()
            curseur.execute("UPDATE Pokemon SET actif = True WHERE id_pokemon = {};".format(result[0][0]))
            connexion.commit()
        except psycopg2.Error as error:
            connection.rollback()
            raise error
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return result[0][0]


"""from DAO.joueurDAO import JoueurDAO
user = JoueurDAO().recuperer_pseudo("Lucie")
print(user)
joueur = JoueurDAO().recuperer(user[0][0], user[0][1])
print(InventaireDAO().recuperer(joueur).afficher_argent())
print(InventaireDAO().recuperer(joueur).afficher_pokeball())
print(InventaireDAO().recuperer(joueur).captures.afficher_pokedex())
print(InventaireDAO().recuperer(joueur).pokedex.afficher_pokedex())"""







