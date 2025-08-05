
print(f"=====PROMEDIO DE ESTUDIANTES=====")
notas={}
while True:
    try:

        while True:
            #pedimos la cantidad de estudiantes que queremos
            students = int(input("===¿CUANTOS ESTUDIANTES DESEA INGRESAR===?: "))
            #iteramos para recopilar cada dato del estudiante: nombre, cantidad de notas que desea, las notas
            for i in range(students):
                print(f"\n___INGRESE ESTUDIANTES {i+1}")
                name = input(f"___INGRESE NOMBRE DEL ESTUDIANTE___: ")
                cantidad_notas = int(input(f"___¿CUANTAS NOTAS DESEA INGRESAR PARA EL ESTUDIANTE: {name}___: ?"))

                #lista para guardar las notas de este estudiante
                notas_2= []
                for j in range(cantidad_notas):
                    notes=int(input(f"\n___INGRESE LA NOTA: {j+1} DEL ESTUDIANTE:{name}____: "))
                    notas_2.append(notes)
                    #estamos guardando la lista dentro del diccionario
                    notas['name'] = notas_2
                    print(f"la nota es {notas['name'][2]}")
                    promedio = sum(notas_2) / len(notas_2)
                    print(promedio)
    except ValueError:
        print(f"Error: Debes ingresar numeros validos.")

    except ZeroDivisionError:
        print(f"Error: no se puede dividir dentro de cero.")

    except TypeError:
        print(f"No puedes combinar 2 tipos de datos diferentes (texto + numero).")

    except Exception as e:
        print("Se produjo un error inesperado:",e)

    else:
        print(f"====EL RESULTADO DEL PROMEDIO DEL ESTUDIANTE: {name} ES IGUAL A:{notas[promedio]} ====")

    finally:
        print("Fin del proceso.")


#print(f"=====ESTUDIANTE: {name}__PROMEDIO DEL ESTUDIANTE: {promedio}")


