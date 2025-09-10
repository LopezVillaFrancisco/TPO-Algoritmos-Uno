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
    dni = input("Ingrese DNI: ")
    tarea = input("Ingrese tarea: ")
    empleado = {
        "nombre": nombre,
        "dni": dni,
        "tarea": tarea
    }
    empleados.append(empleado)
    print("Empleado/Encargado agregado.")


def baja_empleado(empleados):
    nombre = input("Ingrese nombre del empleado/encargado a eliminar: ")
    for e in empleados:
        if e['nombre'] == nombre:
            empleados.remove(e)
            print("Empleado/Encargado eliminado.")
            return
    print("No encontrado.")


def modificar_empleado(empleados):
    nombre = input("Ingrese nombre del empleado/encargado a modificar: ")
    for e in empleados:
        if e['nombre'] == nombre:
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            nuevo_dni = input("Ingrese el nuevo DNI: ")
            nueva_tarea = input("Ingrese la nueva tarea: ")
            e.update({"nombre": nuevo_nombre, "dni": nuevo_dni, "tarea": nueva_tarea})
            print("Empleado/Encargado modificado.")
            return
    print("No encontrado.")

def listar_empleados(empleados):
    print("\nLista de Empleados/Encargados:")
    for e in empleados:
        print(f"- {e['nombre']} (DNI: {e['dni']}, Tarea: {e['tarea']})")

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
