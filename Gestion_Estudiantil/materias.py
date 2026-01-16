class Materia:
    def __init__(self, nombre, creditos):
        self.nombre = nombre
        self.creditos = creditos
        self.nota = None 

    def calificar(self, valor):
        self.nota = valor

    def esta_aprobada(self):
        if self.nota and self.nota >= 6:
            return True
        return False

    def keep(self):
        with open("reporte.txt", "a") as archivo:
            archivo.write(f"nombre: {self.nombre} | creditos: {self.creditos} | nota: {self.nota}\n")