class Car:
    def __init__(self):
        self.__color: str = ""
        self.__model: str = ""
        self.__year: int = 0
    
    def getYear(self):
        return self.__year
    
    def getColor(self):
        return self.__color
    
    def getModel(self):
        return self.__model
    
    def setYear(self, year: int):
        self.__year = year
        
    def setColor(self, color: str):
        self.__color = color
    
    def setModel(self, model: str):
        self.__model = model
        
    def acelerar(self):
        self.__acelerar()
    
    def __acelerar(self):
        print("Acelerando")
    
    def __str__(self):
        return f"color: {self.__color}, model: {self.__model}, year: {self.__year}"
