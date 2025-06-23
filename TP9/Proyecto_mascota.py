class Mascota:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
        self.felicidad = 75
        self.energia = 75
        self.hambre = 75

    def jugar(self, incremento, decremento):
        self.felicidad += incremento
        self.energia, self.hambre -= decremento
        print(f"¡{self.nombre} corretea feliz! Su felicidad subió.")

    def comer(self, incremento, decremento):
        self.hambre -= decremento
        self.energia += incremento
        print(f"¡{self.nombre} devoró su comida con ganas! Ya no tiene tanta hambre.")

    def dormir(self, incremento, decremento):
        self.energia += incremento
        self.felicidad, self.hambre -= decremento
        print(f"¡{self.nombre} está echando una siesta! Se ve más enérgico.")

    def mostrar_estado(self):
        print(f"nombre: {self.nombre}, especie: {self.especie}, felicidad: {self.felicidad}, energía: {self.energia}, hambre: {self.hambre}.")
        print(f"¡{self.nombre} está muy hambriento!")
        print(f"¡{self.nombre} está radiante de felicidad!")