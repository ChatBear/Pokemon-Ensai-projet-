from Webservice.pokemonAPI import PokemonAPI
from Metier.joueur import Joueur
from DAO.pokedexDAO import PokedexDAO

admin=Joueur("admin", "admin", None)
print(admin.nom)

pokemonAPI = PokemonAPI()
pkm1 = pokemonAPI.getPokemon(299, 15)
print(pkm1.nom)
pkm2 = pokemonAPI.getPokemon(67, 25)
print(pkm2.nom)
pkm3 = pokemonAPI.getPokemon(82, 35)
print(pkm3.nom)
pkm4= pokemonAPI.getPokemon(324, 45)
print(pkm4.nom)
pkm5= pokemonAPI.getPokemon(289, 55)
print(pkm5.nom)
pkm6= pokemonAPI.getPokemon(277, 65)
print(pkm6.nom)
pkm7 = pokemonAPI.getPokemon(196, 75)
print(pkm7.nom)
pkm8 = pokemonAPI.getPokemon(197, 85)
print(pkm8.nom)
pkm9 = pokemonAPI.getPokemon(249, 100)
print(pkm9.nom)

pokemons = [pkm1, pkm2, pkm3, pkm4, pkm5, pkm6, pkm7, pkm8, pkm9]


pokedexDAO=PokedexDAO()
i=1
for pkm in pokemons:
    pokedexDAO.remplir(admin, pkm, False)
    print(i)
    i+=1