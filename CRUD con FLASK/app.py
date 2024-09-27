# TENER EN CUENTA!!!!!!!!!!!!!
# Hay que tener instalado python y pip una vez eso pedira la instalacion de flask y las otras librerias
# Pip ya viene instalado por defecto si se instalo python bien
# Instalar flask se pone en la terminal este comando:
# pip install Flask
# Instalar MySQLdb se pone en la terminal:
# pip install mysqlclient
# Una vez instalado todo solo tendremos que dar click en el triagulo invertido en la parte superior derecha
# Y conectarnos al link que sale en la terminal
# Direccion de coneccion: http://127.0.0.1:5000
# Para finalizar el programa se da Control + C

from flask import Flask, render_template, request, redirect, url_for  # Importa Flask y funciones necesarias para la creación de la aplicación web
from flask_mysqldb import MySQL  # Importa la extensión MySQL para Flask

app = Flask(__name__)  # Crea una instancia de la aplicación Flask

# Configuración de la base de datos MySQL
app.config['MYSQL_HOST'] = 'localhost'  # Dirección del servidor MySQL
app.config['MYSQL_USER'] = 'root'  # Usuario de la base de datos
app.config['MYSQL_PASSWORD'] = ''  # Contraseña del usuario
app.config['MYSQL_DB'] = 'CRUD'  # Nombre de la base de datos

mysql = MySQL(app)  # Inicializa la extensión MySQL con la aplicación Flask

@app.route('/')  # Define la ruta para la página de inicio
def index():
    cur = mysql.connection.cursor()  # Crea un cursor para ejecutar consultas SQL
    cur.execute("SELECT * FROM productos")  # Ejecuta una consulta para obtener todos los productos
    data = cur.fetchall()  # Recupera todos los registros
    cur.close()  # Cierra el cursor
    return render_template('index.html', productos=data)  # Renderiza la plantilla 'index.html' con los productos obtenidos

@app.route('/agregar_producto', methods=['GET', 'POST'])  # Define la ruta para agregar un producto, permitiendo GET y POST
def agregar_producto():
    if request.method == 'POST':  # Si la solicitud es POST
        nombre = request.form['nombre']  # Obtiene el nombre del formulario
        marca = request.form['marca']  # Obtiene la marca del formulario
        cantidad = request.form['cantidad']  # Obtiene la cantidad del formulario
        descripcion = request.form['descripcion']  # Obtiene la descripción del formulario
        precio = request.form['precio']  # Obtiene el precio del formulario
        cur = mysql.connection.cursor()  # Crea un cursor para ejecutar consultas SQL
        cur.execute("INSERT INTO productos (nombre, marca, cantidad, precio, descripcion) VALUES (%s, %s, %s, %s, %s)", (nombre, marca, cantidad, precio, descripcion))  # Inserta un nuevo producto en la base de datos
        mysql.connection.commit()  # Confirma la transacción
        return redirect(url_for('index'))  # Redirige a la página de inicio
    
    return render_template('agregar_producto.html')  # Renderiza la plantilla 'agregar_producto.html' para mostrar el formulario

@app.route('/editar/<id>', methods=['GET', 'POST'])  # Define la ruta para editar un producto, permitiendo GET y POST
def editar_producto(id):
    cur = mysql.connection.cursor()  # Crea un cursor para ejecutar consultas SQL
    cur.execute("SELECT * FROM productos WHERE id = %s", (id,))  # Ejecuta una consulta para obtener un producto por su ID
    data = cur.fetchone()  # Recupera el registro
    cur.close()  # Cierra el cursor
    if request.method == 'POST':  # Si la solicitud es POST
        nombre = request.form['nombre']  # Obtiene el nombre del formulario
        marca = request.form['marca']  # Obtiene la marca del formulario
        cantidad = request.form['cantidad']  # Obtiene la cantidad del formulario
        descripcion = request.form['descripcion']  # Obtiene la descripción del formulario
        precio = request.form['precio']  # Obtiene el precio del formulario
        cur = mysql.connection.cursor()  # Crea un cursor para ejecutar consultas SQL
        cur.execute("""
            UPDATE productos
            SET nombre = %s, marca=%s, precio = %s, cantidad=%s, descripcion = %s
            WHERE id = %s
        """, (nombre, marca, cantidad, precio, descripcion, id))  # Actualiza el producto en la base de datos
        mysql.connection.commit()  # Confirma la transacción
        return redirect(url_for('index'))  # Redirige a la página de inicio
    
    return render_template('editar_producto.html', producto=data)  # Renderiza la plantilla 'editar_producto.html' con el producto obtenido

@app.route('/eliminar/<id>')  # Define la ruta para eliminar un producto
def eliminar_producto(id):
    cur = mysql.connection.cursor()  # Crea un cursor para ejecutar consultas SQL
    cur.execute("DELETE FROM productos WHERE id = %s", (id,))  # Ejecuta una consulta para eliminar un producto por su ID
    mysql.connection.commit()  # Confirma la transacción
    return redirect(url_for('index'))  # Redirige a la página de inicio

if __name__ == '__main__':  # Comprueba si el script se está ejecutando directamente
    app.run(debug=True)  # Ejecuta la aplicación Flask en modo debug
