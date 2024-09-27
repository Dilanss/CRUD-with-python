# Importa el módulo mysql.connector y la clase Error del mismo módulo
import mysql.connector
from mysql.connector import Error

# Función para establecer una conexión a la base de datos
def conectar():
    try:
        # Intenta establecer una conexión con la base de datos
        conn = mysql.connector.connect(
            host='localhost',       # Dirección del servidor de la base de datos
            database='tienda',      # Nombre de la base de datos
            user='root',            # Nombre de usuario para la conexión
            password=''             # Contraseña del usuario (aquí está vacío) esto dependiendo de cada XAMPP
        )
        # Si la conexión es exitosa y está establecida, la función retorna el objeto de conexión
        if conn.is_connected():
            return conn
    except Error as e:
        # Si ocurre un error, lo captura e imprime el mensaje de error
        print(f"Error al conectar a MySQL: {e}")
        # Retorna None si la conexión falla
        return None

# Función para crear un nuevo producto en la base de datos
def crear_producto(nombre, precio, cantidad):
    # Llama a la función conectar() para obtener la conexión
    conn = conectar()
    if conn:
        # Crea un cursor para interactuar con la base de datos
        cursor = conn.cursor()
        # Ejecuta la consulta SQL para insertar un nuevo producto
        cursor.execute('''
            INSERT INTO productos (nombre, precio, cantidad)
            VALUES (%s, %s, %s)
        ''', (nombre, precio, cantidad))
        # Confirma los cambios en la base de datos
        conn.commit()
        # Cierra el cursor y la conexión
        cursor.close()
        conn.close()

# Función para listar todos los productos de la base de datos
def listar_productos():
    # Llama a la función conectar() para obtener la conexión
    conn = conectar()
    if conn:
        # Crea un cursor para interactuar con la base de datos
        cursor = conn.cursor()
        # Ejecuta la consulta SQL para seleccionar todos los productos
        cursor.execute('SELECT * FROM productos')
        # Obtiene todos los resultados de la consulta
        productos = cursor.fetchall()
        # Cierra el cursor y la conexión
        cursor.close()
        conn.close()
        # Retorna la lista de productos
        return productos

# Función para actualizar un producto existente en la base de datos
def actualizar_producto(id, nombre, precio, cantidad):
    # Llama a la función conectar() para obtener la conexión
    conn = conectar()
    if conn:
        # Crea un cursor para interactuar con la base de datos
        cursor = conn.cursor()
        # Ejecuta la consulta SQL para actualizar un producto
        cursor.execute('''
            UPDATE productos
            SET nombre = %s, precio = %s, cantidad = %s
            WHERE id = %s
        ''', (nombre, precio, cantidad, id))
        # Confirma los cambios en la base de datos
        conn.commit()
        # Cierra el cursor y la conexión
        cursor.close()
        conn.close()

# Función para eliminar un producto de la base de datos
def eliminar_producto(id):
    # Llama a la función conectar() para obtener la conexión
    conn = conectar()
    if conn:
        # Crea un cursor para interactuar con la base de datos
        cursor = conn.cursor()
        # Ejecuta la consulta SQL para eliminar un producto
        cursor.execute('DELETE FROM productos WHERE id = %s', (id,))
        # Confirma los cambios en la base de datos
        conn.commit()
        # Cierra el cursor y la conexión
        cursor.close()
        conn.close()
