import math

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius
        
    def aire(self):
        return math.pi * self.radius ** 2

# Instanciation de la classe Rectangle
rectangle = Rectangle(5, 7)

# Instanciation de la classe Cercle
cercle = Cercle(4)

# Impression de l'aire du rectangle et du cercle
print(rectangle.aire())  # Résultat : 35
print(cercle.aire())  # Résultat : 50.26548245743669