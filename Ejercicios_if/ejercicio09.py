#Ejercicio 9

CHURRASCO = 1500
COMPLETO = 1000
VEGETARIANO = 2000
BARROLUCO = 3000
DESCUENTO = 0.90


print('''
    -------------------  
    venta de sandwiches
      delivery
    -------------------  

''')
print("1:CHURRASCO = $1.500, 2:COMPLETO = $1.000, 3:VEGETARIANO = $2.000, 4:BARROLUCO = $3.000")
producto = int(input("Indique ocpión que desea (1-2-3-4): "))

if producto == 1:
    cantidad = int(input("cuantos desea llevar? : "))
    descuento = input("Tiene cupon de descuento? (S/N): ").upper()
    if descuento == "S":
        total = CHURRASCO * cantidad * DESCUENTO

    if descuento == "N":
        total = CHURRASCO * cantidad

    print(f"total a pagar: {total}")

if producto == 2:
    cantidad = int(input("cuantos desea llevar? : "))
    descuento = input("Tiene cupon de descuento? (S/N): ").upper()
    if descuento == "S":
        total = COMPLETO * cantidad - DESCUENTO

    if descuento == "N":
        total = COMPLETO * cantidad

    print(f"total a pagar: {total}")

if producto == 3:
    cantidad = int(input("cuantos desea llevar? : "))
    descuento = input("Tiene cupon de descuento? (S/N): ").upper()
    if descuento == "S":
        total = VEGETARIANO * cantidad - DESCUENTO

    if descuento == "N":
        total = VEGETARIANO * cantidad

    print(f"total a pagar: {total}")

if producto == 4:
    cantidad = int(input("cuantos desea llevar? : "))
    descuento = input("Tiene cupon de descuento? (S/N): ").upper()
    if descuento == "S":
        total = BARROLUCO * cantidad - DESCUENTO

    if descuento == "N":
        total = BARROLUCO * cantidad

    print(f"total a pagar: {total}") 