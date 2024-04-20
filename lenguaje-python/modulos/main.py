
"""
importar un modulo con sus funciones completas
import calculator 
number = calculator.sumerTwoNumbers(3, 5)
print(number)
"""

"""
importar una funcion especificamente
from calculator import sumerTwoNumbers
number = sumerTwoNumbers(3, 5)
print(number)
"""

"""
"""
#importar todas las funcines sin necesaidad de usar el modulo
from calculator import *
number = sumerTwoNumbers(3, 5)


# modulos predefinidos:

#FECHAS

import datetime

date = datetime.date.today()
print(date)
dateFormat = date.strftime("%d/%m/%Y")
print(dateFormat)
hours = datetime.datetime.now().hour
print(hours)

#Matematicas
import math

numberPi = math.pi
print(numberPi)
raiz = math.sqrt(4)
print(raiz)

# Numeros aleatorios
import random
randomNumber = random.randint(15, 20)
print(randomNumber)
