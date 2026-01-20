from Estudiantes import Student
from materias import Materia

def pedir_nombre_estudiante():
    while True:
        nombre = input("Ingrese el nombre del estudiante: ")
        if nombre.isalpha():
            break
        elif nombre == "":
            print("Por favor, ingrese un nombre válido.")
            continue
        else:
            print("Por favor, ingrese un nombre válido.")
            continue
    return nombre

def pedir_nombre_materia():
    while True:
        nombre_materia = input("Ingrese el nombre de la materia: ")
        if nombre_materia == "":
            print("Por favor, ingrese un nombre válido.")
            continue
        else:
            break
    return nombre_materia

def pedir_creditos():
    while True:
        try:
            creditos = int(input("Ingrese los créditos de la materia: "))
            if creditos < 0:
                print("Por favor, ingrese una cantidad válida de créditos.")
                continue
            else:
                break
        except ValueError:
            print("Por favor, ingrese una cantidad válida de créditos.")
            continue
        else:
            break
    return creditos

def pedir_nota():
    while True:
        try:
            nota = float(input("Ingrese la nota: "))
            if nota < 0 or nota > 10:
                print("Por favor, ingrese una nota válida.")
                continue
            else:
                break
        except ValueError:
            print("Por favor, ingrese una nota válida.")
            continue
    return nota

nombre_estudiante = pedir_nombre_estudiante()
nombre = Student(nombre_estudiante)
while True:
    nombre_materia = pedir_nombre_materia()
    creditos = pedir_creditos()
    nota = pedir_nota()
    
    materia = Materia(nombre_materia, creditos)
    materia.calificar(nota)
    nombre.add_grades(materia)
    materia.esta_aprobada()

    desicion = input("¿desea agregar mas materias?s/n")
    if desicion == "s":
        continue
    else:
        break

average, status = nombre.get_average()
nombre.keep()
materia.keep()

print(f"El promedio de {nombre_estudiante} es: {average}")
print(f"Estado: {status}")
print("El promedio de todas las notas es: ")
print("registro guardado")