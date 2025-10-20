def mostrar_menu_empleados():
    """Muestra el menú de opciones para empleados/encargados."""
    print("\n--- ABM Empleados/Encargados ---")
    print("1. Alta de Empleado/Encargado")
    print("2. Baja de Empleado/Encargado")
    print("3. Modificar Empleado/Encargado")
    print("4. Listar Empleados/Encargados")
    print("5. Buscar empleado por nombre")
    print("6. Listar ordenado alfabéticamente")
    print("0. Volver al menú principal")

def alta_empleado(empleados):
    """Pide datos por consola y agrega un empleado a la lista."""
    try:
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
    except (ValueError, IndexError, TypeError):
        print("Error: no se pudo agregar el empleado. Revise la entrada.")


def baja_empleado(empleados):
    """Pide un nombre y elimina el empleado correspondiente si existe."""
    try:
        nombre = input("Ingrese nombre del empleado/encargado a eliminar: ")
        for empleado in empleados:
            if empleado.get('nombre') == nombre:
                empleados.remove(empleado)
                print("Empleado/Encargado eliminado.")
                return
        print("No encontrado.")
    except (ValueError, IndexError, TypeError):
        print("Error: no se pudo eliminar el empleado. Revise la entrada.")


def modificar_empleado(empleados):
    """Modifica los datos de un empleado identificado por nombre."""
    try:
        nombre = input("Ingrese nombre del empleado/encargado a modificar: ")
        for empleado in empleados:
            if empleado.get('nombre') == nombre:
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                nuevo_dni = input("Ingrese el nuevo DNI: ")
                nueva_tarea = input("Ingrese la nueva tarea: ")
                empleado.update({"nombre": nuevo_nombre, "dni": nuevo_dni, "tarea": nueva_tarea})
                print("Empleado/Encargado modificado.")
                return
        print("No encontrado.")
    except (ValueError, IndexError, TypeError):
        print("Error: no se pudo modificar el empleado. Revise los datos ingresados.")

def listar_empleados(empleados):
    """Imprime la lista de empleados tal como están (sin ordenar).

    Usa una lista por comprensión internamente para preparar las líneas.
    """
    print("\nLista de Empleados/Encargados:")
    lineas = [f"- {empleado.get('nombre')} (DNI: {empleado.get('dni')}, Tarea: {empleado.get('tarea')})" for empleado in empleados]
    for linea in lineas:
        print(linea)


def buscar_por_nombre(lista_empleados, nombre):
    """Busca un empleado por nombre (case-insensitive) y lo devuelve si existe."""
    objetivo = nombre.strip().lower()
    for empleado in lista_empleados:
        if empleado.get('nombre', '').strip().lower() == objetivo:
            return empleado
    return None

FUNCIONES_ORDENAMIENTO = {
    'nombre': lambda empleado: empleado.get('nombre', '').lower(),
    'dni': lambda empleado: int(empleado.get('dni')) if str(empleado.get('dni')).isdigit() else empleado.get('dni', ''),
    'tarea': lambda empleado: empleado.get('tarea', '').lower(),
}

def listar_empleados_ordenado(lista_empleados):
    """Imprime la lista de empleados ordenada alfabéticamente por nombre (ascendente)."""
    lista_ordenada = sorted(lista_empleados, key=FUNCIONES_ORDENAMIENTO['nombre'])

    print("\nLista ordenada alfabéticamente por nombre:")
    for empleado in lista_ordenada:
        print(f"- {empleado['nombre']} (DNI: {empleado['dni']}, Tarea: {empleado['tarea']})")

def abm_empleados(empleados):
    """Bucle principal del ABM de empleados (interfaz de consola)."""
    opcion = ''
    while opcion != "0":
        try:
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
            elif opcion == "5":
                listar_empleados_ordenado(empleados)
            elif opcion == "0":
                break
            else:
                print("Opción inválida.")
        except (ValueError, IndexError, TypeError):
            print("Error en el menú de empleados. Intente nuevamente.")
