print("Calculadora")
repetir = int(input("¿Cuántas veces desea repetir el proceso? "))
while repetir > 0:
    repetir -= 1
    print("1 = Suma")
    print("2 = Resta")
    print("3 = Multiplicación")
    print("4 = División")
    operacion = int(input("Elija una operación: "))
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    if operacion == 1:
        print("La suma de los dos números es: ", num1 + num2)
    if operacion == 2:
        print("La resta de los dos números es: ", num1 - num2)
    if operacion == 3:
        print("La multiplicación de los dos números es: ", num1 * num2)
    if operacion == 4:
        if num2 != 0:
            print("La división de los dos números es: ", num1 / num2)
        else:
            print("No se puede dividir por cero.")
print("Fin del proceso.")