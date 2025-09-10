def mostrar_menu_servicios():
    print("\n--- ABM Servicios ---")
    print("1. Alta de Servicio")
    print("2. Baja de Servicio")
    print("3. Modificar Servicio")
    print("4. Listar Servicios")
    print("0. Volver al menú principal")


def alta_servicio(servicios):
    nombre = input("Ingrese nombre del servicio: ")
    descripcion = input("Ingrese descripción: ")
    costo = input("Ingrese costo: ")
    servicio = {"nombre": nombre, "descripcion": descripcion, "costo": costo}
    servicios.append(servicio)
    print("Servicio agregado.")


def baja_servicio(servicios):
    nombre = input("Ingrese nombre del servicio a eliminar: ")
    for s in servicios:
        if s['nombre'] == nombre:
            servicios.remove(s)
            print("Servicio eliminado.")
            return
    print("Servicio no encontrado.")


def modificar_servicio(servicios):
    nombre = input("Ingrese nombre del servicio a modificar: ")
    for s in servicios:
        if s['nombre'] == nombre:
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            nueva_descripcion = input("Ingrese la nueva descripción: ")
            nuevo_costo = input("Ingrese el nuevo costo: ")
            s.update({"nombre": nuevo_nombre, "descripcion": nueva_descripcion, "costo": nuevo_costo})
            print("Servicio modificado.")
            return
    print("Servicio no encontrado.")


def listar_servicios(servicios):
    print("\nLista de Servicios:")
    for s in servicios:
        print(f"- {s['nombre']} | {s['descripcion']} | ${s['costo']}")

def abm_servicios(servicios):
    while True:
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
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")
