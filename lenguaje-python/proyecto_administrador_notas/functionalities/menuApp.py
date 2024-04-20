from functionalities.personalityException import ExceptionOptions
from functionalities.models import Person, Note
from functionalities.repository import createTableInDataBase, getOnePersonByNameInDataBase, createPersonInDataBase, getVerificationUserByEmailAndName, getAllNotes, createNewNote, createTableNotes, deleteNoteByTitle
import datetime

def showMenuMain():
    try:
        print("********************MENU********************")
        print("1. Registrarse")
        print("2. Iniciar Sesion")
        option = input("Ingresa un numero para las opcione: ").strip()
        
        if not option.isnumeric():
            raise ExceptionOptions("La opcion que elegiste no es numerica")
        
        option = int(option)
        createTableInDataBase()
        
        if option < 1 or option > 2:
            raise ExceptionOptions("La opcion que elegiste no existe")
        elif option == 1:
            registryUser()
        elif option == 2:
            loginUser()
        else:
            raise ExceptionOptions("La opcion que elegiste no existe")
    except ExceptionOptions as error:
        print(error)
        option = 0
        
def registryUser():
    try:
        print("********************Registrarse********************")
        name = input("Ingresa tu nombre: ")
        lastName = input("Ingresa tu apellido: ").strip()
        email = input("Ingresa tu correo: ").strip()
        
        if len(name) == 0:
            raise ExceptionOptions("El nombre no puede estar vacio")
        elif len(lastName) == 0:
            raise ExceptionOptions("El apellido no puede estar vacio")
        elif len(email) == 0:
            raise ExceptionOptions("El correo no puede estar vacio")
        
        person = Person()
        person.setName(name)
        person.setLastName(lastName)
        person.setEmail(email)
        createPersonInDataBase(person)
        personDb = getOnePersonByNameInDataBase(person.getName())
        if not personDb:
            raise ExceptionOptions("No se pudo registrar el usuario")
        print(f"Te has registrado correctamente con el email: {personDb.getName()}")
        
    except Exception as error:
        print(error)
    
    
def loginUser():
    print("********************Iniciar sesion********************")
    print("Datos para la verificacion en el sistema")
    email = input("Ingresa tu correo: ").strip()
    name = input("Ingresa tu primer nombre: ")
    
    if len(email) == 0:
        raise ExceptionOptions("El correo no puede estar vacio")
    elif len(name) == 0:
        raise ExceptionOptions("El nombre no puede estar vacio")
    
    verification = getVerificationUserByEmailAndName(email, name)
    
    if (verification):
        print(f"Te has logueado correctamente con el email: {name} el dia : {datetime.datetime.now()}")
        showMenuAFterLogin()
    else:
        print("El usuario no existe")
        print("....Cerrando sistema por seguridad")
    
    personDb = getOnePersonByNameInDataBase(email)
    if not personDb:
        raise ExceptionOptions("El usuario no existe")
    print(f"Bienvenido {personDb.getName()}")
    
    
def showMenuAFterLogin():
    createTableNotes()
    statusMenu = True
    while statusMenu:
        print("********************MENU********************")
        print("1. Ver notas")
        print("2. Crear una nueva nota")
        print("3. Eliminar una nota")
        print("4. Salir")
        
        option = input("Ingresa un numero para las opcione: ").strip()
        if not option.isnumeric():
            raise ExceptionOptions("La opcion que elegiste no es numerica")
        
        option = int(option)
        
        if option < 1 or option > 4:
            raise ExceptionOptions("La opcion que elegiste no existe")
        elif option == 1:
            option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            statusMenu = False
        else:
            raise ExceptionOptions("La opcion que elegiste no existe")
        
    print("Cerrando sistema...")
            
    
def option1():
    listNotes = getAllNotes()
    
    if not listNotes:
        print("No hay notas")
        return
    for note in listNotes:
        print(note)
        
def option2():
    title = input("Ingresa el titulo de la nota: ").strip()
    description = input("Ingresa la descripción de la nota: ").strip()
    
    if len(title) == 0:
        raise ExceptionOptions("El titulo no puede estar vacio")
    elif len(description) == 0:
        raise ExceptionOptions("La descripción no puede estar vacia")
    
    note = Note()
    note.setTitle(title)
    note.setDescription(description)
    
    createNewNote(note)
        
def option3():
    title = input("Ingresa el titulo de la nota: ").strip()
    
    if len(title) == 0:
        raise ExceptionOptions("El titulo no puede estar vacio")
    
    deleteNoteByTitle(title)