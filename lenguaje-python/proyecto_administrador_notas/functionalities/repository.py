import mysql.connector
from functionalities.models import Person, Note

def createTableInDataBase():
    try:
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
            CREATE TABLE IF NOT EXISTS persons(
            id INTEGER PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(50),
            lastName VARCHAR(50),
            email VARCHAR(50) 
        )""")
        
        connection.commit()
    
    except Exception as error:
        print(error)
    finally:
        #cursor.execute("DROP DATABASE IF EXISTS test_python")
        cursor.close()
        connection.close()
        
def createPersonInDataBase(person):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="juan",
            database="test_python"
        )
        
        cursor = connection.cursor(dictionary=True)
        
        cursor.execute("INSERT INTO persons (name, lastName, email) VALUES (%s, %s, %s)", (person.getName(), person.getLastName(), person.getEmail()))
        connection.commit()

        print("Te registraste de forma exitosa")
        
    except Exception as error:
        print(error)
    finally:
        cursor.close()
        connection.close()
        
def getOnePersonByNameInDataBase(name):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="juan",
            database="test_python"
        )
        
        cursor = connection.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM persons WHERE name = %s", (name,))
        personDb = cursor.fetchone()
        
        if personDb is None:
            raise Exception(f"No se encontró ninguna persona con el nombre '{name}' en la base de datos")
        
        person = Person()
        person.setName(personDb["name"])
        person.setLastName(personDb["lastName"])
        person.setEmail(personDb["email"]) 
        
        return person
        
    except Exception as error:
        print(error)
    finally:
        cursor.close()
        connection.close()
        
def getVerificationUserByEmailAndName(email, name):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="juan",
            database="test_python"
        )
        
        cursor = connection.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM persons WHERE email = %s AND name = %s", (email, name))
        personDb = cursor.fetchone()
        
        if personDb is None:
            return False
        else:
            return True
    except Exception as error:
        print(error)
    finally:
        cursor.close()
        connection.close()
        
def getAllNotes():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="juan",
            database="test_python"
        )
        
        cursor = connection.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM notes")
        notesDb = cursor.fetchall()
        
        notes = []
        for noteDb in notesDb:
            note = Note()
            note.setTitle(noteDb["title"])
            note.setDescription(noteDb["description"])
            notes.append(note)
        
        return notes
    except Exception as error:
        print(error)
    finally:
        cursor.close()
        connection.close()
        
def createNewNote(note):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="juan",
            database="test_python"
        )
        
        cursor = connection.cursor(dictionary=True)
        
        cursor.execute("INSERT INTO notes (title, description) VALUES (%s, %s)", (note.getTitle(), note.getDescription()))
        connection.commit()
        
        print("Secreo la nota de forma exitosa")
    except Exception as error:
        print(error)
    finally:
        cursor.close()
        connection.close()

def getOneNoteByTitle(title):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="juan",
            database="test_python"
        )
        
        cursor = connection.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM notes WHERE title = %s", (title,))
        noteDb = cursor.fetchone()
        
        if noteDb is None:
            raise Exception(f"No se encontró ninguna nota con el titulo '{title}' en la base de datos")
        
        note = Note()
        note.setTitle(noteDb["title"])
        note.setDescription(noteDb["description"])
        
        return note
    except Exception as error:
        print(error)
    finally:
        cursor.close()
        connection.close()        


def createTableNotes():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="juan",
            database="test_python"
        )
        
        cursor = connection.cursor(dictionary=True)
        
        cursor.execute("CREATE TABLE IF NOT EXISTS notes(id INTEGER PRIMARY KEY AUTO_INCREMENT, title VARCHAR(50), description VARCHAR(50))")
        connection.commit()
    except Exception as error:
        print(error)
    finally:
        cursor.close()
        connection.close()
        
def deleteNoteByTitle(title):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="juan",
            database="test_python"
        )
        
        cursor = connection.cursor(dictionary=True)
        
        cursor.execute("DELETE FROM notes WHERE title = %s", (title,))
        connection.commit()
        
        print("Eliminaste la nota de forma exitosa")
    except Exception as error:
        print(error)
    finally:
        cursor.close()
        connection.close()