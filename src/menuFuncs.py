from typing import List
import pymysql

# Retornar verdad en caso de que no haya errores (recuerda usar un bloque de try exception)
# Retornar falso en caso de que haya error

# Crear un menu basandose en un array de IDs de platillos
# Usar una SP en SQL
def createMenu(conn: pymysql.Connection, platillosList: List) -> bool:
    pass

# Crear un platillo
# Se puede utilizar un insert simple sin SP
def createPlatillo(conn: pymysql.Connection, nombrePlatillo: str, descPlatillo: str, precioUnitario: float) -> bool:
    pass

# Select simple para todos los platillos
def getPlatillos(conn: pymysql.Connection):
    pass

# Select simple para todos los menus
def getMenus(conn: pymysql.Connection):
    pass
