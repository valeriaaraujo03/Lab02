def imprimirNumero(numero):
    if (int(numero)==1):
        mensaje="uno"
    elif(int(numero)==2):
        mensaje="dos"
    elif(int(numero)==3):
        mensaje="tres"
    else:
        mensaje= "No definido"
    return mensaje

while True:
    numero = input("Ingrese un número:")
    if(numero=="salir"):
        break
    numeroLetras= imprimirNumero(int(numero))
    print(numeroLetras)
