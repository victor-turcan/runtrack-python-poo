class Vehicule:
    def __init__(self, marque, annee, prix):
        self.marque = marque
        self.annee = annee
        self.prix = prix
    
    def informationsVehicule(self):
        print(f"Marque: {self.marque}\nAnnée: {self.annee}\nPrix: {self.prix}")

    def demarrer(self):
        print("Attention, je roule.")

class Voiture(Vehicule):
    def __init__(self, marque, annee, prix, portes):
        super().__init__(marque, annee, prix)
        self.portes = portes
    
    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Portes: {self.portes}")
    
    def demarrer(self):
        print("La voiture démarre.")

class Moto(Vehicule):
    def __init__(self, marque, annee, prix, roue=2):
        super().__init__(marque, annee, prix)
        self.roue = roue
    
    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Roues: {self.roue}")
    
    def demarrer(self):
        print("La moto démarre.")

# Instanciation d'un objet Voiture
ma_voiture = Voiture("Peugeot", 2022, 20000, 5)
ma_voiture.informationsVehicule()
ma_voiture.demarrer()

# Instanciation d'un objet Moto
ma_moto = Moto("Yamaha", 2023, 15000)
ma_moto.informationsVehicule()
ma_moto.demarrer()