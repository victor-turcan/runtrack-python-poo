class Student:
    def __init__(self, nom, prenom, num_etudiant):
        self.nom = nom
        self.prenom = prenom
        self.num_etudiant = num_etudiant
        self.nb_credits = 0
        self.level = self.__studentEval()

    def add_credits(self, credits):
        if credits > 0:
            self.nb_credits += credits

    def __studentEval(self):
        if self.nb_credits >= 90:
            return "Excellent"
        elif self.nb_credits >= 80:
            return "Très bien"
        elif self.nb_credits >= 70:
            return "Bien"
        elif self.nb_credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def studentInfo(self):
        print(f"Nom: {self.nom}\nPrénom: {self.prenom}\nID étudiant: {self.num_etudiant}\nNiveau: {self.level}")

# Instancier un objet représentant l'étudiant John Doe qui possède le numéro d'étudiant 145
etudiant1 = Student("Dupuis", "Damien", 145)

# Ajoutez-lui des crédits à trois reprises et imprimer son total de crédits en console.
etudiant1.add_credits(25)
etudiant1.add_credits(30)
etudiant1.add_credits(20)
print("Total de crédits:", etudiant1.nb_credits)

# Afficher les informations de l'étudiant
etudiant1.studentInfo()