class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def SePresenter(self):
        return "Je m'appelle {} {}".format(self.prenom, self.nom)

personne1 = Personne("Doe", "John")
personne2 = Personne("Dupont", "Jean")

print(personne1.SePresenter())
print(personne2.SePresenter())