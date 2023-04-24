class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages

    def get_titre(self):
        return self.__titre

    def set_titre(self, titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_nb_pages(self):
        return self.__nb_pages

    def set_nb_pages(self, nb_pages):
        if isinstance(nb_pages, int) and nb_pages > 0:
            self.__nb_pages = nb_pages
        else:
            print("Erreur: le nombre de pages doit être un entier positif")
livre1 = Livre("Python pour les nuls", "J.P. Mueller", 388)
print(livre1.get_titre())  # Affiche "Python pour les nuls"
print(livre1.get_auteur())  # Affiche "J.P. Mueller"
print(livre1.get_nb_pages())  # Affiche 388

livre1.set_nb_pages(400)
print(livre1.get_nb_pages())  # Affiche 400

livre1.set_nb_pages("500")  # Affiche "Erreur: le nombre de pages doit être un entier positif"