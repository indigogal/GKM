from typing import Tuple
import pymysql

def createOrden(conn: pymysql.Connection, clienteID: int, qtySaludable: int, qtyEcon: int) -> bool:
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
    try:
        cursor = conn.cursor()
        cursor.callproc('crearOrden', [clienteID, qtySaludable, qtyEcon])
        conn.commit()
        print("Orden creada correctamente.")
        return True

    except pymysql.err.InternalError as e:
        print(f"Error al crear la orden: {e}")
        return False

def getAllOrdenes(conn: pymysql.Connection) -> Tuple:
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM ordenes')
        return cursor.fetchall()

def getOrdenesFromUser(conn: pymysql.Connection, userID: int) -> Tuple:
    with conn.cursor() as cursor:
        cursor.execute(f'SELECT * FROM ordenes o INNER JOIN clientes c ON o.clienteID = c.clienteID WHERE o.clienteID = {userID}')
        return cursor.fetchall()

# Usar SP para validar que orden no este en proceso
# si esta en proceso retornar falso
# else retornar verdad
# def cancelOrden(conn: pymysql.Connection,_OrderID: int) -> bool:
#     try:
#         cursor=conn.cursor()
#         cursor.callproc('cancelarOrden',[clienteID])
#         conn.commit()
#         print("Haz eliminado la orden correctamente.")
#         return True
#     
#     except pymysql.err.InternalError as e:
#         print(f"Error al cancelar la orden: {e}")
#         return False
