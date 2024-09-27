import mysql.connector  # Importa el módulo mysql.connector para interactuar con la base de datos MySQL

# Configuración de la base de datos
db_config = {
    'user': 'root',       # Usuario de la base de datos
    'password': '',       # Contraseña del usuario
    'host': 'localhost',  # Dirección del servidor de la base de datos
    'database': 'tienda'  # Nombre de la base de datos
}

# Conectar a la base de datos
def get_db_connection():
    return mysql.connector.connect(**db_config)  # Conecta a la base de datos usando la configuración definida

# Crear nuevo producto
def crear_producto(nombre, precio, cantidad):
    conn = get_db_connection()  # Obtiene una conexión a la base de datos
    cursor = conn.cursor()  # Crea un cursor para ejecutar consultas
    cursor.execute('INSERT INTO productos (nombre, precio, cantidad) VALUES (%s, %s, %s)', (nombre, precio, cantidad))  # Ejecuta una consulta para insertar un nuevo producto
    conn.commit()  # Confirma la transacción
    cursor.close()  # Cierra el cursor
    conn.close()  # Cierra la conexión a la base de datos

# Leer todos los productos
def listar_productos():
    conn = get_db_connection()  # Obtiene una conexión a la base de datos
    cursor = conn.cursor(dictionary=True)  # Crea un cursor, el resultado será un diccionario
    cursor.execute('SELECT * FROM productos')  # Ejecuta una consulta para obtener todos los productos
    productos = cursor.fetchall()  # Recupera todos los registros
    cursor.close()  # Cierra el cursor
    conn.close()  # Cierra la conexión a la base de datos
    return productos  # Retorna la lista de productos

# Leer un producto por ID
def leer_producto(producto_id):
    conn = get_db_connection()  # Obtiene una conexión a la base de datos
    cursor = conn.cursor(dictionary=True)  # Crea un cursor, el resultado será un diccionario
    cursor.execute('SELECT * FROM productos WHERE id = %s', (producto_id,))  # Ejecuta una consulta para obtener un producto por su ID
    producto = cursor.fetchone()  # Recupera el registro
    cursor.close()  # Cierra el cursor
    conn.close()  # Cierra la conexión a la base de datos
    return producto  # Retorna el producto

# Actualizar un producto por ID
def actualizar_producto(producto_id, nombre, precio, cantidad):
    conn = get_db_connection()  # Obtiene una conexión a la base de datos
    cursor = conn.cursor()  # Crea un cursor para ejecutar consultas
    cursor.execute('UPDATE productos SET nombre = %s, precio = %s, cantidad = %s WHERE id = %s', (nombre, precio, cantidad, producto_id))  # Ejecuta una consulta para actualizar un producto
    conn.commit()  # Confirma la transacción
    cursor.close()  # Cierra el cursor
    conn.close()  # Cierra la conexión a la base de datos

# Eliminar un producto por ID
def eliminar_producto(producto_id):
    conn = get_db_connection()  # Obtiene una conexión a la base de datos
    cursor = conn.cursor()  # Crea un cursor para ejecutar consultas
    cursor.execute('DELETE FROM productos WHERE id = %s', (producto_id,))  # Ejecuta una consulta para eliminar un producto por su ID
    conn.commit()  # Confirma la transacción
    cursor.close()  # Cierra el cursor
    conn.close()  # Cierra la conexión a la base de datos

# Mostrar menú
def show_menu():
    print("1. Crear nuevo producto")
    print("2. Leer todos los productos")
    print("3. Leer un producto por ID")
    print("4. Actualizar un producto por ID")
    print("5. Eliminar un producto por ID")
    print("6. Salir")

# Función principal
def main():
    while True:  # Bucle infinito para mostrar el menú hasta que el usuario elija salir
        show_menu()  # Muestra el menú
        choice = input("Elige una opción: ")  # Pide al usuario que elija una opción
        if choice == '1':  # Crear nuevo producto
            nombre = input("Nombre: ")  # Pide el nombre del producto
            precio = input("Precio: ")  # Pide el precio del producto
            cantidad = input("Cantidad: ")  # Pide la cantidad del producto
            try:
                crear_producto(nombre, float(precio), int(cantidad))  # Crea el producto con los valores proporcionados
                print("Producto creado con éxito.")
            except ValueError:  # Maneja el error si el precio o la cantidad no son válidos
                print("Error: Precio y Cantidad deben ser numéricos.")
        elif choice == '2':  # Leer todos los productos
            productos = listar_productos()  # Obtiene la lista de productos
            for producto in productos:  # Itera sobre cada producto
                print(producto)  # Imprime la información del producto
        elif choice == '3':  # Leer un producto por ID
            producto_id = input("ID del producto: ")  # Pide el ID del producto
            producto = leer_producto(producto_id)  # Obtiene el producto por su ID
            if producto:  # Si el producto existe
                print(producto)  # Imprime la información del producto
            else:  # Si el producto no existe
                print("Producto no encontrado.")
        elif choice == '4':  # Actualizar un producto por ID
            producto_id = input("ID del producto: ")  # Pide el ID del producto
            nombre = input("Nuevo nombre: ")  # Pide el nuevo nombre del producto
            precio = input("Nuevo precio: ")  # Pide el nuevo precio del producto
            cantidad = input("Nueva cantidad: ")  # Pide la nueva cantidad del producto
            try:
                actualizar_producto(producto_id, nombre, float(precio), int(cantidad))  # Actualiza el producto con los nuevos valores
                print("Producto actualizado con éxito.")
            except ValueError:  # Maneja el error si el precio o la cantidad no son válidos
                print("Error: Precio y Cantidad deben ser numéricos.")
        elif choice == '5':  # Eliminar un producto por ID
            producto_id = input("ID del producto: ")  # Pide el ID del producto
            eliminar_producto(producto_id)  # Elimina el producto por su ID
            print("Producto eliminado con éxito.")
        elif choice == '6':  # Salir del programa
            break  # Sale del bucle
        else:  # Opción no válida
            print("Opción no válida. Por favor, elige de nuevo.")

# Si este archivo se ejecuta directamente, llama a la función principal
if __name__ == "__main__":
    main()
