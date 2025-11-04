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
    print("0. Volver al menú principal")

def alta_evento(eventos):
    """Pide datos por consola y agrega un evento a la lista"""
    try:
        cliente = input("Ingrese nombre del cliente: ")
        while cliente == "" or cliente ==' ':
            cliente = input("El nombre del cliente no puede estar vacío. Ingrese nombre del cliente: ")
        fecha = input("Ingrese fecha (DD/MM/AAAA): ")
        while fecha == "" or fecha ==' ':
            fecha = input("La fecha no puede estar vacía. Ingrese fecha (DD/MM/AAAA): ")
        tipo = input("Ingrese tipo de evento: ")
        while tipo == "" or tipo == ' ':
            tipo = input("El tipo de evento no puede estar vacío. Ingrese tipo de evento: ")
        evento = {
            "cliente": cliente,
            "fecha": fecha,
            "tipo": tipo
        }
        eventos.append(evento)
        print("Evento agregado")
        guardar_eventos(eventos)
    except (ValueError, IndexError, TypeError):
        print("Error: no se pudo agregar el evento. Revise los datos")


def baja_evento(eventos):
    """Elimina un evento por cliente si existe"""
    try:
        cliente = input("Ingrese nombre del evento a eliminar: ")
        while cliente == "" or cliente ==' ':
            cliente = input("El nombre del cliente no puede estar vacío. Ingrese nombre del evento a eliminar: ")
        for evento in eventos:
            if evento.get('cliente') == cliente:
                eventos.remove(evento)
                print("Evento eliminado")
                guardar_eventos(eventos)
                return
        print("Evento no encontrado")
    except (ValueError, IndexError, TypeError):
        print("Error: no se pudo eliminar el evento. Revise la entrada")


def modificar_evento(eventos):
    """Modifica los datos de un evento identificado por cliente"""
    try:
        cliente = input("Ingrese nombre del evento a modificar: ")
        while cliente == "" or cliente ==' ':
            cliente = input("El nombre del cliente no puede estar vacío. Ingrese nombre del evento a modificar: ")
        for evento in eventos:
            if evento.get('cliente') == cliente:
                nuevo_cliente = input("Nuevo nombre del cliente: ")
                while nuevo_cliente == "" or nuevo_cliente == ' ':
                    nuevo_cliente = input("El nombre del cliente no puede estar vacío. Ingrese nuevo nombre del cliente: ")
                nueva_fecha = input("Nueva fecha (DD/MM/AAAA): ")
                while nueva_fecha == "" or nueva_fecha == ' ':
                    nueva_fecha = input("La fecha no puede estar vacía. Ingrese nueva fecha (DD/MM/AAAA): ")
                nuevo_tipo = input("Nuevo tipo de evento: ")
                while nuevo_tipo == "" or nuevo_tipo == ' ':
                    nuevo_tipo = input("El tipo de evento no puede estar vacío. Ingrese nuevo tipo de evento: ")
                evento.update({"cliente": nuevo_cliente, "fecha": nueva_fecha, "tipo": nuevo_tipo})
                print("Evento modificado")
                guardar_eventos(eventos)
                return
        print("Evento no encontrado")
    except (ValueError, IndexError, TypeError):
        print("Error: no se pudo modificar el evento. Revise los datos")


def listar_eventos(eventos):
    """Imprime la lista de eventos usando una lista por comprensión"""
    print("\nLista de Eventos:")
    lineas = [f"- Cliente: {ev.get('cliente')}, Fecha: {ev.get('fecha')}, Tipo: {ev.get('tipo')}" for ev in eventos]
    for linea in lineas:
        print(linea)


FUNCIONES_ORDEN_EVENTOS = {
    'cliente': lambda ev: ev.get('cliente','').lower(),
}

def buscar_evento_por_cliente(lista_eventos, cliente):
    """Busca un evento por cliente (case-insensitive) y lo devuelve si existe"""
    objetivo = cliente.strip().lower()
    for evento in lista_eventos:
        if evento.get('cliente','').strip().lower() == objetivo:
            return evento
    return None

def listar_eventos_ordenado(lista_eventos):
    """Imprime los eventos ordenados por cliente (alfabéticamente)"""
    lista_ordenada = sorted(lista_eventos, key=FUNCIONES_ORDEN_EVENTOS['cliente'])
    print("\nEventos ordenados por cliente:")
    lineas = [f"- Cliente: {ev.get('cliente')}, Fecha: {ev.get('fecha')}, Tipo: {ev.get('tipo')}" for ev in lista_ordenada]
    for linea in lineas:
        print(linea)

def abm_eventos(eventos):
    opcion = ''
    while opcion != "0":
        try:
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
            elif opcion == "5":
                nombre_buscar = input("Ingrese nombre del cliente a buscar: ")
                res = buscar_evento_por_cliente(eventos, nombre_buscar)
                if res:
                    print("Evento encontrado:", res)
                else:
                    print("Evento no encontrado")
            elif opcion == "6":
                listar_eventos_ordenado(eventos)
            elif opcion == "0":
                break
            else:
                print("Opción inválida")
        except (ValueError, IndexError, TypeError):
            print("Error en el menú de eventos. Intente nuevamente")
