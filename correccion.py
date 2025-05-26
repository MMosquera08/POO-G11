import matplotlib.pyplot as plt

print("Cálculos: Función Cuadrática.")
a = float(input("Ingrese el coeficiente de a: "))
b = float(input("Ingrese el coeficiente de b: "))
c = float(input("Ingrese el coeficiente de c: "))
print("La Ordenada al Origen es: ",c)


print("Calcular las raíces")
D = b**2 - 4*a*c
if D > 0:
    x1 = -b +- (b**2 - 4*a*c)**0.5 / (2 * a)
    x2 = -b +- (b**2 - 4*a*c)**0.5/ (2 * a)
    print("Tiene dos raíces reales: x1= ", x1, "y x2 = ", x2)
elif D == 0:
    x = -b / (2 * a)
    print("Tiene una raíz doble: x = ", x)
else:
    print("No tiene raíces reales, son complejas.")

print("Calcular los vértices")
xv = -b / (2 * a)
yv = a * xv**2 + b * xv + c
print("El vértice en x: " "",xv)
print("El vértice en y:" "",yv)
print("Fin de los cálculos.")



a = 1
b = 0
c = 0

inicio = -10
fin = 10
paso = (fin - inicio) / 399  # 400 puntos

for i in range(400):
    valor_x = inicio + i * paso
    xv.append(valor_x)
    yv.append(a * valor_x**2 + b * valor_x + c)

print("x:", xv)
print("y:", yv)
# Graficar la función cuadrática
plt.plot(xv, yv)
plt.title('Función cuadrática')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()