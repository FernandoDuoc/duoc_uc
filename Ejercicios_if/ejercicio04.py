#Ejercicio 4

flag = False
num = int(input("Ingrese un numero entre el 1 y 101: "))

if num % 2 == 0:
    flag = True
if flag:
    print("El numero ingresado es par")
else:
    print("El numero ingresado es impar") 