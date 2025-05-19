import matplotlib.pyplot as plt

a = 1
b = 0
c = 0

x = []
y = []
inicio = -10
fin = 10
paso = (fin - inicio) / 399  # 400 puntos

for i in range(400):
    valor_x = inicio + i * paso
    x.append(valor_x)
    y.append(a * valor_x**2 + b * valor_x + c)

print("x:", x)
print("y:", y)
# Graficar la función cuadrática
plt.plot(x, y, label=f'{a}x² + {b}x + {c}')
plt.title('Función cuadrática')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()

a = float(input("Ingrese el coeficiente de a: "))
b = float(input("Ingrese el coeficiente de b: "))
c = float(input("Ingrese el coeficiente de c: "))
print("La Ordenada al Origen es: ",c)

print("Calcular las raíces")
if d > 0:
    x1 = (-b + d**0.5) / (2 * a)
    x2 = (-b + d**0.5) / (2 * a)
    print("Tiene dos raíces reales: x1= ", x1, "y x2 = ", x2)
elif d == 0:
    x = -b / (2 * a)
    print("Tiene una raíz doble: x = ", x)
else:
    print("No tiene raíces reales, son complejas.")

print("Calcular los vértices")
xv = -b / (2 * a)
xy = a * xv**2 + b * xv + c
print("El vértice es: (" , xv, ",", yv, ")")