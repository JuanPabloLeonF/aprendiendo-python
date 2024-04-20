from carCovert import CartCover
from car import Car

cart1 = CartCover()
cart1.acelerar()
cart1.setColor("red")
cart1.setYear(2020)
cart1.setModel("Mustang")
cart1.setModelCover("Ferrari")
print(f"Cart1: {cart1}")

if isinstance(cart1, Car):
    print("cart1 es una instancia de Car")
else:
    print("cart1 no es una instancia de CartCover")