import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = []
        couleurs = ['coeur', 'carreau', 'pique', 'trèfle']
        valeurs = list(range(2, 11)) + ['valet', 'dame', 'roi', 'as']
        for couleur in couleurs:
            for valeur in valeurs:
                self.paquet.append(Carte(valeur, couleur))

    def melanger(self):
        random.shuffle(self.paquet)

    def distribuer(self):
        return self.paquet.pop()

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.main = []

    def ajouter_carte(self, carte):
        self.main.append(carte)

    def calculer_points(self):
        points = 0
        as_count = 0
        for carte in self.main:
            if type(carte.valeur) == int:
                points += carte.valeur
            elif carte.valeur in ['valet', 'dame', 'roi']:
                points += 10
            else:  # as
                as_count += 1
                points += 11
        while points > 21 and as_count > 0:
            points -= 10
            as_count -= 1
        return points

class Partie:
    def __init__(self):
        self.jeu = Jeu()
        self.jeu.melanger()
        self.joueur = Joueur('Joueur')
        self.croupier = Joueur('Croupier')

    def jouer(self):
        # Distribution initiale
        for i in range(2):
            self.joueur.ajouter_carte(self.jeu.distribuer())
            self.croupier.ajouter_carte(self.jeu.distribuer())

        # Tour du joueur
        while True:
            print(f"{self.joueur.nom} a la main : {[carte.valeur for carte in self.joueur.main]} ({self.joueur.calculer_points()} points)")
            if self.joueur.calculer_points() >= 21:
                break
            choix = input("Voulez-vous prendre une carte (P) ou passer (S) ? ").lower()
            if choix == 'p':
                self.joueur.ajouter_carte(self.jeu.distribuer())
            else:
                break

        # Tour du croupier
        while self.croupier.calculer_points() < 17:
            self.croupier.ajouter_carte(self.jeu.distribuer())

        # Résultat
        print(f"{self.joueur.nom} a la main : {[carte.valeur for carte in self.joueur.main]} ({self.joueur.calculer_points()} points)")
        print(f"{self.croupier.nom} a la main : {[carte.valeur for carte in self.croupier.main]} ({self.croupier.calculer_points()} points)")
        if self.joueur.calculer_points() > 21:
            print("Vous avez dépassé 21 points, vous avez perdu !")
        elif self.croupier.calculer_points() > 21 or self.joueur.calculer_points() > self.croupier.calculer_points():
            print("Vous avez gagné !")
        elif self.joueur.calculer_points() < self.croupier.calculer_points():
            print