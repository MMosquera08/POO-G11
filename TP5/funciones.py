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