print("Ejercicio 3 - Adivina el Número")
numsecreto = 86
i = 0
while i < 8:
    num = int(input("Intenta adivinar el número secreto: "))
    i = i + 1
    if num < numsecreto:
        print("El número ingresado es menor al correcto.")
    elif num > numsecreto:
        print("El número ingresado es mayor al correcto.")
    elif num == numsecreto:
        print("Ganaste.")
        break
    if i == 8:
        print("Perdiste.")