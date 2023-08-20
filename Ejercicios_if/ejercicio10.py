#Ejercicio 10

input_comuna_compra = ""
comuna_origen = "Lo Espejo"
v_mascarilla = 500
v_total_compra = 0
input_cantidad_compra = ""
# input_precio_mascarilla = 0


print('''
    -------------------  
    Coronavirus COVID-19
      delivery de Mascarillas
    -------------------  

''')
print("Bienvenido, ingrese datos para compra")
input_comuna_compra = input("Ingrese Comuna de Compra: ")
input_cantidad_compra = int(input("Cantidad de Mascarillas: "))


v_total_compra = input_cantidad_compra * 500

if v_total_compra > 15000:
    print("Felicidades, su envío es Gratis!")
else:
    if input_comuna_compra == comuna_origen:
        #print("Es un Escaleno")
        v_total_compra += 1000  
    elif input_comuna_compra != comuna_origen or input_comuna_compra == "PAC" or input_comuna_compra == "La Cisterna" or input_comuna_compra == "Cerrillos":
        #print("Es un Equilátero")  
        v_total_compra += 2000
    else:
        #print("Es un Isósceles")  
        v_total_compra += 3000
    
print(f"El total de su compra es de {v_total_compra} pesos, gracias por su preferencia")