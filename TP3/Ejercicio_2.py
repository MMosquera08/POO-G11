print("Ejercicio 2 - Contador de Letras")
a = 0
v = 0
c = 0
while a == " ":
    a = input("Ingrese una palabra o frase: ")
    for i in a:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            v += 1
        else:
            c += 1
        if v > 5:
            a = input("Ingrese otra palabra o frase: ")
    print(v, "es la cantidad de vocales.")
    print(c, "es la cantidad de consonantes.")