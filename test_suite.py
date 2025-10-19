import unittest

from empleados import (
    alta_empleado,
    listar_empleados,
    buscar_por_nombre,
    listar_empleados_ordenado,
)
from servicios import (
    alta_servicio,
    listar_servicios,
    buscar_servicio_por_nombre,
    listar_servicios_ordenado,
)
from eventos import (
    alta_evento,
    listar_eventos,
    buscar_evento_por_cliente,
    listar_eventos_ordenado,
)

class TestABM(unittest.TestCase):
    def test_empleados_buscar_y_listar(self):
        lista = []
        # no usamos alta_empleado porque pide input; creamos manualmente
        lista.append({'nombre':'Carlos','dni':'10','tarea':'A'})
        lista.append({'nombre':'Ana','dni':'2','tarea':'B'})
        encontrado = buscar_por_nombre(lista, 'Ana')
        self.assertIsNotNone(encontrado)
        # comprobar ordenado (alfabético)
        listar_empleados_ordenado(lista)  # no assert, solo que no falle

    def test_servicios_buscar_y_listar(self):
        lista = []
        lista.append({'nombre':'Lavado','descripcion':'Limpieza','costo':50})
        lista.append({'nombre':'Corte','descripcion':'Pelo','costo':30})
        encontrado = buscar_servicio_por_nombre(lista, 'Corte')
        self.assertIsNotNone(encontrado)
        listar_servicios_ordenado(lista)

    def test_eventos_buscar_y_listar(self):
        lista = []
        lista.append({'cliente':'Zoe','fecha':'01/01/2025','tipo':'Boda'})
        lista.append({'cliente':'Alfa','fecha':'02/02/2025','tipo':'Cumple'})
        encontrado = buscar_evento_por_cliente(lista, 'Zoe')
        self.assertIsNotNone(encontrado)
        listar_eventos_ordenado(lista)

if __name__ == '__main__':
    unittest.main()
