import os, shutil

# Crear una carpeta

existeDirectory = os.path.exists("c:/Users/USUARIO/Desktop/curso-python/lenguaje-python/sistema-archivos/directorio")

if not existeDirectory:
    print("No existe el directorio")
    os.mkdir("c:/Users/USUARIO/Desktop/curso-python/lenguaje-python/sistema-archivos/directorio")
else:
    print("El directorio ya existe")
    
# Eliminar una carpeta
existeDirectory = os.path.exists("c:/Users/USUARIO/Desktop/curso-python/lenguaje-python/sistema-archivos/directorio")

if existeDirectory:
    #os.rmdir("c:/Users/USUARIO/Desktop/curso-python/lenguaje-python/sistema-archivos/directorio")
    print("borrar la")
else:
    print("El directorio no existe")
    
# Copiar una carpeta
existeDirectory = os.path.exists("c:/Users/USUARIO/Desktop/curso-python/lenguaje-python/sistema-archivos/directorio")

if existeDirectory:
    print("El directorio existe cipoado")
    #shutil.copytree("c:/Users/USUARIO/Desktop/curso-python/lenguaje-python/sistema-archivos/directorio2", "c:/Users/USUARIO/Desktop/curso-python/lenguaje-python/sistema-archivos/directorio")
else:
    print("El directorio no existe")

# Mover una carpeta
existeDirectory = os.path.exists("c:/Users/USUARIO/Desktop/curso-python/lenguaje-python/sistema-archivos/directorio")

if existeDirectory:
    shutil.move("c:/Users/USUARIO/Desktop/curso-python/lenguaje-python/sistema-archivos/directorio2", "c:/Users/USUARIO/Desktop/curso-python/lenguaje-python/sistema-archivos/directorio")
else:
    print("El directorio no existe")
