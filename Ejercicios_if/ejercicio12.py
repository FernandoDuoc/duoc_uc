#Ejercicio 12

#acumulador
acum = 0
#entradas
ESTRENO = 4800
NORMAL = 2900
#palomitas 
PALOMITAPEQUENA = 2500
PALOMITAMEDIANA = 4500
PALOMITAGRANDE = 7800
#bebidas
BEBIDAPEQUENA = 1000
BEBIDAMEDIANA = 1250
BEBIDAGRANDE = 2000
DESCUENTO = 0.70

print('''

    -----------------------
        CINE DUOC
    -----------------------
      VENTA DE BOLETOS
      PALOMITAS Y BEBIDAS
    -----------------------
          
    ''')

cliente = input("¿Pertenece a Duoc?(S/N): ").upper()
if cliente == "S":
    print("Pertenece a la Institución / descuento en entrada del 30%")
    entrada = input("¿Qué entrada desea?(E: Estreno/ N: Normal): ").upper()
    if entrada == "E":
        acum += ESTRENO * DESCUENTO
        print(f"Estreno, valor ${ESTRENO*DESCUENTO} ")
    elif entrada == "N":
        acum += NORMAL * DESCUENTO
        print(f"Normal, valor ${NORMAL*DESCUENTO} ")
elif cliente == "N":
    print("No Pertenece a la Institución")
    entrada = input("¿Qué entrada desea?(E: Estreno/ N: Normal): ").upper()
    if entrada == "E":
        acum += ESTRENO
        print(f"Estreno, valor ${ESTRENO} ")
    elif entrada == "N":
        acum += NORMAL
        print(f"Normal, valor ${NORMAL} ")


palomita = input("¿Desea palomitas?(S/N): ").upper()
if palomita == "S":
    palomita = input("¿Qué porte desea?: (P: pequeña $2.500 / M: mediana $4.500 / G: grande $7.800): ").upper()
    if palomita == "P":
        print(f"escogió palomitas pequeñas ${PALOMITAPEQUENA}")
        acum += PALOMITAPEQUENA
    elif palomita == "M":
        print(f"escogió palomitas medianas ${PALOMITAMEDIANA}")
        acum += PALOMITAMEDIANA
    elif palomita == "G":
        print(f"escogió palomitas grandes ${PALOMITAGRANDE}")
        acum += PALOMITAGRANDE
else:
    print("No desea palomitas, continuar...")

bebida = input("¿Desea bebida?(S/N): ").upper()
if bebida == "S":
    bebida = input("¿Qué porte desea?: (P: pequeña $1.000 / M: mediana $1.250 / G: grande $2.000): ").upper()
    if bebida == "P":
        print(f"escogió bebida pequeña ${BEBIDAPEQUENA}")
        acum += BEBIDAPEQUENA
    elif bebida == "M":
        print(f"escogió bebida mediana ${BEBIDAMEDIANA}")
        acum += BEBIDAMEDIANA
    elif bebida == "G":
        print(f"escogió palomitas grandes ${BEBIDAGRANDE}")
        acum += BEBIDAGRANDE
else:
    print("No desea bebida, continuar...")

print(f"Total a pagar ${acum}")
efectivo = int(input("Ingrese el valor del efectivo: "))
if efectivo > acum:
    vuelto = efectivo - acum
    print(f"Su vuelto es de: ${vuelto}")
else:
    print("Dinero insuficiente, Guardias!")         

print("Disfrute la pelicula!")