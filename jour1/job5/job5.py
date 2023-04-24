class Animal:
    def __init__(self):
        self.age = 0
    
    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.nom = 'Luna'
        
animal = Animal()
print("L'age de l'animal est {} ans".format(animal.age))
animal.vieillir()
print("#Age de l'animal apres la methode vieillir")
print("l'age de l'animal est {} ans".format(animal.age))
animal.nommer("Luna")
print("L'animal se nomme", animal.nom)