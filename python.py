import random

longitud=int(input("escribe cauntos digitos tendra su contraseña:"))
elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
contraseña="3"

for i in range(longitud):
    contraseña += random.choice(elements)

print("su contraseña es",contraseña)
