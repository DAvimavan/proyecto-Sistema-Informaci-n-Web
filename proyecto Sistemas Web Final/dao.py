import sqlite3
from modelo import Product, Usuario


#CAPA DE PERSISTENCIA


def get_db_connection():
    conn = sqlite3.connect('database.db')
    return conn


#PRODUCT crear base de datos
def create_product_table_Product():
    conn = get_db_connection() 
    cursor = conn.cursor() 

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            idProduct INTEGER PRIMARY KEY AUTOINCREMENT,
            nombreProduct TEXT NOT NULL,
            descripcionProduct TEXT NOT NULL,
            precio REAL NOT NULL,
            disponibilidad BOOLEAN NOT NULL
        );
    ''')

    conn.commit()
    conn.close() 
    

#PRODUCTO CREATE, INSERTAR
def insert_or_update_product(product:Product):
    conn = get_db_connection()  # Llamamos a la función para obtener la conexión
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO products (nombreProduct, descripcionProduct, precio, disponibilidad)
        VALUES (?,?,?,?)
    ''', (product.nombreProduct, product.descripcionProduct, product.precio, product.disponibilidad))

    conn.commit()
    conn.close()
    return {"product": product}


#PRODUCTO recuperar un dato
def get_product(product_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT nombreProduct, descripcionProduct, precio, disponibilidad FROM products WHERE idProduct = ?
    ''', (product_id,))

    product = cursor.fetchone()
    conn.close()

    return product


# PRODUCTO recuperar todos los datos
def get_all_products():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT idProduct,nombreProduct,descripcionProduct,precio,disponibilidad FROM products")
    products = cursor.fetchall()

    for product in products:     #Muestra por pantalla todos los datos de cada producto (prueba para ver si funciona correctamente)
        id_product, nombre, descripcion, precio, disponibilidad = product
        print("El ID del producto es:", id_product)
        print("El nombre del producto es:", nombre)
        print("La descripción del producto es:", descripcion)
        print("El precio del producto es:", precio)
        print("La disponibilidad del producto es:", disponibilidad)
        print("-----------------------------------")
    conn.cursor()
    return products



#PRODUCTO borrar un dato
def delete_product(product_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM products WHERE idProduct = ?', (product_id,))
    conn.commit()
    conn.close() 




#USUARIO crear base de datos
def create_product_table_Usuario():
    conn = get_db_connection()  
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
            nombreUsuario TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            contrasena TEXT NOT NULL
        );
    ''')

    conn.commit()
    conn.close()


#USUARIO CREATE, INSERTAR
def insert_or_update_Usuario(usuario:Usuario):
    conn = get_db_connection()  # Llamamos a la función para obtener la conexión
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO usuarios (nombreUsuario,email,contrasena)
        VALUES (?,?,?)
    ''', (usuario.nombreUsuario,usuario.email,usuario.contrasena))

    conn.commit()
    conn.close()
    return {"usuario": usuario}


#Usuario recuperar un dato
def get_Usuario(id_usuario: int):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT  nombreUsuario,email,contrasena FROM usuarios WHERE id_usuario = ?
    ''', (id_usuario,))

    product = cursor.fetchone()
    conn.close()

    return product


# USUARIO recuperar todos los datos
def get_all_Usuarios():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id_usuario,nombreUsuario,email,contrasena FROM usuarios")
    usuarios = cursor.fetchall()

    for usuario in usuarios:     #Muestra por pantalla todos los datos de cada usuario (prueba para ver si funciona correctamente)
        id_usuario, nombreUsuario, email,contrasena = usuario
        print("El ID del usuario es:", id_usuario)
        print("El nombre del usuario es:", nombreUsuario)
        print("El email del usuario es:", email)
        print("La contrasena del usuario es: ", contrasena) #Esto no se deberia de mostrar pero bueno, es una prueba 
        print("-----------------------------------")
    conn.cursor()
    return usuarios


#USUARIO borrar un dato
def delete_usuario(id_usuario: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM usuarios WHERE  id_usuario= ?', (id_usuario,))
    conn.commit()
    conn.close() 