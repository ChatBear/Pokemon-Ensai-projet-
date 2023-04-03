import requests
import json
from Metier.Pokemon import Pokemon
from Metier.Attaques import Attaques
class Type():
	def __init__(self, nom):
		self.nom = nom

	def gestion_type(self,type2):
		#-1 : si pas efficace si le type 1 n'est pas efficace au type 2
		# 0 : si pas d'effet particulier
		# 1 : si super efficace si le type 1 est efficace par rapport au type 2
		# -100 si le type 1 n'affecte pas le type 2

		#Récupère les informations liées au premier type
		r1 = requests.get("https://pokeapi.co/api/v2/type/" + self.nom)
		X1 = r1.text
		Y1 = json.loads(X1)

		#Vérifie que le type 1 est super efficace contre le type 2
		for i in range (len(Y1["damage_relations"]["double_damage_to"])):
			if Y1["damage_relations"]["double_damage_to"][i]["name"] == type2.nom :
				return 1
		#Vérifie que le type 1 n'est pas efficace contre le type 2
		for i in range (len(Y1["damage_relations"]["half_damage_to"])):
			if Y1["damage_relations"]["half_damage_to"][i]["name"] == type2.nom:
				return -1
		#Vérifie que le type 1 affecte le type 2
		for i in range (len(Y1["damage_relations"]["no_damage_to"])):
			if Y1["damage_relations"]["no_damage_to"][i]["name"] == type2.nom:
				return -100
		#Si le type n'est dans aucune des catégories ci-dessus, alors, le type 2 n'a pas fait d'effet particulier
		return 0




	def calcul_dmg_type(self,pokemon1,pokemon2,attaque1):
		#Cette méthode va calculer les dégats de l'attaque du pokemon1 au pokemon2 avec l'attaque1 en gérant l'aspect type, donc l'efficacité de l'attaque
		#Je définis les différents types en prenant en compte que les pokemons peuvent avoir 2 types
		if len(pokemon1.types) == 2:
			Type11 = pokemon1.types[0]
			Type12 = pokemon1.types[1]
		else:
			Type11 = pokemon1.types[0]
			Type12 = None
		if len(pokemon2.types) == 2:
			Type21 = pokemon2.types[0]
			Type22 = pokemon2.types[1]
		else :
			Type21 = pokemon2.types[0]
			Type22 = None
		Type3 = attaque1.type
		degat = attaque1.degats

		#Je vérifie que l'attaque du pokemon1 et de l'attaque1 ont le même type (cela augmente les dégats)
		Stab = 0
		if Type11 == Type3 or Type12 == Type3:
			Stab = 15
		i = Type3.gestion_type(Type21)
		if Type22 != None:
			j = Type3.gestion_type(Type22)
		else:
			j = 0

		if i == -100 or j== -100:
			print("Cette attaque n'affecte pas le pokémon")
			return 0
		if i == 0:
			if j == 0:
				degat_finaux = degat + Stab + pokemon1.niveau
			if j == -1:
				degat_finaux = 0.5*degat + Stab + pokemon1.niveau
				print("Ce n'est pas très efficace ")
			if j == 1:
				degat_finaux = 1.5*degat + Stab + pokemon1.niveau
				print("C'est super efficace ")
		if i == -1 :
			if j == 0:
				degat_finaux = 0.5*degat + Stab + pokemon1.niveau
				print("Ce n'est pas très efficace")
			if j == -1:
				degat_finaux = 0.25*degat + Stab + pokemon1.niveau
				print("Ce n'est pas très efficace")
			if j == 1 :
				degat_finaux = degat + Stab + pokemon1.niveau
		if i == 1:
			if j == 0:
				degat_finaux = 1.5*degat + Stab + pokemon1.niveau
				print("C'est super efficace")
			if j == 1:
				degat_finaux = 2*degat + Stab + pokemon1.niveau
				print("C'est super efficace")
			if j == -1:
				degat_finaux = degat + Stab + pokemon1.niveau
		return degat_finaux

###TEST
