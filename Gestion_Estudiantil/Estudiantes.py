class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grades(self, grade, signature):
        self.grades.append([signature, grade])

    def get_average(self):
        try:
            suma_total = 0
            for i in self grades:
                suma_total += i[1]

            average = suma_total / len(self.grades)

            if average >= 6:
                status = "aprobado"
            else:
                status = "reprobado"
            return (average, status)
        except ZeroDivisionError:
            return (0, "sin calificacion")

    def aprovados (self):
        return [i[1] for i in self.grades if i[1] >= 6]

    def keep(self):
        with open("reporte.txt", "a") as archivo:
            archivo.write(f"nombre: {self.name} | notas: {self.get_average()}\n")