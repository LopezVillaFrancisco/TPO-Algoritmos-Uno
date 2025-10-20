
from servicios import abm_servicios
from empleados import abm_empleados
from eventos import abm_eventos

def mostrar_menu():
    print("Menú Principal")
    print("1. ABM Servicios")
    print("2. ABM Empleados/Encargados")
    print("3. Modelo de Evento")
    print("0. Salir")



def main():
    servicios = []  # Lista para almacenar los servicios en memoria
    empleados = []  # Lista para almacenar los empleados/encargados en memoria
    eventos = []    # Lista para almacenar los eventos en memoria
    
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
                abm_eventos(eventos)
            elif opcion == "0":
                print("Saliendo...")
            else:
                print("Opción inválida. Intente de nuevo.")
        except (ValueError, IndexError, TypeError):
            print("Error en el menú principal. Intente nuevamente.")

main()