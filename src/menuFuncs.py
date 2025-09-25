from typing import List, Tuple
from datetime import date
import pymysql

def createMenu(conn: pymysql.Connection, inputArr:  List[int], tipo: str, 
               numSemana: int, anio: int) -> bool:
   #  Args:
   #      conn: PyMySQL database connection
   #      inputArr: Array of exactly 5 platillo IDs as string "1,2,3,4,5" or list [1,2,3,4,5]
   #      tipo: Menu type ('saludable' or 'economico')
   #      numSemana: Week number (1-53)
   #      anio: Year
   #      fechaInicio: Start date of the menu (Monday)
   #      fechaFin: End date of the menu (Friday)
   #  
   #  Retorna:
   #      bool: True if successful, False if errors occurred
    
    diasSemana = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']
    
    try:
        with conn.cursor() as cursor:
            precioVenta = 300.0 if tipo == 'saludable' else 200.0
            
            # Validar tipo
            if tipo not in ['saludable', 'economico']:
                print(f"Error: Tipo invalido '{tipo}'. Debe de ser 'saludable' o 'economico'")
                return False
            
            # Validar numero de semana
            if numSemana < 1 or numSemana > 53:
                print(f"Error: Numero de semana invalido '{numSemana}'. Debe de ser entre 1 y 53")
                return False
            
            # Validar que todos los elementos sean numericos
            if isinstance(inputArr, list):
                try:
                    platillo_ids = [int(x) for x in inputArr]
                except (ValueError, TypeError):
                    print("Error: inputArr list must contain only integers")
                    return False
            else:
                print("Error: Todos los valores deben de ser numericos")
                return False
            
            # Validar que sean 5 platillos
            if len(platillo_ids) != 5:
                print(f"Error: Platillos insuficientes, deben de ingresarse 5, se ingresaron {len(platillo_ids)}")
                return False
            
            # Validar que el id del platillo sea positivo
            for platillo_id in platillo_ids:
                if platillo_id <= 0:
                    print(f"Error: Platillo ID invalido '{platillo_id}'. debe de ser positivo")
                    return False
                
                # Checar si el platillo existe
                cursor.execute("SELECT 1 FROM platillos WHERE platilloID = %s", (platillo_id,))
                if not cursor.fetchone():
                    print(f"Error: Platillo con ID '{platillo_id}' no existe")
                    return False
            
            # Checar si hay duplicados (mismo tipo, semana, y anio)
            cursor.execute("""
                SELECT 1 FROM menus_semanales 
                WHERE tipoMenu = %s AND numSemana = %s AND anio = %s
            """, (tipo, numSemana, anio))
            
            if cursor.fetchone():
                print(f"Error: Un menu {tipo} para la semana {numSemana} del {anio} ya existe")
                return False
            
            conn.begin()
            
            try:
                cursor.execute("""
                    INSERT INTO menus_semanales 
                    (tipoMenu, numSemana, anio, precioVenta)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (tipo, numSemana, anio, precioVenta))
                
                menuID = cursor.lastrowid
                
                for index, platillo_id in enumerate(platillo_ids):
                    day_of_week = diasSemana[index]
                    
                    cursor.execute("""
                        INSERT INTO menu_platillos (menuSemanalID, platilloID, diaDeSemana)
                        VALUES (%s, %s, %s)
                    """, (menuID, platillo_id, day_of_week))
                
                conn.commit()
                return True
                
            except Exception as e:
                conn.rollback()
                print(f"Error: {str(e)}")
                return False
                
    except Exception as e:
        print(f"Error: {str(e)}")
        return False



# Crear un platillo
# Se puede utilizar un insert simple sin SP
def createPlatillo(conn: pymysql.Connection, nombrePlatillo: str, descPlatillo: str, precioUnitario: float) -> bool:
    try:
        qry = f"INSERT INTO platillos (platilloNombre, platilloDescripcion, CostoUnitario) VALUES ('{nombrePlatillo}','{descPlatillo}',{precioUnitario})"
        with conn.cursor() as cursor:
            cursor.execute(qry)

        conn.commit()
        return True

    except pymysql.MySQLError as e:
        print(f"Connection o query fallo\nError: {e}\nContacte a su administrador de sistemas")
        return False

# Select simple para todos los platillos
def getPlatillos(conn: pymysql.Connection) -> Tuple :
    try:
        with conn.cursor() as c:
            c.execute('SELECT * FROM platillos')
            return c.fetchall()
    except pymysql.MySQLError as e:
        print(f"Connection o query fallo\nError: {e}\nContacte a su administrador de sistemas")
        return (()) # Tupla nula

def getPlatillo(conn: pymysql.Connection, platilloID: int) -> Tuple:
    try:
        with conn.cursor() as c:
            c.execute(f'SELECT * FROM platillos p WHERE p.platilloID = {platilloID}')
            return c.fetchall()
    except pymysql.MySQLError as e:
        print(f"Connection o query fallo\nError: {e}\nContacte a su administrador de sistemas")
        return (()) # Tupla nula

# Select simple para todos los menus
def getMenus(conn: pymysql.Connection):
    try:
        with conn.cursor() as c:
            c.execute('SELECT * FROM menus_semanales')
            return c.fetchall()
    except pymysql.MySQLError as e:
        print(f"Connection o query fallo\nError: {e}\nContacte a su administrador de sistemas")
        return (()) # Tupla nula

# TODO: ADD PLATILLO NAME IN SELECT
def getMenu(conn: pymysql.Connection, numSemana: int):
    try:
        with conn.cursor() as c:
            c.execute(f'SELECT * FROM menus_semanales m WHERE m.numSemana = {numSemana}')
            return c.fetchall()
    except pymysql.MySQLError as e:
        print(f"Connection o query fallo\nError: {e}\nContacte a su administrador de sistemas")
        return (()) # Tupla nula
    pass
