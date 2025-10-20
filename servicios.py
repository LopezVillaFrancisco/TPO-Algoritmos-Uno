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
        nombre = input("Ingrese nombre del servicio: ")
        descripcion = input("Ingrese descripción: ")
        costo_texto = input("Ingrese costo: ")
        costo = float(costo_texto)
        servicio = {"nombre": nombre, "descripcion": descripcion, "costo": costo}
        servicios.append(servicio)
        print("Servicio agregado.")
    except (ValueError, IndexError, TypeError):
        print("Error: no se pudo agregar el servicio. Revise los datos.")


def baja_servicio(servicios):
    """Elimina un servicio por nombre si existe."""
    try:
        nombre = input("Ingrese nombre del servicio a eliminar: ")
        for servicio in servicios:
            if servicio.get('nombre') == nombre:
                servicios.remove(servicio)
                print("Servicio eliminado.")
                return
        print("Servicio no encontrado.")
    except (ValueError, IndexError, TypeError):
        print("Error: no se pudo eliminar el servicio. Revise la entrada.")


def modificar_servicio(servicios):
    """Modifica los campos de un servicio identificado por nombre."""
    try:
        nombre = input("Ingrese nombre del servicio a modificar: ")
        for servicio in servicios:
            if servicio.get('nombre') == nombre:
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                nueva_descripcion = input("Ingrese la nueva descripción: ")
                nuevo_costo = input("Ingrese el nuevo costo: ")
                nuevo_costo_val = float(nuevo_costo)
                servicio.update({"nombre": nuevo_nombre, "descripcion": nueva_descripcion, "costo": nuevo_costo_val})
                print("Servicio modificado.")
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
