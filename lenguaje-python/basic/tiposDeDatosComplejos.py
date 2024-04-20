#Tipos de dtos complejos

#Listas
listNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(listNumbers)
listNumbers.append(11)
print(listNumbers)
listNumbers.reverse()
print(listNumbers)
del listNumbers[0]
print(listNumbers)
# matrices
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matriz:
    for column in row:
        print(column)

# Sets
setNumbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1}
print(setNumbers)
setNumbers.add(11)
print(setNumbers)

#Diccionarios
dicNumbers = {
    "name": "Julian",
    "lastName": "Hernandez",
    "age": 23
}
print(dicNumbers)
dicNumbers["dni"] = 12345678
print(dicNumbers)