# Condicionales y estructuras de control

# IF, elif y else

true = True
false = False

if (true):
    print("Es verdadero")
elif (false):
    print("Es falso")
else:
    print("Ninguna de las anteriores")
    
# ternaria del if

true = True
false = False


print("Es verdadero") if true else (print("Es falso") if false else print("Ninguna de las anteriores"))

# while

number = 0
while number < 10:
    number += 1
    print(number)
    
# diferentes fors

for number in range(0, 10):
    print(number)

listNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in listNumbers:
    print(number)
    
for i in range(5):
    if i == 9:
        print("Se interrumpio el bucle")
        break
else:
    print("El bucle no fue interrumpido")

    
# break y continue
while number < 10:
    number += 1
    if number == 5:
        break
    print(number)

# try y except
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero")
    
# eliminacion de un elemento en listas
lista = [1, 2, 3, 4, 5]
del lista[0]  # Elimina el primer elemento de la lista
print(lista)

# assert Se utiliza para verificar si una expresión es verdadera y generar una excepción si no lo es. 
x = 5
assert x < 5, "x no puede ser mayor o igual a 5"

