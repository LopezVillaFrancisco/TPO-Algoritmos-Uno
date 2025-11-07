from persistencia import guardar_eventos
import datetime


def parsear_eventos_date(eventos):
    """Parsea los eventos de texto a objetos datetime.date."""
    for evento in eventos:
        fecha = evento.get('fecha')
        # Intentar usar strip() si falla no es string
        try:
            fecha_string = fecha.strip()
        except Exception as e:
            raise TypeError(f"Campo 'fecha' inválido en evento {evento}: {e}")

        if not fecha_string:
            raise ValueError(f"Campo 'fecha' vacío en evento {evento}")
        try:
            evento['fecha'] = datetime.datetime.strptime(fecha_string, "%d/%m/%Y").date()
        except ValueError as e:
            raise ValueError(f"Formato de fecha inválido en evento {evento}: {e}")


def parsear_eventos_JSON(eventos):
    """Parsea la lista de eventos a diccionario para poder guardarlo en JSON."""
    salida = []
    for evento in eventos:
        #Se hace una copia del evento para no modificar el original
        evento_parsear = evento.copy()
        fecha = evento_parsear.get('fecha')
        try:
            # Intentar formatear la fecha a string
            evento_parsear['fecha'] = fecha.strftime("%d/%m/%Y")
        except Exception:
            evento_parsear['fecha'] = "" if fecha is None else str(fecha)
        salida.append(evento_parsear)
    return salida


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
    """Pide datos por consola y agrega un evento a la lista (fecha -> datetime.date)"""
    cliente = input("Ingrese nombre del cliente: ").strip()
    while cliente == "":
        cliente = input("El nombre del cliente no puede estar vacío. Ingrese nombre del cliente: ").strip()

    # pedir nueva fecha y convertir a datetime.date
    fecha = None
    while fecha is None:
        try:
            dia = int(input("Ingrese día (1-31): "))
            while dia <= 0 or dia > 31:
                dia = int(input("Día inválido. Debe estar entre 1 y 31. Ingrese día (1-31): "))

            mes = int(input("Ingrese mes (1-12): "))
            while mes <= 0 or mes > 12:
                mes = int(input("Mes inválido. Debe estar entre 1 y 12. Ingrese mes (1-12): "))

            anio = int(input("Ingrese año (debe ser 2025): "))
            while anio != 2025:
                anio = int(input("Año inválido. Debe ser 2025. Ingrese año (debe ser 2025): "))

            # Se convierte la fecha con tipo datetime.date
            fecha = datetime.date(anio, mes, dia)

            # validar que no exista ya un evento para esa fecha
            existe_mismo_dia = False
            for otro_evento in eventos:
                if otro_evento.get("fecha") == fecha:
                    existe_mismo_dia = True

            if existe_mismo_dia:
                print("Ya existe un evento para esa fecha. Elija otra fecha.")
                fecha = None

        except ValueError:
            print("Ingrese números enteros válidos o una combinación de fecha real.")

    tipo = input("Ingrese tipo de evento: ").strip()
    while tipo == "":
        tipo = input("El tipo de evento no puede estar vacío. Ingrese tipo de evento: ").strip()

    evento = {"cliente": cliente, "fecha": fecha, "tipo": tipo}
    eventos.append(evento)
    print("Evento agregado.")
    guardar_eventos(parsear_eventos_JSON(eventos))

def baja_evento(eventos):
    """Elimina un evento por cliente si existe"""
    cliente = input("Ingrese nombre del evento a eliminar: ").strip()
    while cliente == "":
        cliente = input("El nombre del cliente no puede estar vacío. Ingrese nombre del evento a eliminar: ").strip()

    cliente_objetivo = cliente.lower()
    for evento in list(eventos):
        if evento.get('cliente', '').strip().lower() == cliente_objetivo:
            eventos.remove(evento)
            print("Evento eliminado.")
            guardar_eventos(parsear_eventos_JSON(eventos))
            return
    print("Evento no encontrado.")


def modificar_evento(eventos):
    """Modifica los datos de un evento identificado por cliente"""
    cliente = input("Ingrese nombre del evento a modificar: ").strip()
    while cliente == "":
        cliente = input("El nombre del cliente no puede estar vacío. Ingrese nombre del evento a modificar: ").strip()

    cliente_objetivo = cliente.lower()
    for evento in eventos:
        if evento.get('cliente', '').strip().lower() == cliente_objetivo:
            nuevo_cliente = input("Nuevo nombre del cliente: ").strip()
            while nuevo_cliente == "":
                nuevo_cliente = input("El nombre del cliente no puede estar vacío. Ingrese nuevo nombre del cliente: ").strip()

            """ pedir nueva fecha y convertir a datetime.date"""
            while True:
                try:
                    dia = int(input("Nuevo día (1-31): "))
                    while dia <= 0 or dia > 31:
                        dia = int(input("Día inválido. Debe estar entre 1 y 31. Ingrese nuevo día: "))
                    mes = int(input("Nuevo mes (1-12): "))
                    while mes <= 0 or mes > 12:
                        mes = int(input("Mes inválido. Debe estar entre 1 y 12. Ingrese nuevo mes: "))
                    anio = int(input("Nuevo año (debe ser 2025): "))
                    while anio != 2025:
                        anio = int(input("Año inválido. Debe ser 2025. Ingrese nuevo año: "))
                except ValueError:
                    print("Ingrese números enteros válidos para día, mes y año.")
                    continue
                try:
                    nueva_fecha = datetime.date(anio, mes, dia)
                    # validar que no exista ya un evento para esa fecha (excluyendo el evento actual)
                    existe_mismo_dia = False
                    for evento_existente in eventos:
                        if evento_existente is not evento and evento_existente.get("fecha") == nueva_fecha:
                            existe_mismo_dia = True
                    if existe_mismo_dia:
                        print("Ya existe un evento para esa fecha. Elija otra fecha.")
                        continue
                    break
                except ValueError:
                    print("Combinación día/mes/año no corresponde a una fecha real. Intente nuevamente.")

            nuevo_tipo = input("Nuevo tipo de evento: ").strip()
            while nuevo_tipo == "":
                nuevo_tipo = input("El tipo de evento no puede estar vacío. Ingrese nuevo tipo de evento: ").strip()

            evento.update({"cliente": nuevo_cliente, "fecha": nueva_fecha, "tipo": nuevo_tipo})
            print("Evento modificado.")
            guardar_eventos(parsear_eventos_JSON(eventos))
            return

    print("Evento no encontrado.")


