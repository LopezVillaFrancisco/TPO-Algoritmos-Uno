from persistencia import guardar_eventos


def mostrar_menu_eventos():
    """Muestra el menú de opciones para eventos"""
    print("\n--- Modelo de Evento ---")
    print("1. Alta de Evento")
    print("2. Baja de Evento")
    print("3. Modificar Evento")
    print("4. Listar Eventos")
    print("5. Buscar evento por cliente")
    print("6. Listar eventos ordenados por cliente")
    print("7. Filtrar Eventos por Fecha")
    print("0. Volver al menú principal")


def alta_evento(eventos):
    """Pide datos por consola y agrega un evento a la lista"""
    cliente = input("Ingrese nombre del cliente: ").strip()
    while cliente == "":
        cliente = input("El nombre del cliente no puede estar vacío. Ingrese nombre del cliente: ").strip()

    fecha = input("Ingrese fecha (DD/MM/AAAA): ").strip()
    while fecha == "":
        fecha = input("La fecha no puede estar vacía. Ingrese fecha (DD/MM/AAAA): ").strip()

    tipo = input("Ingrese tipo de evento: ").strip()
    while tipo == "":
        tipo = input("El tipo de evento no puede estar vacío. Ingrese tipo de evento: ").strip()

    evento = {"cliente": cliente, "fecha": fecha, "tipo": tipo}
    eventos.append(evento)
    print("Evento agregado.")
    guardar_eventos(eventos)


def baja_evento(eventos):
    """Elimina un evento por cliente si existe"""
    cliente = input("Ingrese nombre del evento a eliminar: ").strip()
    while cliente == "":
        cliente = input("El nombre del cliente no puede estar vacío. Ingrese nombre del evento a eliminar: ").strip()

    objetivo = cliente.lower()
    for evento in list(eventos):
        if evento.get('cliente', '').strip().lower() == objetivo:
            eventos.remove(evento)
            print("Evento eliminado.")
            guardar_eventos(eventos)
            return
    print("Evento no encontrado.")


def modificar_evento(eventos):
    """Modifica los datos de un evento identificado por cliente"""
    cliente = input("Ingrese nombre del evento a modificar: ").strip()
    while cliente == "":
        cliente = input("El nombre del cliente no puede estar vacío. Ingrese nombre del evento a modificar: ").strip()

    objetivo = cliente.lower()
    for evento in eventos:
        if evento.get('cliente', '').strip().lower() == objetivo:
            nuevo_cliente = input("Nuevo nombre del cliente: ").strip()
            while nuevo_cliente == "":
                nuevo_cliente = input("El nombre del cliente no puede estar vacío. Ingrese nuevo nombre del cliente: ").strip()

            nueva_fecha = input("Nueva fecha (DD/MM/AAAA): ").strip()
            while nueva_fecha == "":
                nueva_fecha = input("La fecha no puede estar vacía. Ingrese nueva fecha (DD/MM/AAAA): ").strip()

            nuevo_tipo = input("Nuevo tipo de evento: ").strip()
            while nuevo_tipo == "":
                nuevo_tipo = input("El tipo de evento no puede estar vacío. Ingrese nuevo tipo de evento: ").strip()

            evento.update({"cliente": nuevo_cliente, "fecha": nueva_fecha, "tipo": nuevo_tipo})
            print("Evento modificado.")
            guardar_eventos(eventos)
            return

    print("Evento no encontrado.")


def listar_eventos(eventos):
    """Imprime la lista de eventos usando una lista por comprensión"""
    print("\nLista de Eventos:")
    if not eventos:
        print("(sin eventos)")
        return
    lineas = [f"- Cliente: {ev.get('cliente')}, Fecha: {ev.get('fecha')}, Tipo: {ev.get('tipo')}" for ev in eventos]
    for linea in lineas:
        print(linea)


FUNCIONES_ORDEN_EVENTOS = {
    'cliente': lambda ev: ev.get('cliente', '').lower(),
}


def buscar_evento_por_cliente(lista_eventos, cliente):
    """Busca un evento por cliente (case-insensitive) y lo devuelve si existe"""
    objetivo = cliente.strip().lower()
    for evento in lista_eventos:
        if evento.get('cliente', '').strip().lower() == objetivo:
            return evento
    return None


def listar_eventos_ordenado(lista_eventos):
    """Imprime los eventos ordenados por cliente (alfabéticamente)"""
    lista_ordenada = sorted(lista_eventos, key=FUNCIONES_ORDEN_EVENTOS['cliente'])
    print("\nEventos ordenados por cliente:")
    if not lista_ordenada:
        print("(sin eventos)")
        return
    lineas = [f"- Cliente: {ev.get('cliente')}, Fecha: {ev.get('fecha')}, Tipo: {ev.get('tipo')}" for ev in lista_ordenada]
    for linea in lineas:
        print(linea)
        
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
    opcion = ''
    while opcion != "0":
        try:
            mostrar_menu_eventos()
            opcion = input("Seleccione una opción: ").strip()
            if opcion == "1":
                alta_evento(eventos)
            elif opcion == "2":
                baja_evento(eventos)
            elif opcion == "3":
                modificar_evento(eventos)
            elif opcion == "4":
                listar_eventos(eventos)
            elif opcion == "5":
                nombre_buscar = input("Ingrese nombre del cliente a buscar: ")
                res = buscar_evento_por_cliente(eventos, nombre_buscar)
                if res:
                    print("Evento encontrado:", res)
                else:
                    print("Evento no encontrado.")
            elif opcion == "6":
                listar_eventos_ordenado(eventos)
            elif opcion == "7":
                filtrar_eventos_por_fecha(eventos)
            elif opcion == "0":
                break
            else:
                print("Opción inválida.")
        except (ValueError, IndexError, TypeError):
            print("Error en el menú de eventos. Intente nuevamente.")
