import turtle
import colorsys
print("Segundo ejemplo de Turtle.")
pantalla = turtle.Screen()
pantalla.bgcolor("Black")
pantalla.title("Flor Mandala Multicolor")
t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)
colores = 100
h = 0

for i in range(360):
    color = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(int(color[0]*255), int(color[1]*255), int(color[2]*255))
    t.circle(100)
    t.left(360 / colores)
    h += 1 / colores

turtle.done()