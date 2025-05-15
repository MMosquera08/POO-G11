import funciones as f

print("Calculadora")

ans=0
while True:
    uso_ans = input("¿Quiere usar ans, si o no?: ")
    if uso_ans == "no":
        print("1 - Suma")
        print("2 - Resta")
        print("3 - Multiplicación")
        print("4 - División")
        print("5 - Salir")
        operacion = (input("Seleccione una operación: "))
        if operacion == "1":
            x1, x2 = f.ingresar_datos()
            R = f.suma(x1, x2)
            print("El resultado es ", R)
        elif operacion == "2":
            x1, x2 = f.ingresar_datos()
            R = f.resta(x1, x2)
            print("El resultado es ", R)
        elif operacion == "3":
            x1, x2 = f.ingresar_datos()
            R = f.multiplicacion(x1, x2)
            print("El resultado es ", R)
        elif operacion == "4":
            x1, x2 = f.ingresar_datos()
            R = f.division(x1, x2)
            print("El resultado es ", R)
        elif operacion == "5":
            break
        ans=R
    elif uso_ans == "si":
        print("1 - Suma")
        print("2 - Resta")
        print("3 - Multiplicación")
        print("4 - División")
        print("5 - Salir")
        operacion = (input("Seleccione una operación: "))
        if operacion == "1":
            x1 = f.datos_ans()
            R = f.suma(x1, ans)
            print("El resultado es ", R)
        elif operacion == "2":
            x1 = f.datos_ans()
            R = f.resta(x1, ans)
            print("El resultado es ", R)
        elif operacion == "3":
            x1 = f.datos_ans()
            R = f.multiplicacion(x1, ans)
            print("El resultado es ", R)
        elif operacion == "4":
            x1 = f.datos_ans()
            R = f.division(x1, ans)
            print("El resultado es ", R)
        elif operacion == "5":
            break
        ans = R