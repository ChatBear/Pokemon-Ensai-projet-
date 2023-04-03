from DAO.pool_connexion import PoolConnection
import psycopg2

class PokedexDAO():

	def recuperer(self, joueur):
		"""créer une instance de la classe Pokedex dans le jeu pour après afficher"""
		connexion = PoolConnection.getConnexion()
		curseur = connexion.cursor()
		try:
			requete_sql = """SELECT id_pokemon FROM Pokemon WHERE id_pokedex = '{}';""".format(joueur.nom)
			curseur.execute(requete_sql)
			rows = curseur.fetchall()
			dict = {}
			from DAO.pokemonDAO import PokemonDAO
			pokemonDAO=PokemonDAO()
			for i in range(len(rows)):
				key = "Pokémon "+str(i+1)
				dict[key] = pokemonDAO.recuperer(rows[i][0])
		finally:
			curseur.close()
			PoolConnection.putBackConnexion(connexion)
		return dict


	def remplir(self,joueur, pokemon, capture, actif = False):
		"""Permet d'ajouter un pokemon au pokedex
		capture permet de renseigner si le pokemon a été capturé oui (True) ou non (False)"""
		connexion = PoolConnection.getConnexion()
		curseur = connexion.cursor()
		try:
			requete_sql1 = """INSERT INTO Pokemon VALUES (DEFAULT,'{}',{}, {}, {}, '{}', {}, {}, '{}');
					SELECT id_pokemon FROM Pokemon ORDER BY id_pokemon DESC LIMIT 1;""".format(pokemon.nom,
																							     pokemon.niveau,
																								 pokemon.experience,
																								 pokemon.experience_accumule,
																								 pokemon.sprite, capture,
																								 actif,
																								 joueur.nom)
			curseur.execute(requete_sql1)
			id_pk = curseur.fetchall()
			requete_sql2 =  """INSERT INTO statistiques VALUES(DEFAULT,'{}', {}, {}, {}, {});
			INSERT INTO types VALUES (DEFAULT,'{}', NULL, '{}'), (DEFAULT, '{}', NULL, '{}');
			""".format(id_pk[0][0], pokemon.stat.attaque, pokemon.stat.defense, pokemon.stat.vitesse, pokemon.stat.pv,
					   id_pk[0][0], pokemon.types[0].nom, id_pk[0][0], pokemon.types[0].nom)
			curseur.execute(requete_sql2)
			for i in range(4):
				if pokemon.attaques[i].degats == None:
					pokemon.attaques[i].degats = 0
				requete_sql3 = """INSERT INTO Attaques VALUES (DEFAULT,'{}', '{}', '{}', {});
								SELECT id_attaque FROM Attaques ORDER BY id_attaque DESC LIMIT 1;
								""".format(id_pk[0][0],pokemon.attaques[i].nom, pokemon.attaques[i].description, pokemon.attaques[i].degats)
				curseur.execute(requete_sql3)
				id_att = curseur.fetchall()
				requete_sql4 = """INSERT INTO types VALUES (DEFAULT,NULL, '{}', '{}');""".format(id_att[0][0], pokemon.attaques[i].type.nom)
				curseur.execute(requete_sql4)
			connexion.commit()
		except psycopg2.Error as error:
			connexion.rollback()
			raise error
		finally:
			curseur.close()
			PoolConnection.putBackConnexion(connexion)

"""from DAO.joueurDAO import JoueurDAO
user = JoueurDAO().recuperer_pseudo("Lucie")
print(user)
joueur = JoueurDAO().recuperer(user[0][0], user[0][1])
print(PokedexDAO().recuperer(joueur))"""