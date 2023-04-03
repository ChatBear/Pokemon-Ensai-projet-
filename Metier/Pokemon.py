from Metier.Attaques import Attaques
#from pokemon.Metier.Attaques import Attaques

class Pokemon:
	def __init__(self, nom, stat, niveau,  experience, experience_accumule =0, types = None, attaques = None, sprite=None, barre_exp=0,exp_completer = 0):
		self.nom = nom
		self.stat = stat
		self.niveau = niveau
		self.experience = experience
		self.experience_accumule = experience_accumule
		self.types = types
		self.attaques = attaques
		self.sprite = sprite
		self.barre_exp = barre_exp
		self.exp_completer = exp_completer

	def affiche_photo(self):
		pass

	def use_attaque(self):
		print("Attaque 1 : " + self.attaques[0].nom + "\n" +
		      "Attaque 2 : " + self.attaques[1].nom + "\n" +
	        "Attaque 3 : " + self.attaques[2].nom + "\n" +
		"Attaque 4 : " + self.attaques[3].nom + "\n" )
		i = int(input("Veuillez choisir une attaque en donnant une chiffre "))
		return self.attaques[i-1]

	def gain_exp(self,exp):
		self.experience_accumule += exp
		self.barre_exp += exp
		while self.barre_exp > self.exp_completer:

			self.niveau += 1
			self.barre_exp = self.barre_exp - self.exp_completer
			self.exp_completer = self.experience + self.niveau
		self.update_stat(False)




	def update_stat(self,state = True):
		lvl = self.niveau
		self.stat.pv = self.stat.pv + 0.2*lvl
		self.stat.attaque = self.stat.attaque + lvl
		self.stat.defense = self.stat.defense + lvl
		self.stat.vitesse = self.stat.vitesse + lvl
		if state == True:
			self.experience_accumule = lvl*self.experience + (lvl-1)*(lvl-2)/2
			self.exp_completer = self.experience + lvl




#### Je mets ici parce que je ne sais pas où l'écrire. J'explique brièvement comment j'ai pensé à faire pour l'expérience des
# pokemon. En gros pour passer du niveau k à k+1 il faut : 50 +10^k point d'expérience.


