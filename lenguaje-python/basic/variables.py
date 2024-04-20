name = "Julian"
lastName = "Hernandez"
website = "julianhernandez.com"
number = 23
double = 23.5

print(f"My name is {name} {lastName} and my website is {website}")

#Tipos de datos

nothing = None
print(type(nothing))

string = "hola"
print(type(string))

integer = 23
print(type(integer))

floatNumber = 23.5
print(type(float))

boolean = True
print(type(boolean))

list = [1, 2, 3, 4, 5]
print(type(list))

tuple = (1, 2, 3, 4, 5)
print(type(tuple))

set = {1, 2, 3, 4, 5}
print(type(set))

dict = {
    "name": "Julian",
    "lastName": "Hernandez"
}
print(type(dict))

range1= range(9)
print(type(range1))

byteStr = b"hola"
print(type(byteStr))

#Conversiones 
text = "hola mundo"
number = 5
print(text + str(number))

number = int(number)
number = float(number)

print(number)