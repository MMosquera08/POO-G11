print("Calculadora")
print("1 = Suma")
print("2 = Resta")
print("3 = Multiplicación")
print("4 = División")
operacion = int(input("Elija una operación: "))
if operacion == 1:
    print("Suma")
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    print("La suma de los dos números es: ", num1 + num2)
if operacion == 2:
    print("Resta")
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    print("La resta de los dos números es: ", num1 - num2)
if operacion == 3:
    print("Multiplicación")
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    print("La multiplicación de los dos números es: ", num1 * num2)
if operacion == 4:
    print("División")
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    if num2 != 0:
        print("La división de los dos números es: ", num1 / num2)
    else:
        print("No se puede dividir por cero.")