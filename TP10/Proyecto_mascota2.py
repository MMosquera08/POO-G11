import random
import time

class Mascota:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
        self.felicidad = 75
        self.energia = 75
        self.hambre = 75
        self.edad = 0
        self.nivel = 1
        self.puntos = 0

    def mini_juego_cazar_raton(self):
        """Mini juego: El gato debe cazar ratones"""
        print(f"\n🎮 === MINI JUEGO: CAZA DE RATONES ===")
        print(f"🐭 ¡Ayuda a {self.nombre} a cazar ratones!")
        print("💡 Instrucciones: Elige la dirección correcta (izquierda/derecha)")
        
        puntos_juego = 0
        rondas = 3
        
        for ronda in range(1, rondas + 1):
            print(f"\n🎯 RONDA {ronda}/{rondas}")
            raton_posicion = random.choice(["izquierda", "derecha"])
            
            print("🐭 ¡Un ratón aparece!")
            time.sleep(1)
            print("🏃‍♂️ El ratón corre hacia la... ¡¿izquierda o derecha?!")
            
            respuesta = input("👈 Escribe 'izquierda' o 'derecha': ").lower().strip()
            
            if respuesta == raton_posicion:
                print(f"🎉 ¡Excelente! {self.nombre} atrapó al ratón!")
                puntos_juego += 10
            else:
                print(f"😿 ¡Oh no! El ratón escapó hacia la {raton_posicion}")
                puntos_juego += 2  # Puntos de consolación
        
        self.puntos += puntos_juego
        bonus_felicidad = min(20, puntos_juego)
        self.felicidad += bonus_felicidad
        if self.felicidad > 100:
            self.felicidad = 100
            
        print(f"\n🏆 ¡Juego terminado!")
        print(f"📊 Puntos obtenidos: {puntos_juego}")
        print(f"💰 Puntos totales: {self.puntos}")
        print(f"😸 Felicidad +{bonus_felicidad}")
        
        return puntos_juego

    def mini_juego_saltar_obstaculos(self):
        """Mini juego: El gato debe saltar obstáculos"""
        print(f"\n🎮 === MINI JUEGO: SALTAR OBSTÁCULOS ===")
        print(f"🏃‍♀️ ¡{self.nombre} debe saltar obstáculos!")
        print("💡 Instrucciones: Escribe 'saltar' cuando veas un obstáculo")
        
        puntos_juego = 0
        obstaculos = 4
        
        for i in range(1, obstaculos + 1):
            print(f"\n🎯 OBSTÁCULO {i}/{obstaculos}")
            
            # Crear expectativa
            for j in range(3):
                print("🏃‍♀️" + "." * j, end="\r")
                time.sleep(0.5)
            
            # Momento del obstáculo
            if random.choice([True, False]):  # 50% chance de obstáculo
                print("🚧 ¡OBSTÁCULO! ", end="")
                respuesta = input("¿Qué haces? ").lower().strip()
                
                if "saltar" in respuesta or "salto" in respuesta:
                    print(f"🦘 ¡Perfecto salto! {self.nombre} esquiva el obstáculo")
                    puntos_juego += 15
                else:
                    print(f"💥 ¡Auch! {self.nombre} tropezó un poco")
                    puntos_juego += 5
            else:
                print("✅ Camino libre, ¡sigue corriendo!")
                input("Presiona ENTER para continuar...")
                puntos_juego += 8
        
        self.puntos += puntos_juego
        bonus_energia = min(15, puntos_juego // 2)
        self.energia += bonus_energia
        if self.energia > 100:
            self.energia = 100
            
        print(f"\n🏆 ¡Carrera completada!")
        print(f"📊 Puntos obtenidos: {puntos_juego}")
        print(f"💰 Puntos totales: {self.puntos}")
        print(f"⚡ Energía +{bonus_energia}")
        
        return puntos_juego

    def mini_juego_encontrar_comida(self):
        """Mini juego: Encontrar comida escondida"""
        print(f"\n🎮 === MINI JUEGO: BUSCAR COMIDA ===")
        print(f"🔍 ¡{self.nombre} debe encontrar comida escondida!")
        print("💡 Instrucciones: Elige dónde buscar comida")
        
        lugares = ["cocina", "sala", "jardín", "dormitorio"]
        comida_lugar = random.choice(lugares)
        intentos = 3
        puntos_juego = 0
        encontrado = False
        
        while intentos > 0 and not encontrado:
            print(f"\n🎯 Te quedan {intentos} intentos")
            print("🏠 Lugares disponibles:", ", ".join(lugares))
            
            respuesta = input("🔍 ¿Dónde quieres buscar? ").lower().strip()
            
            if respuesta == comida_lugar:
                print(f"🎉 ¡Encontrado! Había deliciosa comida en la {comida_lugar}!")
                puntos_juego = 20 + (intentos * 5)  # Más puntos si encuentra rápido
                encontrado = True
            else:
                intentos -= 1
                if respuesta in lugares:
                    print(f"😿 No hay nada en la {respuesta}...")
                    puntos_juego += 3  # Puntos por intentar
                else:
                    print("❌ Ese lugar no existe, intenta con: cocina, sala, jardín, dormitorio")
                    intentos += 1  # No pierde intento por lugar inválido
        
        if not encontrado:
            print(f"😔 No encontraste la comida, pero {self.nombre} aprecia el esfuerzo")
            puntos_juego += 10  # Puntos de consolación
        
        self.puntos += puntos_juego
        bonus_hambre = min(25, puntos_juego)
        self.hambre -= bonus_hambre
        if self.hambre < 0:
            self.hambre = 0
            
        print(f"\n🏆 ¡Búsqueda terminada!")
        print(f"📊 Puntos obtenidos: {puntos_juego}")
        print(f"💰 Puntos totales: {self.puntos}")
        print(f"🍽️ Hambre -{bonus_hambre}")
        
        return puntos_juego

    def elegir_mini_juego(self):
        """Permite al jugador elegir qué mini juego jugar"""
        print(f"\n🎮 === MINI JUEGOS DISPONIBLES ===")
        print("1️⃣  - 🐭 Cazar Ratones (Aumenta felicidad)")
        print("2️⃣  - 🏃‍♀️ Saltar Obstáculos (Aumenta energía)")
        print("3️⃣  - 🔍 Buscar Comida (Reduce hambre)")
        print("4️⃣  - 🎲 Juego Aleatorio")
        print("5️⃣  - 🔙 Volver al menú principal")
        
        while True:
            opcion = input("🎯 ¿Qué mini juego quieres jugar? ").strip()
            
            if opcion == "1":
                self.mini_juego_cazar_raton()
                break
            elif opcion == "2":
                self.mini_juego_saltar_obstaculos()
                break
            elif opcion == "3":
                self.mini_juego_encontrar_comida()
                break
            elif opcion == "4":
                # Juego aleatorio
                juegos = [self.mini_juego_cazar_raton, self.mini_juego_saltar_obstaculos, self.mini_juego_encontrar_comida]
                random.choice(juegos)()
                break
            elif opcion == "5":
                return
            else:
                print("❌ Opción no válida. Elige un número del 1 al 5.")

    def jugar(self, incremento=15, decremento=10):
        # Preguntar si quiere mini juego o juego normal
        print(f"\n🎾 ¡Hora de jugar con {self.nombre}!")
        print("1️⃣  - 🎮 Mini Juegos Interactivos")
        print("2️⃣  - 🎾 Juego Clásico")
        
        while True:
            opcion = input("🎯 ¿Cómo quieres jugar? ").strip()
            
            if opcion == "1":
                self.elegir_mini_juego()
                return
            elif opcion == "2":
                # Juego clásico original
                mensajes_jugar = [
                    f"¡{self.nombre} persigue una pelota de lana con gran entusiasmo!",
                    f"¡{self.nombre} salta y corretea por toda la casa!",
                    f"¡{self.nombre} juega con sus juguetes favoritos!",
                    f"¡{self.nombre} hace travesuras y se divierte muchísimo!"
                ]
                
                self.felicidad += incremento
                if self.felicidad > 100:
                    self.felicidad = 100
                self.energia -= decremento
                if self.energia < 0:
                    self.energia = 0
                self.hambre -= decremento
                if self.hambre < 0:
                    self.hambre = 0
                self.edad += 1
                
                print("🎾 " + random.choice(mensajes_jugar))
                time.sleep(1)
                print(f"😸 Felicidad: {self.felicidad}/100 | ⚡ Energía: {self.energia}/100 | 🍽️ Hambre: {self.hambre}/100")
                self._verificar_nivel()
                return
            else:
                print("❌ Opción no válida. Elige 1 o 2.")

    def comer(self, incremento=20, decremento=15):
        # Mensajes aleatorios para comer
        mensajes_comer = [
            f"¡{self.nombre} devora su comida con muchísimas ganas!",
            f"¡{self.nombre} ronronea mientras come su delicioso festín!",
            f"¡{self.nombre} disfruta cada bocado de su comida favorita!",
            f"¡{self.nombre} lame el plato hasta dejarlo brillante!"
        ]
        
        self.hambre -= decremento
        if self.hambre < 0:
            self.hambre = 0
        self.energia += incremento
        if self.energia > 100:
            self.energia = 100
        self.edad += 1
        
        print("🍖 " + random.choice(mensajes_comer))
        time.sleep(1)
        print(f"😸 Felicidad: {self.felicidad}/100 | ⚡ Energía: {self.energia}/100 | 🍽️ Hambre: {self.hambre}/100")
        self._verificar_nivel()
        
        # Consejos después de comer
        if self.hambre == 0:
            print("💡 CONSEJO: ¡Perfecto! Tu gato está completamente satisfecho.")
        elif self.energia > 90:
            print("💡 CONSEJO: Tu gato tiene mucha energía después de comer, ¡hora de jugar!")

    def dormir(self, incremento=15, decremento=5):
        # Mensajes aleatorios para dormir
        mensajes_dormir = [
            f"¡{self.nombre} se acurruca en su lugar favorito para una siesta!",
            f"¡{self.nombre} ronronea suavemente mientras duerme!",
            f"¡{self.nombre} estira sus patitas y se relaja profundamente!",
            f"¡{self.nombre} encuentra el rayo de sol perfecto para dormir!"
        ]
        
        self.energia += incremento
        if self.energia > 100:
            self.energia = 100
        self.felicidad -= decremento
        if self.felicidad < 0:
            self.felicidad = 0
        self.hambre -= decremento
        if self.hambre < 0:
            self.hambre = 0
        self.edad += 1
        
        print("😴 " + random.choice(mensajes_dormir))
        time.sleep(1)
        print(f"😸 Felicidad: {self.felicidad}/100 | ⚡ Energía: {self.energia}/100 | 🍽️ Hambre: {self.hambre}/100")
        self._verificar_nivel()

    def _verificar_nivel(self):
        nuevo_nivel = (self.edad // 10) + 1
        if nuevo_nivel > self.nivel:
            self.nivel = nuevo_nivel
            print(f"🎉 ¡{self.nombre} ha subido al nivel {self.nivel}! ¡Está creciendo!")

    def dar_consejos_automaticos(self):
        """Da consejos automáticos basados en el estado del gato"""
        consejos = []
        
        # Consejos basados en hambre
        if self.hambre > 70:
            consejos.append(f"🍖 CONSEJO: {self.nombre} tiene mucha hambre, ¡aliméntalo pronto!")
        elif self.hambre > 50:
            consejos.append(f"🤤 CONSEJO: {self.nombre} podría comer algo...")
        
        # Consejos basados en energía
        if self.energia < 30:
            consejos.append(f"😴 CONSEJO: {self.nombre} está muy cansado, ¡necesita dormir!")
        elif self.energia < 50:
            consejos.append(f"💤 CONSEJO: Una siesta le vendría bien a {self.nombre}")
        elif self.energia > 80:
            consejos.append(f"⚡ CONSEJO: {self.nombre} tiene mucha energía, ¡perfecto para jugar!")
        
        # Consejos basados en felicidad
        if self.felicidad < 30:
            consejos.append(f"😿 CONSEJO: {self.nombre} está muy triste, ¡juega con él!")
        elif self.felicidad < 50:
            consejos.append(f"🎾 CONSEJO: {self.nombre} se ve aburrido, ¿qué tal si juegan?")
        
        # Consejos combinados
        if self.energia > 70 and self.felicidad < 70:
            consejos.append(f"🎯 CONSEJO ESTRATÉGICO: {self.nombre} tiene energía pero poca felicidad, ¡jugar sería perfecto!")
        
        if self.hambre < 30 and self.energia < 50:
            consejos.append(f"🍖💤 CONSEJO COMBINADO: {self.nombre} necesita comer Y descansar")
        
        # Consejo positivo si está bien
        if all(valor > 60 for valor in [self.felicidad, self.energia, 100-self.hambre]):
            consejos.append(f"🌟 ¡Excelente! {self.nombre} está muy bien cuidado, ¡sigue así!")
        
        # Mostrar consejos
        if consejos:
            print("\n💡 === CONSEJOS AUTOMÁTICOS ===")
            for consejo in consejos:
                print(consejo)
            print("=" * 35)

    def mostrar_estado(self):
        print(f"\n🐱 === ESTADO DE {self.nombre.upper()} ===")
        print(f"📝 Nombre: {self.nombre}")
        print(f"🦁 Especie: {self.especie}")
        print(f"🎂 Edad: {self.edad} días")
        print(f"⭐ Nivel: {self.nivel}")
        print(f"💰 Puntos: {self.puntos}")
        print(f"😸 Felicidad: {self.felicidad}/100")
        print(f"⚡ Energía: {self.energia}/100")
        print(f"🍽️ Hambre: {self.hambre}/100")
        
        # Estados especiales
        if self.hambre < 30:
            print(f"🍽️ ¡{self.nombre} está MUY hambriento! ¡Necesita comida urgente!")
        elif self.hambre < 50:
            print(f"🤤 {self.nombre} tiene un poco de hambre...")
            
        if self.energia < 30:
            print(f"😴 ¡{self.nombre} está muy cansado! Necesita descansar.")
        elif self.energia > 80:
            print(f"⚡ ¡{self.nombre} está lleno de energía!")
            
        if self.felicidad > 90:
            print(f"🌟 ¡{self.nombre} está RADIANTE de felicidad!")
        elif self.felicidad < 30:
            print(f"😿 {self.nombre} se ve muy triste... necesita atención.")
            
        # Logros especiales
        if self.felicidad >= 100:
            print("🏆 ¡LOGRO DESBLOQUEADO: Felicidad Máxima!")
        if self.energia >= 100:
            print("🏆 ¡LOGRO DESBLOQUEADO: Energía Máxima!")
        if self.hambre == 0:
            print("🏆 ¡LOGRO DESBLOQUEADO: Completamente Satisfecho!")
        if self.puntos >= 100:
            print("🏆 ¡LOGRO DESBLOQUEADO: Maestro de Mini Juegos!")
        
        # CONSEJOS AUTOMÁTICOS después de mostrar el estado
        self.dar_consejos_automaticos()

def mostrar_menu():
    print("\n" + "="*40)
    print("🎮 MENÚ DE CUIDADO GATUNO")
    print("="*40)
    print("1️⃣  - Mostrar estado")
    print("2️⃣  - Jugar (Con mini juegos)")
    print("3️⃣  - Comer")
    print("4️⃣  - Dormir")
    print("5️⃣  - Consejos de cuidado")
    print("6️⃣  - Salir del juego")
    print("="*40)

def dar_consejos(mascota):
    print(f"\n💡 CONSEJOS PARA CUIDAR A {mascota.nombre}:")
    
    if mascota.hambre > 70:
        print("🍖 Tu gato tiene mucha hambre, ¡es hora de alimentarlo!")
    if mascota.energia < 40:
        print("😴 Tu gato necesita descansar, ¡una siesta le vendría bien!")
    if mascota.felicidad < 50:
        print("🎾 Tu gato se ve aburrido, ¡juega con él para animarlo!")
    if mascota.energia > 80 and mascota.felicidad < 80:
        print("⚡ Tu gato tiene mucha energía, ¡perfecto momento para jugar!")
    
    if all(valor > 70 for valor in [mascota.felicidad, mascota.energia, 100-mascota.hambre]):
        print("🌟 ¡Excelente trabajo! Tu gato está muy bien cuidado.")

# Inicio del juego
print("🐾" + "="*50 + "🐾")
print("        🎉 ¡BIENVENIDO AL SIMULADOR DE GATOS! 🎉")
print("🐾" + "="*50 + "🐾")
print("\n🐱 Tu nueva mascota será un adorable gato")

while True:
    nombre = input("\n🏷️  ¿Qué nombre le pondrás a tu gato? ").strip()
    if nombre:
        break
    print("❌ Por favor, ingresa un nombre válido para tu gato.")

mascota1 = Mascota(nombre, "gato")

print(f"\n🎊 ¡Perfecto! {nombre} está emocionado de conocerte.")
print("💫 ¡Tu aventura como cuidador de gatos comienza ahora!")
print("🎮 ¡NOVEDAD! Ahora incluye mini juegos interactivos")
time.sleep(2)

# Mostrar estado inicial
mascota1.mostrar_estado()

# Bucle principal del juego
while True:
    mostrar_menu()
    accion = input("🎯 ¿Qué quieres hacer? ").strip()
    
    if accion == "1":
        mascota1.mostrar_estado()
    elif accion == "2":
        mascota1.jugar()
    elif accion == "3":
        print(f"\n🍖 ¡Es hora de alimentar a {mascota1.nombre}!")
        time.sleep(1)
        mascota1.comer()
    elif accion == "4":
        print(f"\n😴 {mascota1.nombre} va a descansar...")
        time.sleep(1)
        mascota1.dormir()
    elif accion == "5":
        dar_consejos(mascota1)
    elif accion == "6":
        print(f"\n👋 ¡Hasta luego! {mascota1.nombre} te extrañará mucho.")
        print(f"🎖️  Estadísticas finales:")
        print(f"   📅 Días cuidados: {mascota1.edad}")
        print(f"   ⭐ Nivel alcanzado: {mascota1.nivel}")
        print(f"   💰 Puntos obtenidos: {mascota1.puntos}")
        print("🐾 ¡Gracias por jugar! 🐾")
        break
    else:
        print("❌ Opción no válida. Por favor, elige un número del 1 al 6.")
    
    # Pausa para mejor experiencia
    input("\n⏸️  Presiona ENTER para continuar...")