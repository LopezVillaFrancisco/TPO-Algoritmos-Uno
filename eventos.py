from persistencia import guardar_eventos


def mostrar_empleados_disponibles(empleados):
    """Muestra la lista de empleados disponibles con nombre y DNI."""
    print("\n--- Empleados Disponibles ---")
    if len(empleados) == 0:
        print("No hay empleados registrados.")
        return
    
    # Recorrer empleados y mostrar cada uno
    for empleado in empleados:
        try:
            # Acceso directo que falla si faltan campos requeridos
            nombre = empleado['nombre']
            dni = empleado['dni']
            print(f"- {nombre} (DNI: {dni})")
        except KeyError as e:
            # Si falta un campo requerido, mostrar error específico
            print(f"Error: Empleado con datos incompletos (falta campo {e})")
        except (ValueError, TypeError) as e:
            # Si hay error de tipo o valor, continuar con siguiente empleado
            print(f"Error: Datos inválidos en empleado - {e}")

def seleccionar_encargado(empleados):
    """Permite seleccionar un encargado por nombre o DNI.
    
    Retorna un diccionario con {nombre, dni} del encargado seleccionado.
    Retorna None si no hay empleados o si hay error crítico.
    """
    try:
        # Verificar que hay empleados disponibles
        if len(empleados) == 0:
            print("Error: No hay empleados disponibles para asignar.")
            return None
        
        # Mostrar lista de empleados disponibles
        mostrar_empleados_disponibles(empleados)
        
        # Solicitar criterio de búsqueda
        criterio = input("\nIngrese nombre o DNI del encargado: ").strip()
        
        # Validar que no esté vacío
        if criterio == "":
            print("Error: Debe ingresar un nombre o DNI.")
            return None
        
        # Normalizar para búsqueda case-insensitive
        criterio_lower = criterio.lower()
        
        # Buscar por nombre o DNI
        for empleado in empleados:
            try:
                # Acceso directo a campos requeridos
                nombre = empleado['nombre']
                dni = str(empleado['dni'])
                
                # Comparar con criterio ingresado
                if nombre.lower() == criterio_lower or dni == criterio:
                    print(f"✓ Encargado seleccionado: {nombre} (DNI: {dni})")
                    return {'nombre': nombre, 'dni': dni}
                    
            except KeyError as e:
                # Si un empleado no tiene los campos requeridos, saltar al siguiente
                print(f"Advertencia: Empleado con datos incompletos (falta campo {e}), se omite.")
                continue
            except (ValueError, TypeError) as e:
                # Error de tipo o conversión, continuar con siguiente empleado
                print(f"Advertencia: Error en datos de empleado - {e}")
                continue
        
        # Si llegamos aquí, no se encontró el empleado
        print(f"Error: No se encontró empleado con nombre o DNI: {criterio}")
        return None
        
    except (ValueError, IndexError, TypeError) as e:
        # Capturar cualquier otro error inesperado
        print(f"Error al seleccionar encargado: {e}")
        return None


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
    try:
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
        print(f"Encargado asignado: {encargado['nombre']} (DNI: {encargado['dni']})")
        
        # Guardar en persistencia
        guardar_eventos(eventos)
        
    except KeyError as e:
        # Error al acceder a campo del encargado
        print(f"Error: Datos incompletos del encargado (falta campo {e})")
    except (ValueError, IndexError, TypeError) as e:
        # Otros errores durante la creación del evento
        print(f"Error al crear el evento: {e}")


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
    try:
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
                    try:
                        print("\n--- Cambio de Encargado ---")
                        nuevo_encargado = seleccionar_encargado(empleados)
                        
                        # Si se seleccionó un nuevo encargado, actualizarlo
                        if nuevo_encargado == None:
                            print("No se cambió el encargado.")
                        else:
                            evento.update({"encargado": nuevo_encargado})
                            print(f"Encargado actualizado: {nuevo_encargado['nombre']} (DNI: {nuevo_encargado['dni']})")
                    
                    except KeyError as e:
                        # Error al acceder a campo del nuevo encargado
                        print(f"Error: Datos incompletos del encargado (falta campo {e})")
                        print("No se cambió el encargado.")
                    except (ValueError, TypeError) as e:
                        # Error en la selección del encargado
                        print(f"Error al cambiar encargado: {e}")
                        print("No se cambió el encargado.")
                
                # Guardar cambios
                print("Evento modificado exitosamente.")
                guardar_eventos(eventos)
                return

        print("Evento no encontrado.")
        
    except (ValueError, IndexError, TypeError) as e:
        # Error general durante la modificación
        print(f"Error al modificar el evento: {e}")


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
