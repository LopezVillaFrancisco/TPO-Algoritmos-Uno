# Gestión de Servicios, Empleados y Eventos (CLI en Python)

Aplicación de consola para administrar **Servicios**, **Empleados/Encargados** y **Eventos** mediante un menú interactivo.  
Pensada como práctica para **Algoritmos y Estructuras de Datos I**, con toda la información almacenada **en Json** y utilizando únicamente Python estándar.

---

## ✦ Uso rápido
1. Ejecutá `index.py` para acceder al **Menú Principal**.  
2. Elegí entre:
   - **ABM de Servicios**
   - **ABM de Empleados/Encargados**
   - **ABM de Eventos**
3. Cada módulo ofrece **alta**, **baja**, **modificación** y **listado**.  
4. Los datos solo existen mientras el programa está en ejecución.  
5. Para los eventos, ingresá la fecha en formato `DD/MM/AAAA` para superar la validación mínima.

---

## ✦ Estructura del proyecto
- `index.py` → Punto de entrada; muestra el menú y deriva a los módulos.  
- `servicios.py` → Operaciones de ABM para servicios.  
- `empleados.py` → ABM para empleados/encargados.  
- `eventos.py` → ABM de eventos y validación de formatos de fecha.

---

## ✦ Autores
- **Franco Pipito**  
- **Francisco Lopez Villa**  
- **Santiago Elcano**
