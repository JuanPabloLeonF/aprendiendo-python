#Operadores aritmeticos

#Operadores aritmeticos
number1 = 77
number2 = 23

decrement = number1 - number2
increment = number1 + number2
multiplication = number1 * number2
division = number1 / number2
resto = number1 % number2

#Operadores de asignacion y logicos
asignar = number1
menorQue = number1 < number2
mayorQue = number1 > number2
menorIgual = number1 <= number2
mayorIgual = number1 >= number2
diferente = number1 != number2
igualdad = number1 == number2
operadorOr = number1 or number2
operadorAnd = number1 and number2

#Operadores de incremento y decremento
year = 2021
year += 1
year -= 1
year =+ 1
year =- 1

#Entrada y salida de datos
try:
    number = int(input("Ingresa un numero: "))
    name = str(input("Ingresa tu nombre: "))
    print(f"El numero es: {number} y tu nombre es {name}")
except ValueError:
    print("Error, no se pudo convertir el dato")
finally:  
    print("Fin del programa")