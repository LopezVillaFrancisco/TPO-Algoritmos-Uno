# empleados.py

def mostrar_menu_empleados():
    print("\n--- ABM Empleados/Encargados ---")
    print("1. Alta de Empleado/Encargado")
    print("2. Baja de Empleado/Encargado")
    print("3. Modificar Empleado/Encargado")
    print("4. Listar Empleados/Encargados")
    print("0. Volver al menú principal")

def alta_empleado(empleados):
    nombre = input("Ingrese nombre del empleado/encargado: ")
    empleados.append(nombre)
    print("Empleado/Encargado agregado.")

def baja_empleado(empleados):
    nombre = input("Ingrese nombre del empleado/encargado a eliminar: ")
    if nombre in empleados:
        empleados.remove(nombre)
        print("Empleado/Encargado eliminado.")
    else:
        print("No encontrado.")

def modificar_empleado(empleados):
    nombre = input("Ingrese nombre del empleado/encargado a modificar: ")
    if nombre in empleados:
        nuevo_nombre = input("Ingrese el nuevo nombre: ")
        idx = empleados.index(nombre)
        empleados[idx] = nuevo_nombre
        print("Empleado/Encargado modificado.")
    else:
        print("No encontrado.")

def listar_empleados(empleados):
    print("\nLista de Empleados/Encargados:")
    for e in empleados:
        print("-", e)

def abm_empleados(empleados):
    while True:
        mostrar_menu_empleados()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            alta_empleado(empleados)
        elif opcion == "2":
            baja_empleado(empleados)
        elif opcion == "3":
            modificar_empleado(empleados)
        elif opcion == "4":
            listar_empleados(empleados)
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")
