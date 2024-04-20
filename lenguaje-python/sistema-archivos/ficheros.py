from io import open
import pathlib
import shutil
import os

#Abrir archivo
# Obtener la ruta absoluta del directorio actual del script
script_directory = pathlib.Path(__file__).resolve().parent
nameUbicationArchivo = str(script_directory) + "/fichero.txt"
print(nameUbicationArchivo)
archivo = open(nameUbicationArchivo, "a+")
archivo.writelines("Hola mundo")
archivo.close()

#leer contenido de archvico
archivo = open(nameUbicationArchivo, "r")
#contenido = archivo.read()
#print(contenido)

#leer contenido de archivo linea por linea
#for linea in contenido:
#    print(linea)
    
# leer contenido y guardarlo en una lista
contenidoList = archivo.readlines()
print(contenidoList)
archivo.close()

# copiar archivos
nameUbicationArchivoOriginal = str(script_directory) + "/fichero.txt"
nameUbicationArchivoNuevo = str(script_directory) + "/fichero2.txt"
#shutil.copyfile(nameUbicationArchivoOriginal, nameUbicationArchivoNuevo)

# mover un archivo
#nameUbicationArchivoOriginal = str(script_directory) + "/fichero_copiado_nuevo.txt"
#nameUbicationArchivoNuevo = str(script_directory) + "/fichero.txt"
shutil.move(nameUbicationArchivoOriginal, nameUbicationArchivoNuevo)

# eliminar archivos
nameUbicationArchivoNuevo = str(script_directory) + "/fichero2.txt"
os.remove(nameUbicationArchivoNuevo)

# comprobar si existe un archivo
print(os.path.exists(nameUbicationArchivoNuevo))
result = f"El archvo con la ruta: {nameUbicationArchivoNuevo} si existe" if os.path.exists(nameUbicationArchivoNuevo) else f"El archvo con la ruta: {nameUbicationArchivoNuevo} no existe"
print(result)