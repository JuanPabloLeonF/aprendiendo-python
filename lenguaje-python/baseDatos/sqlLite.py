import sqlite3

# Conexión a la base de datos
conexion = sqlite3.connect("test.db")

# Habilitar la fila de resultados como diccionarios
conexion.row_factory = sqlite3.Row

try:
    # Crear cursor
    cursor = conexion.cursor()

    # Crear una tabla en la base de datos si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50),
        description VARCHAR(50),
        price FLOAT
    )""")

    # Guardar cambios
    conexion.commit()

    # Insertar datos de prueba
    #cursor.execute("INSERT INTO products (name, description, price) VALUES (?, ?, ?)", ("Product 1", "Description 1", 100.5))
    conexion.commit()

    # Seleccionar todos los productos
    cursor.execute("SELECT * FROM products")
    listProducts = cursor.fetchall()
    listProductsObject = [dict(row) for row in listProducts]
        
    print(f"Productos : {listProductsObject}")
    
    #Actualizar datos de un producto
    cursor.execute("UPDATE products SET name = 'Product 1 Updated' WHERE id = 1")
    conexion.commit()
    cursor.execute("SELECT * FROM products")
    print([dict(row) for row in cursor.fetchall()])
    
    #Eliminar una consulta
    cursor.execute("DELETE FROM products WHERE id = 1")
    conexion.commit()
    cursor.execute("SELECT * FROM products")
    print([dict(row) for row in cursor.fetchall()])

finally:
    # Cerrar conexión
    conexion.close()
