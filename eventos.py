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


def filtrar_encargados(empleados):
    # Filtra empleados cuya tarea contenga 'encargado'.
    
    encargados = []
    for empleado in empleados:
        try:
            # Obtener el campo tarea y normalizar a minúsculas
            tarea = empleado['tarea'].lower()
            # Verificar si contiene la palabra 'encargado'
            if 'encargado' in tarea:
                encargados.append(empleado)
        except KeyError:
            # Si falta el campo 'tarea', omitir este empleado
            continue
        except (ValueError, TypeError):
            # Si hay error al procesar la tarea, omitir
            continue
    return encargados


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
    
    Filtra solo empleados con rol de 'Encargado' en su tarea.
    Retorna un diccionario con {nombre, dni} del encargado seleccionado.
    Retorna None si no hay encargados disponibles o si hay error.
    """
    try:
        # Filtrar solo empleados que sean encargados
        encargados = filtrar_encargados(empleados)
        
        # Verificar que haya encargados disponibles
        if len(encargados) == 0:
            print("Error: No hay empleados con rol de 'Encargado' disponibles.")
            print("Sugerencia: Verifique que el campo 'tarea' contenga la palabra 'Encargado'.")
            return None
        
        # Mostrar lista de encargados disponibles
        mostrar_empleados_disponibles(encargados)
        
        # Solicitar criterio de búsqueda
        criterio = input("\nIngrese nombre o DNI del encargado: ").strip()
        
        # Validar que no esté vacío
        if criterio == "":
            print("Error: Debe ingresar un nombre o DNI.")
            return None
        
        # Normalizar para búsqueda case-insensitive
        criterio_lower = criterio.lower()
        
        # Buscar por nombre o DNI en la lista de encargados
        for encargado in encargados:
            try:
                # Acceso directo a campos requeridos
                nombre = encargado['nombre']
                dni = str(encargado['dni'])
                
                # Comparar con criterio ingresado (búsqueda parcial tolerante a tildes)
                if criterio_lower in nombre.lower() or dni == criterio:
                    print(f"✓ Encargado seleccionado: {nombre} (DNI: {dni})")
                    return {'nombre': nombre, 'dni': dni}
                    
            except KeyError as e:
                # Si un encargado no tiene los campos requeridos, saltar al siguiente
                print(f"Advertencia: Encargado con datos incompletos (falta campo {e}), se omite.")
                continue
            except (ValueError, TypeError) as e:
                # Error de tipo o conversión, continuar con siguiente encargado
                print(f"Advertencia: Error en datos de encargado - {e}")
                continue
        
        print(f"Error: No se encontró encargado con nombre o DNI: {criterio}")
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
    print("8. Calcular costo total y registrar seña")
    print("0. Volver al menú principal")


def alta_evento(eventos, empleados):
    """Pide datos por consola y agrega un evento a la lista (fecha -> datetime.date)"""
    try:
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
        guardar_eventos(parsear_eventos_JSON(eventos))
        
    except KeyError as e:
        # Error al acceder a campo del encargado
        print(f"Error: Datos incompletos del encargado (falta campo {e})")
    except (ValueError, IndexError, TypeError) as e:
        # Otros errores durante la creación del evento
        print(f"Error al crear el evento: {e}")

def baja_evento(eventos):
    """Elimina un evento por cliente si existe"""
    cliente = input("Ingrese el nombre del cliente que organiza el evento a eliminar: ").strip()
    while cliente == "":
        cliente = input("El nombre del cliente no puede estar vacío. Ingrese el nombre del cliente que organiza el evento a eliminar: ").strip()

    cliente_objetivo = cliente.lower()
    for evento in list(eventos):
        if evento.get('cliente', '').strip().lower() == cliente_objetivo:
            eventos.remove(evento)
            print("Evento eliminado.")
            guardar_eventos(parsear_eventos_JSON(eventos))
            return
    print("Evento no encontrado.")


def modificar_evento(eventos, empleados):
    """Modifica los datos de un evento identificado por cliente, incluyendo encargado"""
    # Solicitar nombre del cliente del evento a modificar
    cliente = input("Ingrese nombre del cliente que organiza el evento a modificar: ").strip()
    while cliente == "":
        cliente = input("El nombre del cliente no puede estar vacío. Ingrese nombre del cliente que organiza el evento a modificar: ").strip()

    cliente_objetivo = cliente.lower()
    for evento in eventos:
        if evento.get('cliente', '').strip().lower() == cliente_objetivo:
            nuevo_cliente = input("Nuevo nombre del cliente: ").strip()
            while nuevo_cliente == "":
                nuevo_cliente = input("El nombre del cliente no puede estar vacío. Ingrese nuevo nombre del cliente: ").strip()

            # pedir nueva fecha y convertir a datetime.date
            nueva_fecha = None
            while nueva_fecha is None:
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
                    
                    nueva_fecha = datetime.date(anio, mes, dia)
                    
                    # validar que no exista ya un evento para esa fecha (excluyendo el evento actual)
                    # versión simplificada sin usar "is not"
                    existe_mismo_dia = False
                    for evento_existente in eventos:
                        # solo verificar si es otro evento (comparando cliente para identificarlo)
                        if evento_existente.get('cliente') != evento.get('cliente'):
                            if evento_existente.get("fecha") == nueva_fecha:
                                existe_mismo_dia = True
                    
                    if existe_mismo_dia:
                        print("Ya existe un evento para esa fecha. Elija otra fecha.")
                        nueva_fecha = None
                        
                except ValueError:
                    print("Ingrese números enteros válidos o una combinación de fecha real.")

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
            guardar_eventos(parsear_eventos_JSON(eventos))
            return

    print("Evento no encontrado.")


def listar_eventos(eventos):
    """Imprime la lista de eventos incluyendo encargado si existe"""
    print("\nLista de Eventos:")
    # Validar si hay eventos
    if eventos == []:
        print("(sin eventos)")
        return
    lineas = []
    for evento in eventos:
        fecha = evento.get('fecha')
        try:
            fecha_string = fecha.strftime("%d/%m/%Y")
        except Exception:
            fecha_string = "" if fecha is None else str(fecha)
        
        # Construir línea base con datos del evento
        linea = f"- Cliente: {evento.get('cliente')}, Fecha: {fecha_string}, Tipo: {evento.get('tipo')}"
        
        # Agregar encargado si existe
        encargado = evento.get('encargado')
        if encargado:
            try:
                nombre_enc = encargado.get('nombre', 'N/A')
                dni_enc = encargado.get('dni', 'N/A')
                linea += f", Encargado: {nombre_enc} (DNI: {dni_enc})"
            except Exception:
                linea += ", Encargado: (datos inválidos)"
        
        lineas.append(linea)
    
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
    """Imprime los eventos ordenados por cliente incluyendo encargado si existe"""
    # Ordenar eventos alfabéticamente por cliente
    lista_ordenada = sorted(lista_eventos, key=FUNCIONES_ORDEN_EVENTOS['cliente'])
    print("\nEventos ordenados por cliente:")
    
    # Validar si hay eventos
    if lista_ordenada == []:
        print("(sin eventos)")
        return
    
    for ev in lista_eventos:
        fecha = ev.get('fecha')
        try:
            fecha_string = fecha.strftime("%d/%m/%Y")
        except Exception:
            fecha_string = "" if fecha is None else str(fecha)
        
        # Construir línea base con datos del evento
        linea = f"- Cliente: {ev.get('cliente')}, Fecha: {fecha_string}, Tipo: {ev.get('tipo')}"
        
        # Agregar encargado si existe
        encargado = ev.get('encargado')
        if encargado:
            try:
                nombre_enc = encargado.get('nombre', 'N/A')
                dni_enc = encargado.get('dni', 'N/A')
                linea += f", Encargado: {nombre_enc} (DNI: {dni_enc})"
            except Exception:
                linea += ", Encargado: (datos inválidos)"
        
        print(linea)
        
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
        
def calcular_costo_y_registrar_sena(eventos, servicios):
    #Calcula el costo total de un evento y permite registrar una seña
    try:
        cliente = input("Ingrese el nombre del cliente del evento: ").strip()
        while cliente == "":
            cliente = input("El nombre del cliente no puede estar vacío. Ingrese el nombre del cliente: ").strip()
        
        evento = buscar_evento_por_cliente(eventos, cliente)
        if not evento:
            print("Evento no encontrado.")
            return
        
        print(f"\nEvento encontrado: {evento.get('cliente')} - {evento.get('tipo')}")
        
        # Mostrar servicios disponibles
        print("\n--- Servicios Disponibles ---")
        for i, servicio in enumerate(servicios, 1):
            print(f"{i}. {servicio.get('nombre')} - ${servicio.get('costo'):.2f}")
        
        # Seleccionar servicios
        servicios_contratados = []
        costo_total = 0.0
        
        while True:
            try:
                opcion = input("\nIngrese el número del servicio a agregar (0 para terminar): ").strip()
                if opcion == "0":
                    break
                
                indice = int(opcion) - 1
                if 0 <= indice < len(servicios):
                    servicio_seleccionado = servicios[indice]
                    servicios_contratados.append(servicio_seleccionado)
                    costo_total += servicio_seleccionado.get('costo', 0.0)
                    print(f"Servicio '{servicio_seleccionado.get('nombre')}' agregado. Costo parcial: ${costo_total:.2f}")
                else:
                    print("Número de servicio inválido.")
            except ValueError:
                print("Ingrese un número válido.")
        
        # Registrar seña
        sena = 0.0
        if costo_total > 0:
            try:
                sena_input = input(f"\nCosto total del evento: ${costo_total:.2f}. Ingrese monto de la seña (0 para no registrar seña): $").strip()
                sena = float(sena_input) if sena_input else 0.0
                
                if sena < 0:
                    print("La seña no puede ser negativa. Se establecerá en 0.")
                    sena = 0.0
                elif sena > costo_total:
                    print("La seña no puede ser mayor al costo total. Se establecerá en el costo total.")
                    sena = costo_total
                
            except ValueError:
                print("Monto inválido. No se registrará seña.")
                sena = 0.0
        
        # Actualizar evento
        evento['costo_total'] = costo_total
        evento['sena'] = sena
        evento['servicios_contratados'] = servicios_contratados
        
        print(f"\n✓ Evento actualizado:")
        print(f"   - Costo total: ${costo_total:.2f}")
        print(f"   - Seña registrada: ${sena:.2f}")
        if sena > 0:
            saldo_pendiente = costo_total - sena
            print(f"   - Saldo pendiente: ${saldo_pendiente:.2f}")
        
        guardar_eventos(parsear_eventos_JSON(eventos))
        
    except (ValueError, IndexError, TypeError) as e:
        print(f"Error al calcular costo y registrar seña: {e}")
        
def abm_eventos(eventos, empleados, servicios):
    # convertir fechas cargadas (strings) a datetime.date en memoria
    parsear_eventos_date(eventos)

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
                nombre_buscar = input("Ingrese el nombre del cliente a buscar: ")
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
            elif opcion == "8": 
                if servicios is None: 
                    print("Error: No se han cargado los servicios.")
                else:
                    calcular_costo_y_registrar_sena(eventos, servicios)
            elif opcion == "0":
                break
            else:
                print("Opción inválida.")
        except (ValueError, IndexError, TypeError):
            print("Error en el menú de eventos. Intente nuevamente.")
