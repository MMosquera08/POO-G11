import turtle
import colorsys
print("Primer ejemplo de Turtle.")
pantalla = turtle.Screen()
pantalla.bgcolor("Black")
pantalla.title("Estrella Giratoria")

t = turtle.Turtle()
t.speed(0)
t.width(2)
turtle.colormode(255)

colores = ["Red", "Yellow", "Green", "Cyan", "Blue", "Purple"]

for i in range(120):
    t.color(colores[i % len(colores)])
    t.forward(150)
    t.right(144)
    t.forward(150)
    t.right(144)
    t.right(5)

pantalla.mainloop()