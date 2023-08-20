#Ejercicio 7

print("identificador de tipo de triangulo")

a = int(input("Ingrese el lado A: "))
b = int(input("Ingrese el lado B: "))
c = int(input("Ingrese el lado C: "))


if a != b and b != c and a != c:
    print("Es un Escaleno")  
elif a == b and b == c and a == c:
    print("Es un Equilátero")  
else:
    print("Es un Isósceles")  
        