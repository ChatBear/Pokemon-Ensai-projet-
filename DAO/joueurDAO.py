from DAO.pool_connexion import PoolConnection
import psycopg2


class JoueurDAO():

    @staticmethod
    def recuperer_pseudo(pseudo):
        """permet de savoir si un pseudo est dans la base"""
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            requete_sql = """SELECT * FROM Joueur WHERE pseudo = '{}' ;""".format(pseudo)
            curseur.execute(requete_sql)
            result = curseur.fetchall()
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
            return result

    @staticmethod
    def recuperer(pseudo, password):
        """permet de récuperer un joueur dans la base données lors de la connexion
        s'il n'y a pas de joueur alors la fonction retourne None sinon elle renvoie un objet de la classe joueur"""
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            requete_sql1 = """SELECT pseudo, mdp_hash, progression FROM Joueur WHERE pseudo = '{}' AND mdp_hash = '{}';""".format(pseudo, password)
            curseur.execute(requete_sql1)
            player = curseur.fetchall()
            if player == None :
                joueur = None
            else:
                requete_sql2 = """SELECT id_pokemon FROM pokemon WHERE (id_pokedex = '{}' AND actif = true);""".format(pseudo)
                curseur.execute(requete_sql2)
                pok = curseur.fetchall()
                from DAO.pokemonDAO import PokemonDAO
                pokemonDAO = PokemonDAO()
                pokemon = pokemonDAO.recuperer(pok[0][0])
                from Metier.joueur import Joueur
                joueur = Joueur(nom=player[0][0], password= player[0][1], pokemon=pokemon, etat=True, progression= player[0][2])# du code
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return joueur

    @staticmethod
    def creer(pseudo, password):
        """permet de créer un joueur dans la base de données lors de l'inscription"""
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            requete_sql = """INSERT INTO joueur VALUES ('{}', '{}', false, 0, 60, 5, 0, 0);""".format(pseudo, password)
            curseur.execute(requete_sql)
            connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)


    def update(self, nom, etat):
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            requete_sql = """UPDATE Joueur SET etat = {} WHERE pseudo = '{}';""".format(etat, nom)
            curseur.execute(requete_sql)  # du code
            connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)

#user = JoueurDAO().recuperer_pseudo("Shiraz")
#print(user)
#joueur = JoueurDAO().recuperer(user[0][0], user[0][1])
#print(joueur.nom)
#print(joueur.etat)
#print(joueur.progression)
