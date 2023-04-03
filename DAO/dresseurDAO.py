from DAO.pool_connexion import PoolConnection
import psycopg2

class DresseurDAO():

    def recuperer(self, joueur):
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()


        try:

            curseur.execute("SELECT * FROM Dresseur WHERE Niveau <= %s;",(joueur.pokemon.niveau,))
            results = curseur.fetchall()


            if results == []:
                print("\nVous n'avez pas le niveau requis pour affronter des dresseurs.\nIl faut posséder au moins un pokémon de niveau 15")
                List = None
            else:
                List = []
                for i in range (len(results)):

                    nom = results[i][0]

                    phrase = results[i][1]
                    gain = results[i][2]
                    niveau = results[i][3]
                    if results[i][4] == False:
                        statut = False
                    else:
                        statut = True
                    id_pokemon = results[i][5]
                    from DAO.pokemonDAO import PokemonDAO
                    pokemonDAO = PokemonDAO()
                    pokemon = pokemonDAO.recuperer(id_pkm=id_pokemon)

                    from Metier.dresseur import Dresseur
                    dresseur = Dresseur(nom,pokemon,phrase,gain,statut,niveau)
                    List.append(dresseur)


        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return List

    def update(self, dresseur):
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        requete_sql = """UPDATE Dresseur SET Statut = True WHERE id_dresseur = '{}';""".format(dresseur.nom)
        try:
            curseur.execute(requete_sql)  #
            connexion.commit()
            ras = True
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return ras

##TEST
