class Mascota:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
        self.felicidad = 75
        self.energia = 75
        self.hambre = 75

    def jugar(self, incremento, decremento):
        self.felicidad += incremento
        if self.felicidad > 100:
            self.felicidad = 100
        self.energia -= decremento
        if self.energia < 0:
            self.energia = 0
        self.hambre -= decremento
        if self.hambre < 0:
            self.hambre = 0
        print(f"¡{self.nombre} corretea feliz! Su felicidad subió.")
        print(f"felicidad: {self.felicidad}, energía: {self.energia}, hambre: {self.hambre}.")

    def comer(self, incremento, decremento):
        self.hambre -= decremento
        if self.hambre < 0:
            self.hambre = 0
        self.energia += incremento
        if self.energia > 100:
            self.energia = 100
        print(f"¡{self.nombre} devoró su comida con ganas! Ya no tiene tanta hambre.")
        print(f"felicidad: {self.felicidad}, energía: {self.energia}, hambre: {self.hambre}.")

    def dormir(self, incremento, decremento):
        self.energia += incremento
        if self.energia > 100:
            self.energia = 100
        self.felicidad -= decremento
        if self.felicidad < 0:
            self.felicidad = 0
        self.hambre -= decremento
        if self.hambre < 0:
            self.hambre = 0
        print(f"¡{self.nombre} está echando una siesta! Se ve más enérgico.")
        print(f"felicidad: {self.felicidad}, energía: {self.energia}, hambre: {self.hambre}.")

    def mostrar_estado(self):
        print(f"nombre: {self.nombre}, especie: {self.especie}, felicidad: {self.felicidad}, energía: {self.energia}, hambre: {self.hambre}.")
        if self.hambre < 50:
            print(f"¡{self.nombre} está muy hambriento!")
        if self.felicidad > 80:
            print(f"¡{self.nombre} está radiante de felicidad!")

print("Proyecto Mascota")
especie = input("¿Qué tipo de criatura es tu mascota? (perro - gato - dragón - robot - extraterrestre) ")
nombre = input("¿Qué nombre tiene tu mascota? ")
mascota1 = Mascota(nombre, especie)
print("1 - Mostrar estado.")
print("2 - Jugar.")
print("3 - Comer.")
print("4 - Dormir.")
print("5 - Salir del juego.")
while True:
    accion = input("¿Qué te gustaría hacer ahora? ")
    if accion == "1":
        mascota1.mostrar_estado()
    elif accion == "2":
        mascota1.jugar(15,10)
    elif accion == "3":
        mascota1.comer(20,15)
    elif accion == "4":
        mascota1.dormir(15,5)
    elif accion == "5":
        break