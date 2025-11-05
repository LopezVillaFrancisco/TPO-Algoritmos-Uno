from persistencia import guardar_eventos


def mostrar_empleados_disponibles(empleados):
    """Muestra lista de empleados disponibles con nombre y DNI"""
    if empleados == []:
        # Si la lista está vacía, mostrar mensaje
        print("\nNo hay empleados registrados.")
        return
    print("\n--- Empleados Disponibles ---")
    # Recorrer la lista de empleados y mostrar cada uno
    for empleado in empleados:
        nombre = empleado.get('nombre', 'Sin nombre')
        dni = empleado.get('dni', 'Sin DNI')
        print(f"- {nombre} (DNI: {dni})")


def seleccionar_encargado(empleados):
    """Permite seleccionar un encargado por nombre o DNI con validación robusta.
    
    Retorna un diccionario con formato {'nombre': str, 'dni': str} o None si falla.
    """
    # Mostrar empleados disponibles primero
    mostrar_empleados_disponibles(empleados)
    
    # Si no hay empleados, retornar None
    if empleados == []:
        return None
    
    # Intentar seleccionar hasta que sea válido
    while True:
        try:
            # Pedir identificador del encargado
            identificador = input("\nIngrese nombre o DNI del encargado: ")
            # Limpiar espacios y convertir a minúsculas para comparación
            identificador_limpio = identificador.strip().lower()
            
            # Validar que no esté vacío
            if identificador_limpio == "" or identificador_limpio == ' ':
                print("El identificador no puede estar vacío. Intente nuevamente.")
                continue
            
            # Buscar empleado por nombre o DNI
            encargado_encontrado = None
            for empleado in empleados:
                # Obtener nombre y DNI del empleado
                nombre_empleado = empleado.get('nombre', '').strip().lower()
                dni_empleado = empleado.get('dni', '').strip().lower()
                
                # Comparar con el identificador ingresado
                if nombre_empleado == identificador_limpio or dni_empleado == identificador_limpio:
                    encargado_encontrado = empleado
                    break
            
            # Validar si se encontró el empleado
            if encargado_encontrado == None:
                print("Empleado no encontrado. Verifique el nombre o DNI e intente nuevamente.")
                # Preguntar si quiere reintentar
                reintentar = input("¿Desea intentar nuevamente? (s/n): ").strip().lower()
                if reintentar == 's' or reintentar == 'si':
                    continue
                else:
                    return None
            
            # Retornar diccionario con nombre y DNI del encargado
            return {
                "nombre": encargado_encontrado.get('nombre'),
                "dni": encargado_encontrado.get('dni')
            }
            
        except (ValueError, IndexError, TypeError):
            print("Error al seleccionar encargado. Intente nuevamente.")
            continue


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


def alta_evento(eventos, empleados):
    """Pide datos por consola y agrega un evento a la lista con encargado asignado"""
    # Solicitar datos del cliente
    cliente = input("Ingrese nombre del cliente: ").strip()
    while cliente == "":
        cliente = input("El nombre del cliente no puede estar vacío. Ingrese nombre del cliente: ").strip()

    # Solicitar fecha del evento
    fecha = input("Ingrese fecha (DD/MM/AAAA): ").strip()
    while fecha == "":
        fecha = input("La fecha no puede estar vacía. Ingrese fecha (DD/MM/AAAA): ").strip()

    # Solicitar tipo de evento
    tipo = input("Ingrese tipo de evento: ").strip()
    while tipo == "":
        tipo = input("El tipo de evento no puede estar vacío. Ingrese tipo de evento: ").strip()

    # Seleccionar encargado del evento
    print("\n--- Asignación de Encargado ---")
    encargado = seleccionar_encargado(empleados)
    
    # Validar que se haya seleccionado un encargado
    if encargado == None:
        print("No se pudo asignar un encargado. El evento no será creado.")
        return
    
    # Crear diccionario del evento con todos los campos
    evento = {"cliente": cliente, "fecha": fecha, "tipo": tipo, "encargado": encargado}
    
    # Agregar evento a la lista
    eventos.append(evento)
    print("Evento agregado exitosamente.")
    print(f"Encargado asignado: {encargado.get('nombre')} (DNI: {encargado.get('dni')})")
    
    # Guardar en persistencia
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


