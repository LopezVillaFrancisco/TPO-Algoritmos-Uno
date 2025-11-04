import json

ARCHIVO_SERVICIOS = "servicios.json"
ARCHIVO_EMPLEADOS = "empleados.json"
ARCHIVO_EVENTOS = "eventos.json"


def cargar_datos(nombre_archivo):
    """Carga datos desde un archivo JSON. Si no existe, retorna lista vacía"""
    try:
        archivo = open(nombre_archivo, 'r', encoding='utf-8')
        datos = json.load(archivo)
        archivo.close()
        return datos
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Error al leer {nombre_archivo}. Se iniciará con lista vacía.")
        return []
    except Exception as e:
        print(f"Error inesperado al cargar {nombre_archivo}: {e}")
        return []


def guardar_datos(nombre_archivo, datos):
    """Guarda datos en un archivo JSON"""
    try:
        archivo = open(nombre_archivo, 'w', encoding='utf-8')
        json.dump(datos, archivo, ensure_ascii=False, indent=4)
        archivo.close()
        print(f"Datos guardados en {nombre_archivo}")
        return True
    except Exception as e:
        print(f"Error al guardar en {nombre_archivo}: {e}")
        return False


def cargar_servicios():
    """Carga la lista de servicios desde el archivo JSON"""
    return cargar_datos(ARCHIVO_SERVICIOS)


def guardar_servicios(servicios):
    """Guarda la lista de servicios en el archivo JSON"""
    return guardar_datos(ARCHIVO_SERVICIOS, servicios)


def cargar_empleados():
    """Carga la lista de empleados desde el archivo JSON"""
    return cargar_datos(ARCHIVO_EMPLEADOS)


def guardar_empleados(empleados):
    """Guarda la lista de empleados en el archivo JSON"""
    return guardar_datos(ARCHIVO_EMPLEADOS, empleados)


def cargar_eventos():
    """Carga la lista de eventos desde el archivo JSON"""
    return cargar_datos(ARCHIVO_EVENTOS)


def guardar_eventos(eventos):
    """Guarda la lista de eventos en el archivo JSON"""
    return guardar_datos(ARCHIVO_EVENTOS, eventos)
