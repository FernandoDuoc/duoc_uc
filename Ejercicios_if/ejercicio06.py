#Ejercicio 6

cont = 0

for i in range(3):
    print("Ingrese 3 numeros enteros")
    num = int(input("Ingrese numero: "))
    if num < 0:
        cont = cont + 1

print(f"la cantidad de numeros menor a 0 es: {cont}")