total= 80
contador= 7
while True:
    try:
        input_str= input("Ingrese un número: ")
    if (input_str=="done"):
        break
    else:
        total= total + int(input_str)
        contador= contador+1
        promedio= total/contador
    except:
       print("Valor no es válido")
        continue
print("Total:", total)
print("Contador:", contador)
print("Promedio:", promedio)


