class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur

        # Créer un rectangle de longueur 10 et de largeur 5
mon_rectangle = Rectangle(10, 5)

# Afficher les valeurs initiales
print("Longueur :", mon_rectangle.get_longueur())  # Résultat attendu : 10
print("Largeur :", mon_rectangle.get_largeur())  # Résultat attendu : 5

# Modifier la longueur et la largeur
mon_rectangle.set_longueur(8)
mon_rectangle.set_largeur(3)

# Vérifier que les modifications ont été prises en compte
print("Longueur modifiée :", mon_rectangle.get_longueur())  # Résultat attendu : 8
print("Largeur modifiée :", mon_rectangle.get_largeur())  # Résultat attendu : 3