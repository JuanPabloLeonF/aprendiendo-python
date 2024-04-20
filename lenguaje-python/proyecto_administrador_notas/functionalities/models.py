class Person:

    def __init__(self): 
        self.__name: str = ""
        self.__lastName: str = ""
        self.__email: str = ""
        
    def getName(self):
        return self.__name
    
    def setName(self, name: str):
        self.__name = name
        
    def getLastName(self):
        return self.__lastName
    
    def setLastName(self, lastName: str):
        self.__lastName = lastName
        
    def getEmail(self):
        return self.__email
    
    def setEmail(self, email: str):
        self.__email = email
        
    def __str__(self):
        return f"name: {self.getName()}, lastName: {self.getLastName()}, email: {self.getEmail()}"
    
class Note:
    def __init__(self): 
        self.__title: str = ""
        self.__description: str = ""
        
    def getTitle(self):
        return self.__title
    
    def setTitle(self, title: str):
        self.__title = title
        
    def getDescription(self):
        return self.__description
    
    def setDescription(self, description: str):
        self.__description = description
        
    def __str__(self):
        return f"title: {self.getTitle()}, description: {self.getDescription()}"