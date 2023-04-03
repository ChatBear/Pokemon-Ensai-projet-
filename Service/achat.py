from DAO.inventaireDAO import InventaireDAO
import pandas as pd
import numpy as np

inventaireDAO = InventaireDAO()

class Achat():

    def __init__(self, joueur):

        self.inventaire = inventaireDAO.recuperer(joueur)

    def afficher_inv(self):
        self.inventaire.afficher_argent()
        self.inventaire.afficher_pokeball()
        index = ["Prix à l'unité"]
        columns = ["Pokéball(s)", "Superball(s)", "Hyperball(s)"]
        liste = [["1 €", "3 €", "6 €"]]
        df = pd.DataFrame(liste, index=index, columns=columns)
        print("\nLes différents types de pokéballs sont vendus aux prix suivant :\n", df, "\n")

    # Modification de cette Methode
    def acheter(self, type, quantite, joueur):
        quantite = int(quantite)
        prix_pokeball =1
        prix_superball=3
        prix_hyperball=6
        if type=="pokeball":
            if prix_pokeball*quantite <=self.inventaire.argent:
                self.inventaire.argent=self.inventaire.argent-(prix_pokeball*quantite)
                self.inventaire.nb_pokeball["Pokeball"] += quantite
                print("\nVous avez acheté {} pokéball(s)".format(quantite))
            else:
                print("\nVous n'avez pas assez d'argent pour effectuer cet achat!")
        if type == "superball":
            if prix_superball*quantite <=self.inventaire.argent:
                self.inventaire.argent = self.inventaire.argent - (prix_superball * quantite)
                self.inventaire.nb_pokeball["Superball"] += quantite
                print("\nVous avez acheté {} superball(s)".format(quantite))
            else:
                print("\nVous n'avez pas assez d'argent pour effectuer cet achat!")
        if type == "hyperball":
            if prix_hyperball*quantite <=self.inventaire.argent:
                self.inventaire.argent= self.inventaire.argent - (prix_hyperball * quantite)
                self.inventaire.nb_pokeball["Hyperball"] += quantite
                print("\nVous avez acheté {} hyperball(s)".format(quantite))
            else:
                print("\nVous n'avez pas assez d'argent pour effectuer cet achat!")
        inventaireDAO.update_argent(self.inventaire.argent, joueur)
        inventaireDAO.update_pokeball(self.inventaire.nb_pokeball["Pokéball"], self.inventaire.nb_pokeball["Superball"], self.inventaire.nb_pokeball["Hyperball"], joueur)