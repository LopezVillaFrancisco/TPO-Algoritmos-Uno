# eventos.py

def mostrar_menu_eventos():
    print("\n--- Modelo de Evento ---")
    print("1. Alta de Evento")
    print("2. Baja de Evento")
    print("3. Modificar Evento")
    print("4. Listar Eventos")
    print("0. Volver al menú principal")


def validar_evento(nombre, fecha):
    if not nombre:
        print("El nombre no puede estar vacío.")
        return False
    if not fecha:
        print("La fecha no puede estar vacía. INGRESAR EN FORMATO (DD/MM/AAAA)")
        return False
    return True

def alta_evento(eventos):
    nombre = input("Ingrese nombre del evento: ")
    fecha = input("Ingrese fecha (DD/MM/AAAA): ")
    if validar_evento(nombre, fecha):
        eventos.append({'nombre': nombre, 'fecha': fecha})
        print("Evento agregado.")

def baja_evento(eventos):
    nombre = input("Ingrese nombre del evento a eliminar: ")
    for e in eventos:
        if e['nombre'] == nombre:
            eventos.remove(e)
            print("Evento eliminado.")
            return
    print("Evento no encontrado.")

def modificar_evento(eventos):
    nombre = input("Ingrese nombre del evento a modificar: ")
    for e in eventos:
        if e['nombre'] == nombre:
            nuevo_nombre = input("Nuevo nombre: ")
            nueva_fecha = input("Nueva fecha (DD/MM/AAAA): ")
            if validar_evento(nuevo_nombre, nueva_fecha):
                e['nombre'] = nuevo_nombre
                e['fecha'] = nueva_fecha
                print("Evento modificado.")
            return
    print("Evento no encontrado.")

def listar_eventos(eventos):
    print("\nLista de Eventos:")
    for e in eventos:
        print(f"- {e['nombre']} ({e['fecha']})")

def abm_eventos(eventos):
    while True:
        mostrar_menu_eventos()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            alta_evento(eventos)
        elif opcion == "2":
            baja_evento(eventos)
        elif opcion == "3":
            modificar_evento(eventos)
        elif opcion == "4":
            listar_eventos(eventos)
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")
