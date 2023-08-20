#Ejercicio 11

AGUA = 600
AZUCAR = 1200
ACEITE = 1500
ARROZ = 1250
FIDEOS = 790
BEBIDA = 1780
CHOCOLATE = 2500
PANMOLDE = 1340
acum = 0
DESCUENTO = 0.75

print('''
      
      sistema de venta de productos

            1 AGUA = 600
            2 AZUCAR = 1200
            3 ACEITE = 1500
            4 ARROZ = 1250
            5 FIDEOS = 790
            6 BEBIDA = 1780
            7 CHOCOLATE = 2500
            8 PANMOLDE = 1340
    ''')




print(f"1 AGUA = ${AGUA}")
producto = input("¿Desea el producto?(S/N): ").upper()
if producto == "S":
    cantidad = int(input("¿Cuantos desea?: "))
    acum = acum + AGUA * cantidad
elif producto == "N":
    print("Siguiente producto!")

print("2 AZUCAR = 1200")
producto = input("¿Desea el producto?(S/N): ").upper()
if producto == "S":
    cantidad = int(input("¿Cuantos desea?: "))
    acum = acum + AZUCAR * cantidad
elif producto == "N":
    print("Siguiente producto!")  

print("3 ACEITE =1500")
producto = input("¿Desea el producto?(S/N): ").upper()
if producto == "S":
    cantidad = int(input("¿Cuantos desea?: "))
    acum = acum + ACEITE * cantidad
elif producto == "N":
    print("Siguiente producto!")     

print("4 ARROZ = 1250")
producto = input("¿Desea el producto?(S/N): ").upper()
if producto == "S":
    cantidad = int(input("¿Cuantos desea?: "))
    acum = acum + ARROZ * cantidad
elif producto == "N":
    print("Siguiente producto!")

print("5 FIDEOS = 790")
producto = input("¿Desea el producto?(S/N): ").upper()
if producto == "S":
    cantidad = int(input("¿Cuantos desea?: "))
    acum = acum + FIDEOS * cantidad
elif producto == "N":
    print("Siguiente producto!")

print("6 BEBIDA = 1780")
producto = input("¿Desea el producto?(S/N): ").upper()
if producto == "S":
    cantidad = int(input("¿Cuantos desea?: "))
    acum = acum + BEBIDA * cantidad
elif producto == "N":
    print("Siguiente producto!")

print("7 CHOCOLATE = 2500")
producto = input("¿Desea el producto?(S/N): ").upper()
if producto == "S":
    cantidad = int(input("¿Cuantos desea?: "))
    acum = acum + CHOCOLATE * cantidad
elif producto == "N":
    print("Siguiente producto!")                 

print("8 PAN DE MOLDE = 1340")
producto = input("¿Desea el producto?(S/N): ").upper()
if producto == "S":
    cantidad = int(input("¿Cuantos desea?: "))
    acum = acum + PANMOLDE * cantidad
elif producto == "N":
    print("Siguiente producto!")

cliente = input("¿Ud es cliente preferencial?(S/N): ").upper()
if cliente == "S":
    total = acum * DESCUENTO
    print(f"El total de su compra es: ${total}")

    efectivo = int(input("Ingrese el valor del efectivo: "))
    if efectivo > total:
        vuelto = efectivo - total
        print(f"Su vuelto es de: ${vuelto}")
    else:
        print("Dinero insuficiente, Guardias!")    

elif cliente == "N":
    total = acum
    print(f"El total de su compra es: ${total}")

    efectivo = int(input("Ingrese el valor del efectivo: "))
    if efectivo > total:
        vuelto = efectivo - total
        print(f"Su vuelto es de: ${vuelto}")
    else:
        print("Dinero insuficiente, Guardias!") 