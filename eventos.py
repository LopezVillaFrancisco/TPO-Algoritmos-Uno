# eventos.py

def mostrar_menu_eventos():
    print("\n--- Modelo de Evento ---")
    print("1. Alta de Evento")
    print("2. Baja de Evento")
    print("3. Modificar Evento")
    print("4. Listar Eventos")
    print("5. Filtrar Eventos por Fecha")
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
    cliente = input("Ingrese nombre del cliente: ")
    fecha = input("Ingrese fecha del evento: ")
    tipo = input("Ingrese tipo de evento: ")
    evento = {
        "cliente": cliente,
        "fecha": fecha,
        "tipo": tipo
    }
    eventos.append(evento)
    print("Evento agregado.")


def baja_evento(eventos):
    cliente = input("Ingrese nombre del evento a eliminar: ")
    for e in eventos:
        if e['cliente'] == cliente:
            eventos.remove(e)
            print("Evento eliminado.")
            return
    print("Evento no encontrado.")


def modificar_evento(eventos):
    cliente = input("Ingrese nombre del evento a modificar: ")
    for e in eventos:
        if e['cliente'] == cliente:
            nuevo_cliente = input("Nuevo nombre del cliente: ")
            nueva_fecha = input("Nueva fecha (DD/MM/AAAA): ")
            nuevo_tipo = input("Nuevo tipo de evento: ")  
            e.update({"cliente": nuevo_cliente, "fecha": nueva_fecha, "tipo": nuevo_tipo})
            print("Evento modificado.")
            return
    print("Evento no encontrado.")


def listar_eventos(eventos):
    print("\nLista de Eventos:")
    for e in eventos:
        print(f"- Cliente: {e['cliente']}, Fecha: {e['fecha']}, Tipo: {e['tipo']}")
        
def filtrar_eventos_por_fecha(eventos):
    fecha_busqueda = input("Ingrese fecha a filtrar (DD/MM/AAAA): ")
    
    eventos_filtrados = list(filter(lambda evento: evento['fecha'] == fecha_busqueda, eventos))
    
    if eventos_filtrados:
        print(f"\nEventos para la fecha {fecha_busqueda}:")
        for e in eventos_filtrados:
            print(f"- Cliente: {e['cliente']}, Tipo: {e['tipo']}")
    else:
        print(f"No hay eventos para la fecha {fecha_busqueda}")

def abm_eventos(eventos):
    while True:
        mostrar_menu_eventos()
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            alta_evento(eventos)
        elif opcion == 2:
            baja_evento(eventos)
        elif opcion == 3:
            modificar_evento(eventos)
        elif opcion == 4:
            listar_eventos(eventos)
        elif opcion == 5:
            filtrar_eventos_por_fecha(eventos)
        elif opcion == 0:
            break
        else:
            print("Opción inválida.")
