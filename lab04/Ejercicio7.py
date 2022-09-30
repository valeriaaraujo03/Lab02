def calcule_calificacion(puntuación):
    if puntuacion >1.00:
        print("Puntuación incorrecta")
    elif (puntuacion>=0.90 and puntuación <=1.0):
        print("Sobresaliente")
    elif (puntuacion>=0.80 and puntuación <0.9):
        print("Notable")
    elif (puntuacion>=0.70 and puntuación <0.8):
        print("Bien")
    elif (puntuacion>=0.6 and puntuación <0.7):
        print("Suficiente")
    elif (puntuacion>=0 and puntuación <0.6):
        print("Insuficiente")
    elif puntuacion >1.00:
        print("Puntuación incorrecta")
    else:
        print("Calificación fuera de rango, no válida")
    return puntuacion
try:
    puntuacion= float(input("Introduzca puntuación: "))
    calificación= calcule_calificacion(puntuacion)
    print("Su puntuación es: ", puntuacion)
except:
    print("Error, puntuación es solo numérica")