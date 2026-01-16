class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grades(self, Materias):
        self.grades.append(Materias)
    
    def get_average(self):
        try:
            if not self.grades:
                return (0, "sin materias")

            suma_total = 0
            for i in self.grades:
                suma_total += i.nota

            average = suma_total / len(self.grades)

            if average >= 6:
                status = "aprobado"
            else:
                status = "reprobado"
            return (average, status)
        except ZeroDivisionError:
            return (0, "sin calificacion")

    def aprobados(self):
        return [i for i in self.grades if i.nota >= 6]

    def keep(self):
        with open("reporte.txt", "a") as archivo:
            archivo.write(f"nombre: {self.name} | notas: {self.get_average()}\n")