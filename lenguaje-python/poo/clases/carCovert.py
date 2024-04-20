
from car import Car
class CartCover(Car):
    def __init__(self):
        self.__modelCover: str = ""
        super().__init__()
        
    def getModelCover(self):
        return self.__modelCover
    
    def setModelCover(self, modelCover: str):
        self.__modelCover = modelCover
        
    def acelerar(self):
        print("Acelerando desde la clase CartCover")
        
    def __str__(self):
        return f"color: {self.getColor()}, model: {self.getModel()}, year: {self.getYear()}, modelCover: {self.getModelCover()}"