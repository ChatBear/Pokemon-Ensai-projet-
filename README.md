
                                                      ,'\
                        _.----.        ____         ,'  _\   ___    ___     ____
                    _,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
                    \      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
                     \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
                       \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
                        \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
                         \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
                          \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
                           \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
                            \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                                    `'                            '-._|

Par Shiraz Adamaly, Wissem Baba-Moussa, Hamza El Youmni, Moussa Kafando et Lucie Martin.

Réalisé de Septembre à Décembre 2020.

Description 
===========
Ce projet a été réalisé dans le cadre du projet informatique de deuxième année de l'Ensai (Ecole Nationale de la Statistique et de l'Analyse de l'Information). 
Il consiste à coder un jeu pokemon simplifié en langage Python. 
Nous utilisons l’API PokéApi afin d’obtenir les informations sur les pokemons telles que les statistiques et le type.
Nous utilisons  aussi une base de données qui contient l’ensemble des dresseurs que le joueur affrontera, l’ensemble des pokemons du joueur et enfin le pokedex.
Le joueur aura le choix entre aller attraper ou s’entrainer contre des pokemons sauvages, affronter des dresseurs, acheter des pokéballs ou changer son pokemon actif.
De plus nous avons simplifié la gestion des statistiques, des dégats des attaques tout en essayant de coller le plus proche possible au jeu original. 
Les faiblesses des pokemons, liées à leurs types (herbes, feu etc), sont gérées par notre application.

Mode de jeu
---
Le jeu se joue sur un terminal. 
Vous pourrez interragir avec l'interface en utilisant les flèches de votre clavier ou en écrivant directement dans le terminal selon les actions proposées.
Pour valider une réponse, vous devez appuyer sur la touche Enter de votre clavier.


Le contenu du code
----
Vous trouverez à la racine de ce projet le document d'analyse qui a servi à sa construction et un fichier main qui est un exécutable permettant le lancement de l’application. 

Au même niveau, on retrouve des modules correspondant aux différentes couches de notre programme. 
Ces dossiers seront eux-mêmes décomposés en fichiers, un pour chaque classe du même nom. 
Nous avons donc les dossiers :
* Contrôleur : permet l’interaction entre le joueur et l’application
* Service : partie du code qui manipule les objets métiers pour créer de l’information et lancer les fonctionnalités de notre application
* Métier : objets du code propres à notre application
* DAO : partie du code qui gère la communication avec notre base de données
* Webservice : partie du code qui gère la communication avec l’API 

A ces dossiers, s’ajoutera un dossier Installation qui regroupera les informations et requêtes pour créer notre base de données et un dossier Assets avec les fichiers qui servent à rendre le design des sorties consoles un peu plus ludique.
Sauf exception, les assets ne sont pas de notre création et sont issus de sources internet d'ASCII Art.

Dans le cadre de l'évaluation, la classe Dresseur, présente dans la couche Métier, a été commentée de manière plus complète et est associée à une classe de tests unittaire Test_Dresseur (Elle aussi présente dans la couche Métier).

Installation du jeu
---
Pour que le jeu fonctionne sur votre ordinateur, vous devez suivre les instructions suivantes :
1. Assurez vous d'avoir accès à un serveur en ligne ou local de base de données et une connection Internet
2. Dans le dossier Installation de l'application, recuperer le code du fichier _init_db.sql_ afin de le lancer dans votre serveur de base de données
3. Mettez à jour le fichier _serveur.json_ avec les informations de votre serveur de base de données
4. Lancer le fichier _admin.py_. Celui-ci permet de remplir automatiquement la base de données avec les informations de départ.
5. Vous pouvez maintenant lancer le fichier _main.py_ pour démarrer le jeu. 

Pour profiter d'une meilleure expérience de jeu, nous vous conseillons de vous placer dans un invité de commande lors lancement de l'application.
Utilisez la commande "cd 'chemin_application' python -m main.py".

PS : Attention, des problèmes d'import peuvent subvenir.
L'application utilise des modules python spécifiques qui peuvent ne pas être installés par défaut sur votre machine. 
Si cela vous arrive, utiliser la commande pip install dans un terminal ou une console python.


*__Nous vous remercions d'utiliser notre application et vous souhaitons une bonne expérience de jeu !!!__*

                                                         `;,;.;,;.;.'
                                                          ..:;:;::;:
                                                    ..--''' '' ' ' '''--.
                                                  /' .   .'        '.   .`\
                                                 | /    /            \   '.|
                                                 | |   :             :    :|
                                               .'| |   :             :    :|
                                             ,: /\ \.._\ __..===..__/_../ /`.
                                            |'' |  :.|  `'          `'  |.'  ::.
                                            |   |  ''|    :'';          | ,  `''\
                                            |.:  \/  | /'-.`'   ':'.-'\ |  \,   |
                                            | '  /  /  | / |...   | \ |  |  |';'|
                                             \ _ |:.|  |_\_|`.'   |_/_|  |.:| _ |
                                            /,.,.|' \__       . .      __/ '|.,.,\
                                                 | ':`.`----._____.---'.'   |
                                                  \   `:"""-------'""' |   |
                                                   ',-,-',             .'-=,=,