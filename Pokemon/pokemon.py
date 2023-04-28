import random

class Pokemon:
    def __init__(self, nom, type, vie=100, niveau=1, attaque=10, defense=0):
        self.nom = nom
        self.type = type
        self.vie = vie
        self.niveau = niveau
        self.attaque = attaque
        self.defense = defense

    def attaquer(self, cible):
        degats = self.attaque - cible.defense
        if degats < 0:
            degats = 0
        cible.vie -= degats
        print(f"{self.nom} attaque {cible.nom} et lui inflige {degats} points de dégâts.")
        if cible.vie <= 0:
            print(f"{cible.nom} est KO ! {self.nom} remporte le combat !")

    def soigner(self, points):
        self.vie += points
        if self.vie > 100:
            self.vie = 100
        print(f"{self.nom} récupère {points} points de vie.")

    def afficher_info(self):
        print(f"{self.nom} ({self.type}) - Niveau {self.niveau}")
        print(f"Points de vie : {self.vie}")
        print(f"Attaque : {self.attaque}")
        print(f"Défense : {self.defense}")
        print("")

def combat(pokemon1, pokemon2):
    print(f"Un combat oppose {pokemon1.nom} ({pokemon1.vie} PV) et {pokemon2.nom} ({pokemon2.vie} PV) !")

    while pokemon1.vie > 0 and pokemon2.vie > 0:
        # Tour de pokemon1
        pokemon1.attaquer(pokemon2)
        if pokemon2.vie <= 0:
            break

        # Tour de pokemon2
        pokemon2.attaquer(pokemon1)

    print("Fin du combat.")

# Création de 4 Pokémon
pikachu = Pokemon("Pikachu", "électrique", vie=80, niveau=2, attaque=15, defense=5)
salameche = Pokemon("Salameche", "feu", niveau=1, attaque=12)
carapuce = Pokemon("Carapuce", "eau", vie=120, niveau=3, attaque=10, defense=10)
bulbizarre = Pokemon("Bulbizarre", "plante", vie=110, niveau=4, attaque=8, defense=12)

# Affichage des informations d'un Pokémon
pikachu.afficher_info()

# Soigner un Pokémon
pikachu.soigner(20)

# Combat entre deux Pokémon au hasard
pokemon1 = random.choice([pikachu, salameche, carapuce, bulbizarre])
pokemon2 = random.choice([pikachu, salameche, carapuce, bulbizarre])
combat(pokemon1, pokemon2)