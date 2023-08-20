#Ejercicio 5

cont = 0
suma = 0

for i in range(3):
    print("Ingrese 3 numeros!")
    num = int(input("Ingrese numero: "))
    if num > 0 and num % 2 == 0:
        suma = suma + num
    else:
        cont = cont + 1

print(f"la suma de numeros mayores a 0 y pares es: {suma}")   
print(f"la cantidad de numeros impares y menores a 0 es: {cont}") 