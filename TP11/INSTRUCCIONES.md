# 📱 Generador de Códigos QR - Guía para Estudiantes

## 🚀 Instalación de Dependencias

Antes de ejecutar el código, instala las librerías necesarias:

```bash

pip install qrcode pillow

```

## 📚 Qué aprenderás

Este ejemplo te enseñará a configurar:

### ⚙️ Parámetros Básicos
- **Tamaño de matriz** (`version`): De 1 (21x21) hasta 40 (177x177 módulos)
- **Corrección de errores**: L (~7%), M (~15%), Q (~25%), H (~30%)
- **Tamaño de módulos** (`box_size`): Píxeles por módulo
- **Zona de silencio** (`border`): Espacio blanco alrededor

### 🎨 Personalización Visual Disponible
- **Colores personalizados**: Módulos y fondo con códigos hexadecimales
- **Formas de módulos**: Cuadrados, círculos, esquinas redondeadas
- **Transparencias**: Efectos semi-transparentes con canal alfa
- **Logotipos**: Inserción programática en el centro
- **Combinaciones de colores**: Ejemplos predefinidos para experimentar

### 💾 Formatos de Salida
- **PNG**: Mejor para web y transparencias
- **JPG**: Menor tamaño de archivo
- **SVG**: Vectorial escalable (requiere configuración adicional)
- **PDF**: Para documentos (requiere configuración adicional)

## 🏃‍♂️ Cómo Usar

1. **Ejecuta el código completo**:
   ```bash
   python codigos_qr.py
   ```

2. **Experimenta con las configuraciones disponibles**:
   - Descomenta líneas en `generar_qr_con_estilo()` para probar diferentes formas
   - Cambia valores de `version`, `box_size`, `border`
   - Prueba diferentes combinaciones de colores hexadecimales
   - Modifica los niveles de corrección de errores

3. **Revisa los archivos generados**:
   - `qr_basico.png` - Configuración estándar en blanco y negro
   - `qr_colores.png` - Con colores personalizados
   - `qr_estilizado.png` - Con formas personalizadas (redondeadas por defecto)
   - `qr_con_logo.png` - Con logotipo circular en el centro
   - `qr_transparente.png` - Con efectos de transparencia

## 🎯 Características Implementadas

### ✅ Funcionalidades Disponibles
- **Formas de módulos**: RoundedModuleDrawer, CircleModuleDrawer, SquareModuleDrawer
- **Colores personalizados**: Códigos hexadecimales (#RRGGBB)
- **Transparencias**: Canal alfa RGBA
- **Logotipos**: Inserción programática con PIL
- **Configuración completa**: version, error_correction, box_size, border

### ⚠️ Limitaciones de la Versión Actual
- **Gradientes avanzados**: No disponibles en esta versión de qrcode
- **Rellenos especiales**: SquareGradiantColorFill, RadialGradiantColorFill no soportados
- **Solución**: Se usan colores sólidos con formas personalizadas como alternativa

## 🔧 Ejemplos de Experimentación

### Cambiar Formas de Módulos
```python
# En generar_qr_con_estilo(), descomenta una de estas líneas:
drawer = RoundedModuleDrawer()  # Esquinas redondeadas (por defecto)
# drawer = CircleModuleDrawer()  # Módulos circulares
# drawer = SquareModuleDrawer()  # Módulos cuadrados tradicionales
```

### Personalizar Colores
```python
# Experimenta con estos colores en cualquier función:
fill_color="#FF6B6B"    # Rojo coral para módulos
back_color="#4ECDC4"    # Verde agua para fondo
# O usa nombres: "red", "blue", "green", etc.
```

### Ajustar Tamaño y Corrección
```python
qr = qrcode.QRCode(
    version=5,              # Matriz más grande (37x37)
    box_size=20,           # Módulos más grandes
    border=2,              # Borde más pequeño
    error_correction=qrcode.constants.ERROR_CORRECT_H  # Máxima corrección
)
```

## 🎯 Objetivos Educativos

- **Comprender los parámetros** de configuración de códigos QR
- **Experimentar con estilos visuales** disponibles en la librería
- **Aprender sobre corrección de errores** y su importancia
- **Practicar manipulación de imágenes** con PIL/Pillow
- **Entender el balance** entre funcionalidad y estética
- **Explorar personalización** dentro de las limitaciones técnicas

## 🔧 Solución de Problemas

**Error de importación**: 
```bash
ModuleNotFoundError: No module named 'qrcode'
```
**Solución**: Instala las dependencias con `pip install qrcode pillow`

**QR no legible**: 
- Aumenta el nivel de corrección de errores a `ERROR_CORRECT_H`
- Reduce el tamaño del logo si usas uno
- Verifica que los colores tengan suficiente contraste

**Archivo muy grande**: 
- Reduce el `box_size` (ej: de 20 a 10)
- Usa una `version` más pequeña (ej: de 5 a 2)

**Estilos no funcionan**:
- Verifica que las importaciones estén correctas
- Usa solo las funcionalidades confirmadas como disponibles
- Revisa la documentación de tu versión específica de qrcode

## 📖 Recursos Adicionales

- **Documentación oficial**: https://pypi.org/project/qrcode/
- **PIL/Pillow docs**: https://pillow.readthedocs.io/
- **Códigos de colores**: https://htmlcolorcodes.com/
- **Especificación QR**: ISO/IEC 18004:2015
