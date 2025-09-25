import pymysql

# def deleteCliente(conn: pymysql.Connection, clienteID: int) -> bool:
#     # Descripcion del SP
#     # 1. Asignar todas las ordenes del usuario al "Cliente default"
#     #    el cual sera un cliente creado para mantener historial de las ordenes
#     #    creadas por clientes que no desean estar en nuestra base de datos despues de
#     #    terminar su negocio con nosotros
#     # 2. Borrar Direccion y Usuario
#     pass

def addCliente(conn: pymysql.Connection, nombre: str, email: str, telefono: str, calle: str, numero: str, numeroInt: str, codigoPost: str, referenciasExtra: str ) -> bool:
    try:
        parametros = [
            nombre,          # p_nombre
            email,           # p_email
            telefono,        # p_telefono
            calle,           # p_calle
            numero,          # p_numero
            numeroInt,       # p_numeroInt
            codigoPost,      # p_codigoPost
            referenciasExtra # p_referenciasExtra
        ]

        with conn.cursor() as cursor:
            cursor.callproc('InsertarCliente_Direccion', parametros)
        conn.commit()
        return True

        # Opcional: verificar resultados
        # with conn.cursor() as cursor:
        #     cursor.execute('SELECT * FROM clientes')
        #     clientes = cursor.fetchall()
        #     columnas = [desc[0] for desc in cursor.description]
        #     return [dict(zip(columnas, row)) for row in clientes]

    except pymysql.MySQLError :
        return False

# def updateCliente(conn: pymysql.Connection, clienteID: int) -> bool:
#     pass

def getClientes(conn: pymysql.Connection) -> tuple:
    with conn.cursor() as c:
        c.execute("SELECT c.clienteID, c.nombre, c.telefono, c.email, d.calle, d.numero, d.numeroInt, d.codigoPost, d.referenciasExtra FROM clientes c INNER JOIN direcciones d ON c.direccionDeEntregas = d.direccionID")
        return c.fetchall()
