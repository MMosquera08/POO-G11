"""
Ejemplo completo de generación de códigos QR con Python
========================================================

Este script muestra cómo configurar diferentes parámetros de un código QR:
- Tamaño de matriz
- Nivel de corrección de errores
- Codificación
- Tamaño en píxeles
- Colores y estilos
- Gradientes y transparencias
- Formas personalizadas
- Zona de silencio
- Inserción de logotipo
- Formato de salida

Autor: Para estudiantes de programación
"""

import qrcode
from PIL import Image, ImageDraw
import io
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer, CircleModuleDrawer, SquareModuleDrawer

# Las formas personalizadas están disponibles, pero los gradientes no
STYLED_QR_AVAILABLE = True
ADVANCED_STYLES_AVAILABLE = False  # Los gradientes no están disponibles en esta versión

def generar_qr_basico():
    """
    Ejemplo básico de código QR con configuraciones principales
    """
    print("🔹 Generando código QR básico...")
    
    # CONFIGURACIÓN BÁSICA DEL QR
    qr = qrcode.QRCode(
        # Tamaño de la matriz (1-40, donde 1 es la más pequeña)
        version=1,  # Descomenta para cambiar: version=5
        
        # Nivel de corrección de errores
        # L: ~7% | M: ~15% | Q: ~25% | H: ~30%
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        # error_correction=qrcode.constants.ERROR_CORRECT_H,  # Mayor corrección
        
        # Tamaño de cada módulo en píxeles
        box_size=10,  # Cambia a 15 o 20 para módulos más grandes
        
        # Zona de silencio (borde blanco alrededor del QR)
        border=4,  # Cambia a 2 para menos borde o 8 para más borde
    )
    
    # CONTENIDO DEL QR
    datos = "¡Hola estudiantes del ISP! 👋" 
    
    qr.add_data(datos)
    qr.make(fit=True)
    
    # GENERACIÓN DE IMAGEN BÁSICA
    img = qr.make_image(
        fill_color="black",     # Color de los módulos
        back_color="white"      # Color de fondo
    )
    
    # Guardar imagen
    img.save("/home/pirum/san_pablo/repos/Tareas/TP11/qr_basico.png")
    print("✅ QR básico guardado como 'qr_basico.png'")
    
    return qr

def generar_qr_colores():
    """
    Ejemplo con colores personalizados
    """
    print("\n🎨 Generando código QR con colores personalizados...")
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=12,
        border=4,
    )
    
    qr.add_data("Código QR con colores personalizados")
    qr.make(fit=True)
    
    # COLORES PERSONALIZADOS
    img = qr.make_image(
        fill_color="#2E86AB",      # Azul para módulos
        back_color="#F24236"       # Rojo para fondo
        # fill_color="#FF6B6B",    # Rojo coral
        # back_color="#4ECDC4"     # Verde agua
        # fill_color="purple",     # Púrpura
        # back_color="lightgray"   # Gris claro
    )
    
    img.save("/home/pirum/san_pablo/repos/Tareas/TP11/qr_colores.png")
    print("✅ QR con colores guardado como 'qr_colores.png'")

def generar_qr_con_estilo():
    """
    Ejemplo con formas personalizadas de módulos
    """
    print("\n✨ Generando código QR con formas personalizadas...")
    
    qr = qrcode.QRCode(
        version=2,  # Matriz más grande para mejor visualización de estilos
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Alta corrección
        box_size=15,
        border=4,
    )
    
    qr.add_data("QR con formas personalizadas - Módulos redondeados")
    qr.make(fit=True)
    
    # FORMAS PERSONALIZADAS DE MÓDULOS
    # Descomenta la forma que quieras usar:
    
    # 1. Módulos redondeados (activo por defecto)
    drawer = RoundedModuleDrawer()
    
    # 2. Módulos circulares (descomenta para usar)
    # drawer = CircleModuleDrawer()
    
    # 3. Módulos cuadrados tradicionales (descomenta para usar)
    # drawer = SquareModuleDrawer()
    
    # GENERAR IMAGEN CON FORMAS PERSONALIZADAS Y COLORES
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=drawer,
        fill_color="#4A90E2",      # Azul para módulos
        back_color="#F0F8FF"       # Azul muy claro para fondo
        # fill_color="#FF6B6B",    # Rojo coral (descomenta para usar)
        # back_color="#FFE5B4"     # Melocotón claro (descomenta para usar)
        # fill_color="#32CD32",    # Verde lima (descomenta para usar)  
        # back_color="#F0FFF0"     # Verde muy claro (descomenta para usar)
    )
    
    img.save("/home/pirum/san_pablo/repos/Tareas/TP11/qr_estilizado.png")
    print("✅ QR estilizado guardado como 'qr_estilizado.png'")