def listar_eventos(eventos):
    """Imprime la lista de eventos en memoria (formatea fechas)"""
    print("\nLista de Eventos:")
    if not eventos:
        print("(sin eventos)")
        return
    lineas = []
    for evento in eventos:
        fecha = evento.get('fecha')
        try:
            fecha_string = fecha.strftime("%d/%m/%Y")
        except Exception:
            fecha_string = "" if fecha is None else str(fecha)
        lineas.append(f"- Cliente: {evento.get('cliente')}, Fecha: {fecha_string}, Tipo: {evento.get('tipo')}")
    for linea in lineas:
        print(linea)


FUNCIONES_ORDEN_EVENTOS = {
    'cliente': lambda ev: ev.get('cliente', '').lower(),
}


def buscar_evento_por_cliente(lista_eventos, cliente):
    """Busca un evento por cliente (case-insensitive) y lo devuelve si existe"""
    cliente_objetivo = cliente.strip().lower()
    for evento in lista_eventos:
        if evento.get('cliente', '').strip().lower() == cliente_objetivo:
            return evento
    return None


def listar_eventos_ordenado(lista_eventos):
    """Imprime los eventos ordenados por cliente (alfabéticamente)"""
    lista_ordenada = sorted(lista_eventos, key=FUNCIONES_ORDEN_EVENTOS['cliente'])
    print("\nEventos ordenados por cliente:")
    if not lista_ordenada:
        print("(sin eventos)")
        return
    for ev in lista_ordenada:
        fecha = ev.get('fecha')
        try:
            fecha_string = fecha.strftime("%d/%m/%Y")
        except Exception:
            fecha_string = "" if fecha is None else str(fecha)
        print(f"- Cliente: {ev.get('cliente')}, Fecha: {fecha_string}, Tipo: {ev.get('tipo')}")
        
def filtrar_eventos_por_fecha(eventos):
    # pedir fecha pieza por pieza para la búsqueda
    while True:
        try:
            dia = int(input("Ingrese día a filtrar (1-31): "))
            while dia <= 0 or dia > 31:
                dia = int(input("Día inválido. Debe estar entre 1 y 31. Ingrese día a filtrar (1-31): "))
            mes = int(input("Ingrese mes a filtrar (1-12): "))
            while mes <= 0 or mes > 12:
                mes = int(input("Mes inválido. Debe estar entre 1 y 12. Ingrese mes a filtrar (1-12): "))
            anio = int(input("Ingrese año a filtrar (debe ser 2025): "))
            while anio != 2025:
                anio = int(input("Año inválido. Debe ser 2025. Ingrese año a filtrar (debe ser 2025): "))
        except ValueError:
            print("Ingrese números enteros válidos para día, mes y año.")
            continue
        try:
            fecha_busqueda = datetime.date(anio, mes, dia)
            fecha_busqueda_str = fecha_busqueda.strftime("%d/%m/%Y")
            break
        except ValueError:
            print("Combinación día/mes/año no corresponde a una fecha real. Intente nuevamente.")

    # comparar por igualdad; los eventos deberían haber sido normalizados en memoria
    eventos_filtrados = [evento for evento in eventos if evento.get('fecha') == fecha_busqueda]

    if eventos_filtrados:
        print(f"\nEventos para la fecha {fecha_busqueda_str}:")
        for e in eventos_filtrados:
            print(f"- Cliente: {e['cliente']}, Tipo: {e['tipo']}")
    else:
        print(f"No hay eventos para la fecha {fecha_busqueda_str}")
        
def abm_eventos(eventos):
    # convertir fechas cargadas (strings) a datetime.date en memoria
    parsear_eventos_date(eventos)

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
                evento_buscar = buscar_evento_por_cliente(eventos, nombre_buscar)
                if evento_buscar:
                    fecha = evento_buscar.get('fecha')
                    try:
                        fecha_string = fecha.strftime("%d/%m/%Y")
                    except Exception:
                        fecha_string = "" if fecha is None else str(fecha)
                    print(f"Evento encontrado: Cliente: {evento_buscar.get('cliente')}, Fecha: {fecha_string}, Tipo: {evento_buscar.get('tipo')}")
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