def modificar_evento(eventos, empleados):
    """Modifica los datos de un evento identificado por cliente, incluyendo encargado"""
    # Solicitar nombre del cliente del evento a modificar
    cliente = input("Ingrese nombre del evento a modificar: ").strip()
    while cliente == "":
        cliente = input("El nombre del cliente no puede estar vacío. Ingrese nombre del evento a modificar: ").strip()

    # Buscar el evento por nombre de cliente
    objetivo = cliente.lower()
    for evento in eventos:
        if evento.get('cliente', '').strip().lower() == objetivo:
            # Solicitar nuevo nombre del cliente
            nuevo_cliente = input("Nuevo nombre del cliente: ").strip()
            while nuevo_cliente == "":
                nuevo_cliente = input("El nombre del cliente no puede estar vacío. Ingrese nuevo nombre del cliente: ").strip()

            # Solicitar nueva fecha
            nueva_fecha = input("Nueva fecha (DD/MM/AAAA): ").strip()
            while nueva_fecha == "":
                nueva_fecha = input("La fecha no puede estar vacía. Ingrese nueva fecha (DD/MM/AAAA): ").strip()

            # Solicitar nuevo tipo de evento
            nuevo_tipo = input("Nuevo tipo de evento: ").strip()
            while nuevo_tipo == "":
                nuevo_tipo = input("El tipo de evento no puede estar vacío. Ingrese nuevo tipo de evento: ").strip()

            # Preguntar si desea cambiar el encargado
            cambiar_encargado = input("¿Desea cambiar el encargado del evento? (s/n): ").strip().lower()
            
            # Actualizar datos básicos del evento
            evento.update({"cliente": nuevo_cliente, "fecha": nueva_fecha, "tipo": nuevo_tipo})
            
            # Si el usuario quiere cambiar el encargado
            if cambiar_encargado == 's' or cambiar_encargado == 'si':
                print("\n--- Cambio de Encargado ---")
                nuevo_encargado = seleccionar_encargado(empleados)
                
                # Si se seleccionó un nuevo encargado, actualizarlo
                if nuevo_encargado == None:
                    print("No se cambió el encargado.")
                else:
                    evento.update({"encargado": nuevo_encargado})
                    print(f"Encargado actualizado: {nuevo_encargado.get('nombre')} (DNI: {nuevo_encargado.get('dni')})")
            
            # Guardar cambios
            print("Evento modificado exitosamente.")
            guardar_eventos(eventos)
            return

    print("Evento no encontrado.")


def listar_eventos(eventos):
    """Imprime la lista de eventos incluyendo encargado si existe"""
    print("\nLista de Eventos:")
    # Validar si hay eventos
    if eventos == []:
        print("(sin eventos)")
        return
    
    # Recorrer eventos y mostrar información
    for ev in eventos:
        # Obtener datos básicos del evento
        cliente = ev.get('cliente', 'Sin cliente')
        fecha = ev.get('fecha', 'Sin fecha')
        tipo = ev.get('tipo', 'Sin tipo')
        
        # Obtener encargado si existe (compatibilidad con eventos viejos)
        encargado = ev.get('encargado', None)
        
        # Construir línea de información
        if encargado == None:
            # Evento sin encargado asignado
            linea = f"- Cliente: {cliente}, Fecha: {fecha}, Tipo: {tipo}, Encargado: (sin asignar)"
        else:
            # Evento con encargado asignado
            nombre_encargado = encargado.get('nombre', 'Sin nombre')
            dni_encargado = encargado.get('dni', 'Sin DNI')
            linea = f"- Cliente: {cliente}, Fecha: {fecha}, Tipo: {tipo}, Encargado: {nombre_encargado} (DNI: {dni_encargado})"
        
        # Imprimir línea
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
    """Imprime los eventos ordenados por cliente incluyendo encargado si existe"""
    # Ordenar eventos alfabéticamente por cliente
    lista_ordenada = sorted(lista_eventos, key=FUNCIONES_ORDEN_EVENTOS['cliente'])
    print("\nEventos ordenados por cliente:")
    
    # Validar si hay eventos
    if lista_ordenada == []:
        print("(sin eventos)")
        return
    
    # Recorrer eventos ordenados y mostrar información
    for ev in lista_ordenada:
        # Obtener datos básicos del evento
        cliente = ev.get('cliente', 'Sin cliente')
        fecha = ev.get('fecha', 'Sin fecha')
        tipo = ev.get('tipo', 'Sin tipo')
        
        # Obtener encargado si existe (compatibilidad con eventos viejos)
        encargado = ev.get('encargado', None)
        
        # Construir línea de información
        if encargado == None:
            # Evento sin encargado asignado
            linea = f"- Cliente: {cliente}, Fecha: {fecha}, Tipo: {tipo}, Encargado: (sin asignar)"
        else:
            # Evento con encargado asignado
            nombre_encargado = encargado.get('nombre', 'Sin nombre')
            dni_encargado = encargado.get('dni', 'Sin DNI')
            linea = f"- Cliente: {cliente}, Fecha: {fecha}, Tipo: {tipo}, Encargado: {nombre_encargado} (DNI: {dni_encargado})"
        
        # Imprimir línea
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
        
def abm_eventos(eventos, empleados):
    """Bucle principal del ABM de eventos, recibe empleados para asignar encargados"""
    opcion = ''
    while opcion != "0":
        try:
            mostrar_menu_eventos()
            opcion = input("Seleccione una opción: ").strip()
            if opcion == "1":
                # Pasar empleados para asignar encargado en alta
                alta_evento(eventos, empleados)
            elif opcion == "2":
                baja_evento(eventos)
            elif opcion == "3":
                # Pasar empleados para cambiar encargado en modificación
                modificar_evento(eventos, empleados)
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
