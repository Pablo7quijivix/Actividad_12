
print(f"=====PROMEDIO DE ESTUDIANTES=====")
try:
    notas =[]
    students = int(input("===¿CUANTOS ESTUDIANTES DESEA INGRESAR===: ?"))
for i in range(students):
    print(f"___INGRESE ESTUDIANTES {i+1}")
    name = input(f"___INGRESE NOMBRE DEL ESTUDIANTE___: ")
    cantidad_notas = int(input(f"___¿CUANTAS NOTAS DESEA INGRESAR___: ?"))
    for j in range(cantidad_notas):
        notes= int(input(f"___===INGRESE LA NOTA.{j+1}===: "))
        notas.append(notes)
        promedio = sum(notas) / len(notas)
print(f"=====ESTUDIANTE: {name}__PROMEDIO DEL ESTUDIANTE: {promedio}")

except ValueError:
    print("Error: Debes ingresar números válidos.")