def generar_qr_con_logo():
    """
    Ejemplo con logotipo en el centro
    """
    print("\n🖼️  Generando código QR con logotipo...")
    
    qr = qrcode.QRCode(
        version=3,  # Versión más grande para acomodar el logo
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Alta corrección necesaria para logo
        box_size=10,
        border=4,
    )
    
    qr.add_data("QR con logotipo - Mayor corrección de errores")
    qr.make(fit=True)
    
    # Generar QR base
    img = qr.make_image(fill_color="black", back_color="white")
    
    # CREAR UN LOGO SIMPLE (círculo con texto)
    # En un proyecto real, cargarías: logo = Image.open("mi_logo.png")
    logo_size = 60
    logo = Image.new('RGBA', (logo_size, logo_size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(logo)
    
    # Dibujar círculo de fondo
    draw.ellipse([5, 5, logo_size-5, logo_size-5], fill=(255, 100, 100, 255))
    
    # Convertir a RGB para compatibilidad
    logo = logo.convert('RGB')
    
    # INSERTAR LOGO EN EL CENTRO DEL QR
    # Calcular posición central
    img = img.convert('RGB')
    pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
    
    # Pegar el logo
    img.paste(logo, pos)
    
    img.save("/home/pirum/san_pablo/repos/Tareas/TP11/qr_con_logo.png")
    print("✅ QR con logo guardado como 'qr_con_logo.png'")

def generar_qr_transparente():
    """
    Ejemplo con transparencia y efectos especiales
    """
    print("\n🌈 Generando código QR con transparencia...")
    
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=12,
        border=4,
    )
    
    qr.add_data("QR con efectos de transparencia")
    qr.make(fit=True)
    
    # Generar imagen base
    img = qr.make_image(fill_color="black", back_color="white")
    
    # CONVERTIR A RGBA PARA MANEJAR TRANSPARENCIA
    img = img.convert('RGBA')
    
    # Crear una nueva imagen con fondo transparente
    transparent_img = Image.new('RGBA', img.size, (255, 255, 255, 0))
    
    # APLICAR TRANSPARENCIA A LOS MÓDULOS
    data = img.getdata()
    new_data = []
    
    for pixel in data:
        # Si es negro (módulo), hacerlo semi-transparente azul
        if pixel[0] < 128:  # Píxel oscuro
            new_data.append((0, 100, 200, 180))  # Azul semi-transparente
        else:  # Píxel claro (fondo)
            new_data.append((255, 255, 255, 50))   # Blanco muy transparente
            # new_data.append((255, 255, 255, 0))   # Totalmente transparente
    
    transparent_img.putdata(new_data)
    
    # Guardar como PNG para preservar transparencia
    transparent_img.save("/home/pirum/san_pablo/repos/Tareas/TP11/qr_transparente.png")
    print("✅ QR transparente guardado como 'qr_transparente.png'")

def mostrar_configuraciones_avanzadas():
    """
    Muestra ejemplos de todas las configuraciones comentadas
    """
    print("\n📚 CONFIGURACIONES AVANZADAS DISPONIBLES:")
    print("=" * 50)
    
    print("\n🔢 TAMAÑOS DE MATRIZ (version):")
    print("  version=1  -> 21x21 módulos (más pequeño)")
    print("  version=5  -> 37x37 módulos") 
    print("  version=10 -> 57x57 módulos")
    print("  version=40 -> 177x177 módulos (más grande)")
    
    print("\n🛡️  NIVELES DE CORRECCIÓN DE ERRORES:")
    print("  ERROR_CORRECT_L -> ~7%  corrección (menos robusto)")
    print("  ERROR_CORRECT_M -> ~15% corrección (recomendado)")
    print("  ERROR_CORRECT_Q -> ~25% corrección")
    print("  ERROR_CORRECT_H -> ~30% corrección (para logos)")
    
    print("\n📏 TAMAÑO DE MÓDULOS (box_size):")
    print("  box_size=5  -> Módulos pequeños")
    print("  box_size=10 -> Tamaño estándar") 
    print("  box_size=20 -> Módulos grandes")
    
    print("\n🎨 FORMAS DE MÓDULOS:")
    print("  RoundedModuleDrawer() -> Esquinas redondeadas")
    print("  CircleModuleDrawer()  -> Círculos")
    print("  SquareModuleDrawer()  -> Cuadrados tradicionales")
    
    print("\n🌈 COLORES PERSONALIZADOS:")
    print("  fill_color='#4A90E2'  -> Azul para módulos")
    print("  back_color='#F0F8FF'  -> Azul claro para fondo")
    print("  fill_color='#FF6B6B'  -> Rojo coral para módulos")
    print("  back_color='#FFE5B4'  -> Melocotón para fondo")
    print("  fill_color='#32CD32'  -> Verde lima para módulos")
    
    print("\n⚠️  NOTA: Los gradientes avanzados no están disponibles en esta versión")
    
    print("\n💾 FORMATOS DE SALIDA:")
    print("  .png -> Mejor para web y transparencias")
    print("  .jpg -> Menor tamaño de archivo")
    print("  .svg -> Vectorial, escalable sin pérdida")
    print("  .pdf -> Para documentos")

def main():
    """
    Función principal que ejecuta todos los ejemplos
    """
    print("🚀 GENERADOR DE CÓDIGOS QR - EJEMPLOS EDUCATIVOS")
    print("=" * 55)
    
    # Crear directorio si no existe
    import os
    os.makedirs("/home/pirum/san_pablo/repos/Tareas/TP11", exist_ok=True)
    
    # Ejecutar todos los ejemplos
    generar_qr_basico()
    generar_qr_colores()
    generar_qr_con_estilo()
    generar_qr_con_logo()
    generar_qr_transparente()
    
    # Mostrar información educativa
    mostrar_configuraciones_avanzadas()
    
    print("\n🎉 ¡Todos los ejemplos generados exitosamente!")
    print("📁 Archivos guardados en: /home/pirum/san_pablo/repos/Tareas/TP11/")
    print("\n💡 PARA EXPERIMENTAR:")
    print("   1. Descomenta diferentes configuraciones en el código")
    print("   2. Cambia los valores de los parámetros")
    print("   3. Prueba diferentes combinaciones de colores y estilos")
    print("   4. Experimenta con diferentes niveles de corrección")

# INSTRUCCIONES PARA INSTALAR DEPENDENCIAS
"""
Para ejecutar este código, instala las dependencias necesarias:

pip install qrcode
pip install pillow

O si usas conda:
conda install -c conda-forge qrcode pillow
"""

if __name__ == "__main__":
    main()