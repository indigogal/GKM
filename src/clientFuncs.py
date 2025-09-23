import pymysql

def deleteCliente(conn: pymysql.Connection, clienteID: int) -> bool:
    # Descripcion del SP
    # 1. Asignar todas las ordenes del usuario al "Cliente default"
    #    el cual sera un cliente creado para mantener historial de las ordenes
    #    creadas por clientes que no desean estar en nuestra base de datos despues de
    #    terminar su negocio con nosotros
    # 2. Borrar Direccion y Usuario
    pass

def addCliente(conn: pymysql.Connection) -> bool:
    # usar SP que creo alonso
    pass

def updateCliente(conn: pymysql.Connection, clienteID: int) -> bool:
    pass

def getClientes(conn: pymysql.Connection):
    pass
