import unittest
#from unittest import TestCase
#from pokemon.Metier.dresseur import Dresseur
from Metier.dresseur import Dresseur
#from dresseur import Dresseur

class Test_Dresseur(unittest.TestCase):

    def test_verser_gain(self):
        # When
        expected_output = "Vous avez remporté 10 €"
        # Then
        actual_output = Dresseur().verser_gain(10)
        self.assertEqual(expected_output, actual_output)


