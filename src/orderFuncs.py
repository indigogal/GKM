import pymysql

def createOrden(conn: pymysql.Connection, clienteID: int, qtySaludable: int, qtyEcon: int, Fecha: str) -> bool:
    # Descripcion de la SP a llamar
    # 1. Validar valores, tirar excepcion si las dos qtys son 0
    # 2. crear orden con los parametros pasados mas los siguientes parametros calculados
    #   - precioTotal = (qtyEcon * 200) + (qtySaludable * 300)
    #   - enCurso = False
    #   - fechaApartado = current date
    #   - numSemana = semana actual + 1
    #   - year = current year
    # 3. crear detalle de orden acorde a los menus pedidos
    #   - si qtySaludable = 0 no solo crear 1 detalle para orden qtyEcon y viceversa
    #   - si hay qty de los dos crear dos detalles
    #   - enlazar detalle al menu semanal mediante el numero de semana en el menu semanal y en la orden
    pass

def getAllOrdenes():
    pass

# Usar SP para validar que orden no este en proceso
# si esta en proceso retornar falso
# else retornar verdad
def cancelOrden(_OrderID: int) -> bool:
    pass
