def mostrar_menu_servicios():
	print("\n--- ABM Servicios ---")
	print("1. Alta de Servicio")
	print("2. Baja de Servicio")
	print("3. Modificar Servicio")
	print("4. Listar Servicios")
	print("0. Volver al menú principal")

def alta_servicio(servicios):
	nombre = input("Ingrese nombre del servicio: ")
	servicios.append(nombre)
	print("Servicio agregado.")

def baja_servicio(servicios):
	nombre = input("Ingrese nombre del servicio a eliminar: ")
	if nombre in servicios:
		servicios.remove(nombre)
		print("Servicio eliminado.")
	else:
		print("Servicio no encontrado.")

def modificar_servicio(servicios):
	nombre = input("Ingrese nombre del servicio a modificar: ")
	if nombre in servicios:
		nuevo_nombre = input("Ingrese el nuevo nombre: ")
		idx = servicios.index(nombre)
		servicios[idx] = nuevo_nombre
		print("Servicio modificado.")
	else:
		print("Servicio no encontrado.")

def listar_servicios(servicios):
	print("\nLista de Servicios:")
	for s in servicios:
		print("-", s)

def abm_servicios(servicios):
	while True:
		mostrar_menu_servicios()
		opcion = input("Seleccione una opción: ")
		if opcion == "1":
			alta_servicio(servicios)
		elif opcion == "2":
			baja_servicio(servicios)
		elif opcion == "3":
			modificar_servicio(servicios)
		elif opcion == "4":
			listar_servicios(servicios)
		elif opcion == "0":
			break
		else:
			print("Opción inválida.")
