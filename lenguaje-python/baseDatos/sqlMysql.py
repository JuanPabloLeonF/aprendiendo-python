import mysql.connector

try:
    # Conexión a la base de datos
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="juan",
        database="test_python"
    )
    
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute("CREATE DATABASE IF NOT EXISTS test_python")
    cursor.execute("USE test_python")
    connection.commit()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(50),
        description VARCHAR(50),
        price FLOAT
        )     
    """)
    
    #cursor.execute("INSERT INTO products (name, description, price) VALUES (%s, %s, %s)", ("Product 1", "Description 1", 100.5))
    connection.commit()
    
    cursor.execute("SELECT * FROM products")
    listProducts = cursor.fetchall()
    for product in listProducts:
        print(product)
    print(listProducts)
    
    cursor.execute("UPDATE products SET price = 120.5 WHERE id = 1")
    connection.commit()
    cursor.execute("SELECT * FROM products WHERE id = 1")
    product = cursor.fetchone()
    print(f"product: {product}")
    cursor.execute("DELETE FROM products WHERE id = 1")
    connection.commit()
    cursor.execute("SELECT * FROM products")
    listProducts = cursor.fetchall()
    for product in listProducts:
        print(product)
    
except Exception as error:
    print(error)
finally:
    cursor.execute("DROP TABLE IF EXISTS products")
    cursor.close()
    connection.close()
    print("Conexión finalizada")