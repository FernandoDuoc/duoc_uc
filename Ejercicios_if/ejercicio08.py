#ejercicio 8

print("FABRICA DE ZAPATOS")

zapatos = 20000
envio = 3000
cantidad = int(input("Ingrese la cantidad de zapatos que desea: "))

if cantidad >= 2:
    print("Envío gratis!!")
    total = cantidad * zapatos
else:
    print("$3.000 por el envío")
    total = cantidad * zapatos + envio

print(f"Total a pagar: ${total}")