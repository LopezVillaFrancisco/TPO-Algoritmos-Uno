from servicios import abm_servicios
from empleados import abm_empleados
from eventos import abm_eventos
from persistencia import (cargar_servicios,cargar_empleados,cargar_eventos,)


def mostrar_menu():
    print("\n=== Menú Principal ===")
    print("1. ABM Servicios")
    print("2. ABM Empleados/Encargados")
    print("3. ABM de Eventos")
    print("0. Salir")


def main():
    servicios = cargar_servicios()
    empleados = cargar_empleados()
    eventos = cargar_eventos()
    
    opcion = ''
    while opcion != "0":
        try:
            mostrar_menu()
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                abm_servicios(servicios)
            elif opcion == "2":
                abm_empleados(empleados)
            elif opcion == "3":
                # Pasar empleados a abm_eventos para asignar encargados
                abm_eventos(eventos, empleados, servicios)
            elif opcion == "0":
                print("Saliendo...")
            else:
                print("Opción inválida. Intente de nuevo.")
        except (ValueError, IndexError, TypeError):
            print("Error en el menú principal. Intente nuevamente.")

main()