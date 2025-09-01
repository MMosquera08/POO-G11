import qrcode
from PIL import Image, ImageDraw
import os
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer, CircleModuleDrawer, SquareModuleDrawer

class GeneradorQR:
    def __init__(self):
        self.version = 1
        self.error_correction = qrcode.constants.ERROR_CORRECT_M
        self.box_size = 10
        self.border = 4
        self.data = ""

    def generar_qr(self, version = 1, error_correction = 'M', box_size = 10, border = 4, data = ""):
        self.version = version
        self.error_correction = self.convertir_error_correction(error_correction)
        self.box_size = box_size
        self.border = border
        self.data = data

    def convertir_error_correction(self, nivel):
        niveles = {
            'L': qrcode.constants.ERROR_CORRECT_L,
            'M': qrcode.constants.ERROR_CORRECT_M,
            'Q': qrcode.constants.ERROR_CORRECT_Q,
            'H': qrcode.constants.ERROR_CORRECT_H
        }
        return niveles.get(nivel.upper(), qrcode.constants.ERROR_CORRECT_M)

    def generar_qr_basico(self, color_modulos = "black", color_fondo = "white", nombre_archivo = "qr_basico.png"):
        print("Generando código QR básico...")

        # CONFIGURACIÓN BÁSICA DEL QR
        qr = qrcode.QRCode(
            version = self.version,
            error_correction = self.error_correction,
            box_size = self.box_size,
            border = self.border
            )
        
        # CONTENIDO DEL QR
        qr.add_data(self.data)
        qr.make(fit=True)
        
        # GENERACIÓN DE IMAGEN BÁSICA
        img = qr.make_image(
            fill_color = color_modulos,
            back_color = color_fondo
            )
        img.save(f"{nombre_archivo}")
        print(f"QR básico guardado como '{nombre_archivo}'")
        return img
    
    def generar_qr_con_estilo(self, estilo = "redondeado", color_modulos = "#2E86AB", color_fondo = "#F24236", nombre_archivo = "qr_con_estilo.png"):
        print("Generando código QR con colores personalizados...")
        qr = qrcode.QRCode(
            version = self.version,
            error_correction = self.error_correction,
            box_size = self.box_size,
            border = self.border,
            )
        qr.add_data(self.data)
        qr.make(fit=True)
        if estilo.lower() == "redondeado":
            drawer = RoundedModuleDrawer()
        elif estilo.lower() == "circular":
            drawer = CircleModuleDrawer()
        else:
            drawer = SquareModuleDrawer()
        img = qr.make_image(
            image_factory = StyledPilImage,
            module_drawer = drawer,
            fill_color = color_modulos,
            back_color = color_fondo
        )
        img.save(f"{nombre_archivo}")
        print(f"QR con estilo guardado como '{nombre_archivo}'")
        return img
        
    def generar_qr_con_logo(self, color_logo = (255, 100, 100), nombre_archivo = "qr_con_logo.png"):
        print("Generando código QR con logotipo...")
        qr = qrcode.QRCode(
            version = self.version,
            error_correction = qrcode.constants.ERROR_CORRECT_H,
            box_size = self.box_size,
            border = self.border,
            )
        qr.add_data(self.data)
        qr.make(fit=True)
        img = qr.make_image(fill_color = "black", back_color = "white")
        img = img.convert('RGB')
        
        # CREAR UN LOGO SIMPLE
        logo_size = 60
        logo = Image.new('RGB', (logo_size, logo_size), (255, 255, 255))
        draw = ImageDraw.Draw(logo)

        # INSERTAR LOGO EN EL CENTRO DEL QR
        draw.ellipse([5, 5, logo_size-5, logo_size-5], fill = color_logo)
        pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
        img.paste(logo, pos)
        img.save(f"{nombre_archivo}")
        print(f"QR con logo guardado como '{nombre_archivo}'")
        return img
    
    def mostrar_configuracion_actual(self):
        print("CONFIGURACIÓN ACTUAL:")
        print(f"Versión (tamaño): {self.version}")
        print(f"Corrección de errores: {self.error_correction}")
        print(f"Tamaño de módulos: {self.box_size}")
        print(f"Borde: {self.border}")
        print(f"Datos: '{self.data}'")

def mostrar_menu():
    print("GENERADOR DE CÓDIGOS QR")
    print("1. Configurar parámetros del QR")
    print("2. Generar QR básico")
    print("3. Generar QR estilizado")
    print("4. Generar QR con logo")
    print("5. Ver configuración actual")
    print("6. Ver ayuda")
    print("0. Salir")

def obtener_datos_qr():
    print("INGRESA LOS DATOS PARA EL QR:")
    while True:
        datos = input("Escribe el texto o URL: ").strip()
        if datos:
            return datos
        print("¡Debes ingresar algún texto o URL!")

