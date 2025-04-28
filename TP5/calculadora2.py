print("Calculadora")

def ingresar_datos():
    x1 = int(input("Ingrese el primer número: "))
    x2 = int(input("Ingrese el segundo número: "))
    return x1, x2
def suma(x1, x2):
    resultado = x1 + x2
    return resultado
def resta(x1, x2):
    resultado = x1 - x2
    return resultado
def multiplicacion(x1, x2):
    resultado = x1 * x2
    return resultado
def division(x1, x2):
    if x2 != 0:
        resultado = x1 / x2
        return resultado
    else:
        return "No se puede dividir por cero."

while True:
    print("1 - Suma")
    print("2 - Resta")
    print("3 - Multiplicación")
    print("4 - División")
    print("5 - Salir")
    operacion = int(input("Seleccione una operación: "))
    if operacion == 1:
        x1, x2 = ingresar_datos()
        R = suma(x1, x2)
        print("El resultado es ", R)
    elif operacion == 2:
        x1, x2 = ingresar_datos()
        R = resta(x1, x2)
        print("El resultado es ", R)
    elif operacion == 3:
        x1, x2 = ingresar_datos()
        R = multiplicacion(x1, x2)
        print("El resultado es ", R)
    elif operacion == 4:
        x1, x2 = ingresar_datos()
        R = division(x1, x2)
        print("El resultado es ", R)
    elif operacion == 5:
        break