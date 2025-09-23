import pymysql
import sys

def createConn() -> pymysql.Connection:
    try:
        conn = pymysql.connect(
            host='localhost',
            user='admin',
            password='257Hj986$',
            database='db'
        )
        return conn
    except pymysql.MySQLError as e:
        print(f"Error durante la conexion a la DB\nError: {e}\nContacte a su administrador de sistemas")
        sys.exit(1)
