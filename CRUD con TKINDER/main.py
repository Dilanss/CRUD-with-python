# Importa el módulo tkinter para crear interfaces gráficas
import tkinter as tk
# Importa el módulo messagebox de tkinter para mostrar mensajes emergentes
from tkinter import messagebox
# Importa las funciones CRUD desde el módulo db
from db import crear_producto, listar_productos, actualizar_producto, eliminar_producto

# Función para agregar un producto
def agregar_producto():
    # Obtiene los valores de las entradas
    nombre = entry_nombre.get()
    precio = entry_precio.get()
    cantidad = entry_cantidad.get()

    # Verifica que todos los campos estén llenos
    if nombre and precio and cantidad:
        try:
            # Intenta crear un producto con los valores proporcionados
            crear_producto(nombre, float(precio), int(cantidad))
            # Lista los productos en la interfaz después de agregar uno nuevo
            listar_en_interfaz()
            # Limpia las entradas
            limpiar_entradas()
            # Muestra un mensaje de éxito
            messagebox.showinfo("Éxito", "Producto agregado con éxito")
        except ValueError:
            # Muestra un mensaje de error si el precio o la cantidad no son numéricos
            messagebox.showerror("Error", "Precio y Cantidad deben ser numéricos")
    else:
        # Muestra un mensaje de error si no todos los campos están llenos
        messagebox.showerror("Error", "Todos los campos son requeridos")

# Función para listar productos en la interfaz
def listar_en_interfaz():
    # Destruye los widgets hijos del frame de productos para actualizarlos
    for widget in frame_productos.winfo_children():
        widget.destroy()

    # Obtiene la lista de productos desde la base de datos
    productos = listar_productos()
    # Crea un frame y etiquetas para cada producto
    for producto in productos:
        frame = tk.Frame(frame_productos)
        frame.pack(fill='x', padx=5, pady=5)
        
        tk.Label(frame, text=f"ID: {producto[0]}").pack(side='left')
        tk.Label(frame, text=f"Nombre: {producto[1]}").pack(side='left', padx=10)
        tk.Label(frame, text=f"Precio: {producto[2]}").pack(side='left', padx=10)
        tk.Label(frame, text=f"Cantidad: {producto[3]}").pack(side='left', padx=10)

        tk.Button(frame, text="Editar", command=lambda p=producto: editar_producto(p)).pack(side='left', padx=10)
        tk.Button(frame, text="Eliminar", command=lambda p=producto[0]: eliminar_producto_en_interfaz(p)).pack(side='left', padx=10)

# Función para limpiar las entradas
def limpiar_entradas():
    entry_nombre.delete(0, tk.END)
    entry_precio.delete(0, tk.END)
    entry_cantidad.delete(0, tk.END)

# Función para editar un producto
def editar_producto(producto):
    # Crea una nueva ventana para editar el producto
    edit_window = tk.Toplevel(ventana)
    edit_window.title("Editar Producto")

    # Crea etiquetas y entradas para el nombre, precio y cantidad del producto
    tk.Label(edit_window, text="Nombre").grid(row=0, column=0)
    entry_edit_nombre = tk.Entry(edit_window)
    entry_edit_nombre.grid(row=0, column=1)
    entry_edit_nombre.insert(0, producto[1])

    tk.Label(edit_window, text="Precio").grid(row=1, column=0)
    entry_edit_precio = tk.Entry(edit_window)
    entry_edit_precio.grid(row=1, column=1)
    entry_edit_precio.insert(0, producto[2])

    tk.Label(edit_window, text="Cantidad").grid(row=2, column=0)
    entry_edit_cantidad = tk.Entry(edit_window)
    entry_edit_cantidad.grid(row=2, column=1)
    entry_edit_cantidad.insert(0, producto[3])

    # Función para guardar los cambios del producto editado
    def guardar_cambios():
        nombre = entry_edit_nombre.get()
        precio = entry_edit_precio.get()
        cantidad = entry_edit_cantidad.get()
        try:
            # Actualiza el producto con los nuevos valores
            actualizar_producto(producto[0], nombre, float(precio), int(cantidad))
            # Actualiza la lista de productos en la interfaz
            listar_en_interfaz()
            # Cierra la ventana de edición
            edit_window.destroy()
            # Muestra un mensaje de éxito
            messagebox.showinfo("Éxito", "Producto actualizado con éxito")
        except ValueError:
            # Muestra un mensaje de error si el precio o la cantidad no son numéricos
            messagebox.showerror("Error", "Precio y Cantidad deben ser numéricos")

    # Crea un botón para guardar los cambios
    tk.Button(edit_window, text="Guardar", command=guardar_cambios).grid(row=3, column=0, columnspan=2)

# Función para eliminar un producto
def eliminar_producto_en_interfaz(producto_id):
    # Elimina el producto de la base de datos
    eliminar_producto(producto_id)
    # Actualiza la lista de productos en la interfaz
    listar_en_interfaz()
    # Muestra un mensaje de éxito
    messagebox.showinfo("Éxito", "Producto eliminado con éxito")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("CRUD de Productos")

# Ajusta el tamaño de la ventana (ancho x alto)
ventana.geometry("500x400")  # Ajusta las dimensiones según lo desees

# Crea etiquetas y entradas para el nombre, precio y cantidad del producto
tk.Label(ventana, text="Nombre").grid(row=0, column=0)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1)

tk.Label(ventana, text="Precio").grid(row=1, column=0)
entry_precio = tk.Entry(ventana)
entry_precio.grid(row=1, column=1)

tk.Label(ventana, text="Cantidad").grid(row=2, column=0)
entry_cantidad = tk.Entry(ventana)
entry_cantidad.grid(row=2, column=1)

# Crea un botón para agregar un nuevo producto
tk.Button(ventana, text="Agregar Producto", command=agregar_producto).grid(row=3, column=0, columnspan=2)

# Crea un frame para mostrar la lista de productos
frame_productos = tk.Frame(ventana)
frame_productos.grid(row=4, column=0, columnspan=2)

# Lista los productos en la interfaz al iniciar la aplicación
listar_en_interfaz()

# Inicia el bucle principal de la interfaz gráfica
ventana.mainloop()

# PARA EJECUTAR EL PROGRAMA SOLO SE TIENE QUE DAR CLICK EN EL TRAIGULO INVERTIDO EN LA PARTE DERECHA SUPERIOR DE VISUAL STUDIO
# NO OLVIDAR AGREGAR LA BASE DE DATOS A PHPMYADMIN
