CREATE TABLE Statistiques(
id_stat SERIAL PRIMARY KEY,
id_pokemon INT,
attaque INT,
Defense INT,
Vitesse INT,
PV INT
);

CREATE TABLE Types(
id_Type SERIAL PRIMARY KEY,
id_pokemon INT,
id_attaque INT,
type VARCHAR(40)
);

CREATE TABLE Attaques(
id_attaque SERIAL PRIMARY KEY,
id_pokemon INT,
nom VARCHAR(200),
description VARCHAR(300),
degat INT
);

CREATE TABLE Joueur(
pseudo VARCHAR(40),
mdp_hash VARCHAR(500),
etat BOOLEAN,
progression INT,
argent INT,
nb_pokeball INT,
nb_superball INT,
nb_hyperball INT,
CONSTRAINT pk_pseudo PRIMARY KEY(pseudo)
);

CREATE TABLE Dresseur(
id_dresseur VARCHAR(40),
Phrase VARCHAR(150),
Gain INT,
Niveau INT,
Statut BOOLEAN,
id_pokemon INT,
CONSTRAINT pk_id_dresseur PRIMARY KEY (id_dresseur)
);

INSERT INTO Dresseur VALUES ('dresseur1','Bonjour, je suis le premier dresseur. Je te souhaite bon courage',15,15,False,1),
('dresseur2','Bonjour, je suis le deuxièeme dresseur encore plus fort que le deuxième.',25,25,False,2),
('dresseur3','Bonjour je suis le troisième dresseur. Bravo pour ton parcours',35,35,False,3),
('dresseur4','Bonjour, tu as battu le troisième, bien. Maintenant tu vas perdre',45,45,False,4),
('dresseur5','Salut, vermine.',55,55,False,5),
('dresseur6','Yo, je suis le 6ème dresseur, malheuresment ca sera ton dernier combat',65,65,False,6),
('dresseur7','Salut tu commences a affronter des vrais dresseur, bon courage',75,75,false,7),
('dresseur8','Yoyo',85,85,false,8),
('dresseur9','Bienvenu dans le dernier combat, tu es presque le maître, il te reste plus grand chose, il sera le plus difficile. Bon courage',100,100,False,9);


CREATE TABLE Pokemon(
id_pokemon SERIAL PRIMARY KEY,
nom_pkm VARCHAR(40),
niveau INT,
experience INT,
Experience_accumule INT,
Sprite VARCHAR(40),
capture BOOLEAN,
actif BOOLEAN,
id_pokedex VARCHAR(40)
);
