import pymysql
import sys

'''
LEAN ESTA EXPLICACION

Si bien recuerdan plebes python es un lenguage de tipos dinamicos,
es decir no te pide de ahuevo que declares el tipo de un dato al declarar una
variable, esto nos trae problemas al estar manejando los datos retornados por
las funciones del programa y por los queries SQL.

A lo largo de la siguiente explicacion van a ver algo que
se llama "type hinting", esto sirve para nosotros saber que tipos de datos
ser requieren en los parametros y que tipos de datos retorna una funcion

Se puede especificar que una funcion retorna un tipo de la siguiente forma:

def funcionEjemplo() -> str

Asi sabemos que funcionEjemplo retorna un str, para saber que tipos de dato
se requieren para un parametro de funcion se especifica de la siguiente forma

def funcionEjemplo(texto: str, numero: int) -> str:

Asi sabemos que esta funcion espera un string y un int, y ademas retorna un str
, es lo mismo que hacemos en java de especificar los tipos de los
parametros y retornos.

Les pido de favor utilizen el type hinting en sus funciones para hacernos el
trabajo mas facil el uno al otro :P

'''


# Como crear las funciones CRUD : Guia
# Crear una conexion
def startConn() -> pymysql.Connection:
    # envolver todas las operaciones de SQL en bloques try except
    # crear conexion
    try:
        # Establecemos parametros de la conexion
        conn = pymysql.connect(
            host='localhost',
            user='admin',
            password='257Hj986$',
            database='db'
        )
        return conn
    except pymysql.MySQLError as e:
        print(f"Error durante la conexion a la DB\n{
              e}\nContacte a su administrador de sistemas")
        sys.exit(1)


# Utilizar la conexion para realizar una operacion insert mediante un cursor
# Aqui realizamos un insert y despues un select
def ejemploQuery(conn: pymysql.Connection) -> str:
    try:
        qry = 'INSERT INTO direcciones(calle,numero,numeroInt,codigoPost,referenciasExtra) VALUES ("Parque industrial La palma",63,"14-B",80720,"Primera planta industrial del parque")'
        conn.cursor().execute(qry)
        '''
        Operaciones que realizen cambios a tablas o entradas se haran como
        transaction por ende deben de terminar con un commit
        por parte de la conexion para efectuar cambios
        '''
        conn.commit()
        # Se requiere del with para utilizar un solo cursor por operacion
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM direcciones')
            '''
            Necesitamos hacer un fetchall por parte del cursor
            para retornar los valores de un Select pues
            el execute solo retorna el numero de rows afectados
            envolmemos el cursor.fetchall en str()
            para retornarlo como string
            '''
            return str(cursor.fetchall())
    except pymysql.MySQLError as e:
        # retornamos string formateado para informar del error
        return str(f"Connection o query fallo\nError: {e}\nContacte a su administrador de sistemas")


if __name__ == "__main__":
    # imprimimos el mensaje que retorna ejemploQuery()
    # le pasamos la conexion como parametro startConn()
    print(ejemploQuery(startConn()))
