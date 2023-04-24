class Operation:
    def __init__(self, nombre1=12, nombre2=3):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        result = self.nombre1 + self.nombre2
        print("Le résultat de l'addition est :", result)

operation = Operation(12, 3)
operation.addition()