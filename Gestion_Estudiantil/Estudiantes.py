class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grades(self, Materias):
        self.grades.append(Materias)
    
    def get_average(self):
        if not self.grades:
            return (0, "sin materias")

        suma_ponderada = 0
        total_creditos = 0
        
        for materia in self.grades:
            if materia.nota is not None:
                suma_ponderada += materia.nota * materia.creditos
                total_creditos += materia.creditos
        
        if total_creditos == 0:
            return (0, "sin creditos")

        average = suma_ponderada / total_creditos

        if average >= 6:
            status = "aprobado"
        else:
            status = "reprobado"
            
        return (average, status)

    def aprobados(self):
        return [i for i in self.grades if i.nota >= 6]

    def keep(self):
        with open("reporte.txt", "a") as archivo:
            archivo.write(f"nombre: {self.name} | notas: {self.get_average()}\n")