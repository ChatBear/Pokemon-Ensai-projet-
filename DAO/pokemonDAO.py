from DAO.pool_connexion import PoolConnection
from Metier.Statistique import Statistique
import psycopg2

class PokemonDAO():
    def recuperer_stat(self,id_pkm):
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute("SELECT attaque, defense, vitesse, pv FROM Statistiques WHERE id_pokemon = '{}';".format(id_pkm))
            result = curseur.fetchall()
            stati = Statistique(result[0][3], result[0][0], result[0][1], result[0][2])
        except:
            stati = None
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
            return stati
    def recup_ID(self,joueur,nompkm = None,admin = None):
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()

        try:
            if admin != None:

                curseur.execute("SELECT id_pokemon FROM Pokemon WHERE nom_pkm = '{}' AND id_pokedex = '{}';".format(nompkm,admin))

            if nompkm == None:
                curseur.execute("SELECT id_pokemon FROM Pokemon ORDER BY id_pokemon DESC LIMIT 1")
            if admin == None:
                curseur.execute("SELECT id_pokemon FROM Pokemon WHERE nom_pkm = '{}' AND id_pokedex = '{}';".format(nompkm,joueur.nom))
            Id = curseur.fetchone()

        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return Id[0]

    def recuperer_lvl_pkm(self,id_pkm):
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute("SELECT niveau FROM Pokemon WHERE id_pokemon = '{}';").format(id_pkm)
            result = curseur.fetchone()
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
            return result


    def recupere_nom_pkm(self, id_pkm):
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        result = None
        try:
            curseur.execute("SELECT nom_pkm FROM Pokemon WHERE id_pokemon = %s;", (id_pkm,))
            result = curseur.fetchone()
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
            return result
    def Supprimer_pkm(self,id):
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:

            curseur.execute("DELETE FROM Pokemon WHERE id_pokemon = " + str(id) +";")
            curseur.execute("DELETE FROM Statistiques WHERE id_pokemon = " + str(id)+";")
            curseur.execute("DELETE FROM Types WHERE id_pokemon = " + str(id) + ";")
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close
            PoolConnection.putBackConnexion(connexion)


    def update_experience(self,exp,id,lvl = None):
        #nom désigne le nom du pokemon
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            if lvl != None:
                curseur.execute("SELECT experience FROM pokemon WHERE id_pokemon = '{}';".format(id))
                experience = curseur.fetchone()[0]

                exp_completer = experience + lvl
                curseur.execute("SELECT experience_accumule FROM pokemon WHERE id_pokemon = {};".format(id))
                experience_accumule = curseur.fetchone()[0]

                while experience_accumule > exp_completer:
                    lvl +=1
                    self.update_niveau(lvl,id=id)
                    self.update_pkm_stat(lvl,id_pkm=id)
                    experience_accumule -= exp_completer
                    exp_completer = experience + lvl

                curseur.execute("UPDATE Pokemon SET niveau = {}, experience_accumule = {} WHERE id_pokemon = {};".format(lvl,experience_accumule,id))

            #curseur.execute("UPDATE Pokemon SET experience_accumule = experience_accumule + {} WHERE id_pokemon={};".format(exp,id))
            connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return lvl
    def update_niveau(self,lvl,id):
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:

            curseur.execute("UPDATE Pokemon SET niveau = {} WHERE id_pokemon = '{}';".format(lvl,id))

            connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)


    def update_pkm_stat(self,lvl, id_pkm = None, nompkm = None):
        #nom : pokemon
        #id_pkm désigne l'id du pokemon
        #lvl : le niveau du pokemon
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            if id_pkm != None:
                curseur.execute("UPDATE Statistiques SET attaque = attaque + {}, defense = defense + {}, vitesse = vitesse + {}, PV = PV + 0.25*{}  WHERE id_pokemon = '{}';".format(lvl,lvl,lvl,lvl, id_pkm))
                connexion.commit()
            if id_pkm == None:
                curseur.execute("SELECT id_pokemon FROM Pokemon WHERE nom_pkm = '{}';".format(nompkm))
                id1 = curseur.fetchone()
                id = id1[0]
                curseur.execute("UPDATE Statistiques SET attaque = attaque + {}, defense = defense + {}, vitesse = vitesse + {}, PV = PV + 3*{}  WHERE id_pokemon = '{}';".format(lvl,lvl,lvl,lvl, id))
                connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)

    def update_attraper(self,id):
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute("UPDATE Pokemon SET capture = True WHERE id_pokemon = {};".format(id))
            connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)


    def recuperer(self, id_pkm):
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            requete_sql1= """SELECT nom_pkm, niveau, experience,Experience_accumule FROM Pokemon WHERE id_pokemon = '{}';""".format(id_pkm)
            curseur.execute(requete_sql1)
            result = curseur.fetchall()
            stat = PokemonDAO().recuperer_stat(id_pkm)
            from Metier.Pokemon import Pokemon
            pokemon = Pokemon(nom=result[0][0],stat = stat, niveau =result[0][1], experience=result[0][2], experience_accumule=result[0][3])
            requete_sql2="""SELECT type FROM Types WHERE id_pokemon = '{}';""".format(id_pkm)
            curseur.execute(requete_sql2)
            result = curseur.fetchall()
            from Metier.Type import Type
            type1=Type(result[0][0])
            type2 = Type(result[1][0])
            types= [type1, type2]
            pokemon.types = types
            requete_sql3 = """SELECT id_attaque,nom,description,degat FROM Attaques WHERE id_pokemon  = '{}';""".format(id_pkm)
            curseur.execute(requete_sql3)
            result = curseur.fetchall()
            from Metier.Attaques import Attaques
            attaques = []
            for i in range(4):
                requete_sql4 = """SELECT type FROM Types WHERE id_attaque = '{}';""".format(result[i][0])
                curseur.execute(requete_sql4)
                output = curseur.fetchall()
                type3=Type(output[0][0])
                attaques.append(Attaques(result[i][1],result[i][2], type3, result[i][3]))
            pokemon.attaques = attaques
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return pokemon

##test