def configurar_parametros(generador):
    print("CONFIGURACIÓN DE PARÁMETROS:")
    print("Tamaño de la matriz (1-40, donde 1 es la más pequeña):")
    try:
        version = int(input(f"Versión actual: {generador.version} | Nueva versión (1-40): ") or generador.version)
        generador.version = max(1, min(40, version))
    except ValueError:
        print("Valor inválido, manteniendo configuración actual")
    print("Nivel de corrección de errores:")
    print("L: ~7% | M: ~15% | Q: ~25% | H: ~30%")
    error = input(f"Nivel actual: {generador.error_correction} | Nuevo nivel (L/M/Q/H): ").upper()
    if error in ['L', 'M', 'Q', 'H']:
        generador.error_correction = generador.convertir_error_correction(error)
    print("Tamaño de cada módulo en píxeles:")
    try:
        box_size = int(input(f"Tamaño actual: {generador.box_size} | Nuevo tamaño (5-25): ") or generador.box_size)
        generador.box_size = max(5, min(25, box_size))
    except ValueError:
        print("Valor inválido, manteniendo configuración actual")
    print("Tamaño de la zona de silencio:")
    try:
        border = int(input(f"Borde actual: {generador.border} | Nuevo borde (1-10): ") or generador.border)
        generador.border = max(1, min(10, border))
    except ValueError:
        print("Valor inválido, manteniendo configuración actual")
    print("Configuración actualizada!")

def elegir_colores():
    print("COLORES DISPONIBLES:")
    colores = {
        '1': ('black', 'white'),
        '2': ('#FF6B6B', '#FFE5B4'),
        '3': ('#4A90E2', '#F0F8FF'),
        '4': ('#32CD32', '#F0FFF0'),
        '5': ('#9B59B6', '#F8F0FF'),
        '6': ('#FF8C00', '#FFF8E1')
    }
    print("1. Negro sobre blanco")
    print("2. Rojo coral sobre melocotón")
    print("3. Azul sobre azul claro")
    print("4. Verde lima sobre verde claro")
    print("5. Púrpura sobre lila")
    print("6. Naranja sobre crema")
    eleccion = input("Elige una opción (1-6): ")
    return colores.get(eleccion, ('black', 'white'))

def mostrar_ayuda():
    print("AYUDA - GENERADOR DE CÓDIGOS QR")
    print("TAMAÑOS DE MATRIZ (version):")
    print("version = 1 -> 21x21 módulos (más pequeño)")
    print("version = 5 -> 37x37 módulos") 
    print("version = 10 -> 57x57 módulos")
    print("version = 40 -> 177x177 módulos (más grande)")
    print("NIVELES DE CORRECCIÓN DE ERRORES:")
    print("ERROR_CORRECT_L -> ~7%  corrección (menos robusto)")
    print("ERROR_CORRECT_M -> ~15% corrección (recomendado)")
    print("ERROR_CORRECT_Q -> ~25% corrección")
    print("ERROR_CORRECT_H -> ~30% corrección (para logos)")
    print("FORMAS DE MÓDULOS:")
    print("RoundedModuleDrawer() -> Esquinas redondeadas")
    print("CircleModuleDrawer() -> Círculos")
    print("SquareModuleDrawer() -> Cuadrados tradicionales")

def main():
    os.makedirs("QR_Generados", exist_ok = True)
    os.chdir("QR_Generados")
    generador = GeneradorQR()
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            configurar_parametros(generador)
        elif opcion == '2':
            if not generador.data:
                generador.data = obtener_datos_qr()
            color_modulos, color_fondo = elegir_colores()
            nombre = input("Nombre del archivo (sin extensión): ") or "qr_basico"
            generador.generar_qr_basico(color_modulos, color_fondo, f"{nombre}.png")
            generador.data = ""
        elif opcion == '3':
            if not generador.data:
                generador.data = obtener_datos_qr()
            print("ESTILOS DISPONIBLES:")
            print("1. Redondeado")
            print("2. Circular") 
            print("3. Cuadrado")
            estilo_num = input("Elige estilo (1-3): ")
            estilos = {'1': 'redondeado', '2': 'circular', '3': 'cuadrado'}
            estilo = estilos.get(estilo_num, 'redondeado')
            color_modulos, color_fondo = elegir_colores()
            nombre = input("Nombre del archivo (sin extensión): ") or "qr_estilizado"
            generador.generar_qr_con_estilo(estilo, color_modulos, color_fondo, f"{nombre}.png")
            generador.data = ""
        elif opcion == '4':
            if not generador.data:
                generador.data = obtener_datos_qr()
            print("COLOR DEL LOGO:")
            print("1. Rojo  2. Azul  3. Verde  4. Púrpura  5. Naranja")
            color_num = input("Elige color (1-5): ")
            colores_logo = {
                '1': (255, 100, 100),
                '2': (100, 150, 255),
                '3': (100, 200, 100),
                '4': (150, 100, 200),
                '5': (255, 150, 50)
            }
            color_logo = colores_logo.get(color_num, (255, 100, 100))
            nombre = input("Nombre del archivo (sin extensión): ") or "qr_con_logo"
            generador.generar_qr_con_logo(color_logo, f"{nombre}.png")
            generador.data = ""
        elif opcion == '5':
            generador.mostrar_configuracion_actual()
        elif opcion == '6':
            mostrar_ayuda()
        elif opcion == '0':
            print("¡Gracias por usar el generador de QR!")
            break
        else:
            print("Opción no válida")
        input("Presiona Enter para continuar...")

if __name__ == "__main__":
    print("Instalación requerida:")
    print("pip install qrcode pillow")
    main()