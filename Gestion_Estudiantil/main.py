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
nombre_materia = pedir_nombre_materia()
nota = pedir_nota()

nombre = Student(nombre_estudiante)
nombre.add_grades(nota, nombre_materia)
average, status = nombre.get_average()
nombre.keep()

print(f"El promedio de {nombre_estudiante} es: {average}")
print(f"Estado: {status}")
print("El promedio de todas las notas es: ")
print("registro guardado")