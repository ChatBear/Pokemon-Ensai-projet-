from Metier.Pokemon import Pokemon
class Statistique():
	def __init__(self, pv, attaque, defense, vitesse):
		self.pv=pv
		self.attaque=attaque
		self.defense=defense
		self.vitesse=vitesse

	def afficher(self):
		return(self.pv, self.attaque, self.defense, self.vitesse)


