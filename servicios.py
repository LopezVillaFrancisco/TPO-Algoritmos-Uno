from persistencia import guardar_servicios


def mostrar_menu_servicios():
    """Muestra el menú de opciones para servicios."""
    print("\n--- ABM Servicios ---")
    print("1. Alta de Servicio")
    print("2. Baja de Servicio")
    print("3. Modificar Servicio")
    print("4. Listar Servicios")
    print("5. Buscar servicio por nombre")
    print("6. Listar servicios ordenados alfabéticamente")
    print("0. Volver al menú principal")


def alta_servicio(servicios):
    """Pide datos por consola y agrega un servicio a la lista."""
    try:
        nombre = input("Ingrese nombre del servicio: ").strip()
        while nombre == "":
            nombre = input("El nombre no puede estar vacío. Ingrese nombre del servicio: ").strip()
        descripcion = input("Ingrese descripción: ").strip()
        while descripcion == "":
            descripcion = input("La descripción no puede estar vacía. Ingrese descripción: ").strip()
        try:
            costo = int(input("Ingrese costo: "))
            while costo <= 0 or costo >99999:
                costo = int(input("Error costo invalido, ingrese costo nuevamente (0-99999): "))
        except ValueError:
            print("Error: el costo debe ser un número válido.")
            return
        servicio = {"nombre": nombre, "descripcion": descripcion, "costo": costo}
        servicios.append(servicio)
        print("Servicio agregado.")
        # Guardar inmediatamente en JSON
        guardar_servicios(servicios)
    except (ValueError, IndexError, TypeError):
        print("Error: no se pudo agregar el servicio. Revise los datos.")


def baja_servicio(servicios):
    """Elimina un servicio por nombre si existe."""
    try:
        nombre = input("Ingrese nombre del servicio a eliminar: ").strip()
        while nombre == "":
            nombre = input("El nombre no puede estar vacío. Ingrese nombre del servicio a eliminar: ").strip()
        for servicio in servicios:
            if servicio.get('nombre') == nombre:
                servicios.remove(servicio)
                print("Servicio eliminado.")
                guardar_servicios(servicios)
                return
        print("Servicio no encontrado.")
    except (ValueError, IndexError, TypeError):
        print("Error: no se pudo eliminar el servicio. Revise la entrada.")


def modificar_servicio(servicios):
    """Modifica los campos de un servicio identificado por nombre."""
    try:
        nombre = input("Ingrese nombre del servicio a modificar: ").strip()
        while nombre == "":
            nombre = input("El nombre no puede estar vacío. Ingrese nombre del servicio a modificar: ").strip()
        for servicio in servicios:
            if servicio.get('nombre') == nombre:
                nuevo_nombre = input("Ingrese el nuevo nombre: ").strip()
                while nuevo_nombre == "":
                    nuevo_nombre = input("El nombre no puede estar vacío. Ingrese el nuevo nombre: ").strip()
                nueva_descripcion = input("Ingrese la nueva descripción: ")
                while nueva_descripcion == "" or nueva_descripcion == ' ':
                    nueva_descripcion = input("La descripción no puede estar vacía. Ingrese la nueva descripción: ")
                try:
                    nuevo_costo = int(input("Ingrese el nuevo costo: "))
                    while nuevo_costo <= 0 or nuevo_costo > 99999:
                        nuevo_costo = input("El costo no puede estar vacío. Ingrese el nuevo costo: ")
                    servicio.update({"nombre": nuevo_nombre, "descripcion": nueva_descripcion, "costo": nuevo_costo})
                except ValueError:
                    print("Error: el costo debe ser un número válido.")
                    return
                print("Servicio modificado.")
                guardar_servicios(servicios)
                return
        print("Servicio no encontrado.")
    except (ValueError, IndexError, TypeError):
        print("Error: no se pudo modificar el servicio. Revise los datos.")


def listar_servicios(servicios):
    """Imprime la lista de servicios usando una lista por comprensión."""
    print("\nLista de Servicios:")
    lineas = [f"- {servicio.get('nombre')} | {servicio.get('descripcion')} | ${servicio.get('costo')}" for servicio in servicios]
    for linea in lineas:
        print(linea)


FUNCIONES_ORDEN_SERVICIOS = {
    'nombre': lambda servicio: servicio.get('nombre', '').lower(),
    'costo': lambda servicio: float(servicio.get('costo')) if isinstance(servicio.get('costo'), (int, float)) or str(servicio.get('costo')).replace('.','',1).isdigit() else servicio.get('costo', 0),
}

def buscar_servicio_por_nombre(lista_servicios, nombre):
    """Busca un servicio por nombre y lo devuelve si existe."""
    objetivo = nombre.strip().lower()
    for servicio in lista_servicios:
        if servicio.get('nombre','').strip().lower() == objetivo:
            return servicio
    return None

def listar_servicios_ordenado(lista_servicios):
    """Imprime la lista de servicios ordenada alfabéticamente por nombre."""
    lista_ordenada = sorted(lista_servicios, key=FUNCIONES_ORDEN_SERVICIOS['nombre'])
    print("\nServicios ordenados alfabéticamente:")
    lineas = [f"- {s.get('nombre')} | {s.get('descripcion')} | ${s.get('costo')}" for s in lista_ordenada]
    for linea in lineas:
        print(linea)

def abm_servicios(servicios):
    opcion = ''
    while opcion != "0":
        try:
            mostrar_menu_servicios()
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                alta_servicio(servicios)
            elif opcion == "2":
                baja_servicio(servicios)
            elif opcion == "3":
                modificar_servicio(servicios)
            elif opcion == "4":
                listar_servicios(servicios)
            elif opcion == "5":
                nombre_buscar = input("Ingrese nombre del servicio a buscar: ")
                res = buscar_servicio_por_nombre(servicios, nombre_buscar)
                if res:
                    print("Servicio encontrado:", res)
                else:
                    print("Servicio no encontrado.")
            elif opcion == "6":
                listar_servicios_ordenado(servicios)
            elif opcion == "0":
                break
            else:
                print("Opción inválida.")
        except (ValueError, IndexError, TypeError):
            print("Error en el menú de servicios. Intente nuevamente.")
