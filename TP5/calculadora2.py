import funciones as f

print("Calculadora")

while True:
    print("1 - Suma")
    print("2 - Resta")
    print("3 - Multiplicación")
    print("4 - División")
    print("5 - Salir")
    print("6 - Utilizar resultado anterior")
    operacion = int(input("Seleccione una operación: "))
    if operacion == 1:
        x1, x2 = f.ingresar_datos()
        R = f.suma(x1, x2)
        print("El resultado es ", R)
    elif operacion == 2:
        x1, x2 = f.ingresar_datos()
        R = f.resta(x1, x2)
        print("El resultado es ", R)
    elif operacion == 3:
        x1, x2 = f.ingresar_datos()
        R = f.multiplicacion(x1, x2)
        print("El resultado es ", R)
    elif operacion == 4:
        x1, x2 = f.ingresar_datos()
        R = f.division(x1, x2)
        print("El resultado es ", R)
    elif operacion == 5:
        break
    elif operacion == 6: