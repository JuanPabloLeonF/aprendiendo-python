# Capturar excepciones y manejarlas
"""
try:
    nameUser = str(input("Ingresa tu nombre completo: "))
    if len(nameUser) == 0:
        raise ValueError
    else:
        print(f"Hola {nameUser}")
except ValueError:
    print("El nombre no puede estar vacio entendidoen")
finally:
    print("Programa finalizado")
"""

# manejar multiples excepciones
"""
try:
    nameUser = str(input("Ingresa tu nombre completo: "))
    if len(nameUser) == 0:
        raise Exception
    else:
        print(f"Hola {nameUser}")
except ValueError:
    print( "este es valueError")
except NameError:
    print("El nombre no puede estar vacio")
except Exception:
    print("Error inesperado", type(Exception))
finally:
    print("Programa finalizado")
    
"""

# Crear excepciones personalizadas

class CreandoExcepcones(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

from hmac import new


try:
    name = str(input("Ingresa tu nombre completo: "))
    age = int(input("Ingresa tu edad: "))

    if (age < 0):
        #raise ValueError("No puedes tener una edad negativa")
        raise  CreandoExcepcones("No puedes tener una edad negativa") 
    elif (len(name) == 0):
        raise ValueError("El nombre no puede estar vacio")
    
except ValueError as error:
    print(error)
except CreandoExcepcones as error:
    print(error)
    
