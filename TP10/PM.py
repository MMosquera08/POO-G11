import pygame
import random
import math
import time
from enum import Enum

# Inicializar Pygame
pygame.init()
pygame.font.init()

# Constantes
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
FPS = 60

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (135, 206, 235)  # Sky blue
GREEN = (144, 238, 144)  # Light green
PURPLE = (147, 112, 219)  # Medium purple
PINK = (255, 182, 193)  # Light pink
ORANGE = (255, 165, 0)
RED = (255, 99, 71)
GRAY = (169, 169, 169)
DARK_GRAY = (64, 64, 64)
LIGHT_BLUE = (173, 216, 230)
YELLOW = (255, 255, 0)

# Estados de ánimo del gato
class Mood(Enum):
    HAPPY = "happy"
    SAD = "sad"
    HUNGRY = "hungry"
    SLEEPY = "sleepy"
    ENERGETIC = "energetic"
    NEUTRAL = "neutral"

# Colores de gato disponibles
CAT_COLORS = {
    "Marrón": (139, 69, 19),
    "Negro": (0, 0, 0),
    "Naranja": (255, 140, 0),
    "Gris": (128, 128, 128),
    "Blanco": (245, 245, 245)
}

class VirtualCat:
    def __init__(self, name, color_name):
        self.name = name
        self.color_name = color_name
        self.color = CAT_COLORS[color_name]
        self.happiness = 75
        self.energy = 75
        self.hunger = 75
        self.mood = Mood.NEUTRAL
        
        # Posición y animación
        self.x = WINDOW_WIDTH // 2
        self.y = WINDOW_HEIGHT // 2 - 50
        self.base_y = self.y
        self.animation_offset = 0
        self.scale = 1.0
        self.target_scale = 1.0
        self.last_time_decay = time.time()
        
        # Variables para animaciones de expresión
        self.blink_timer = 0
        self.is_blinking = False
        self.tail_angle = 0
        self.ear_angle = 0
        self.purr_animation = 0
        
    def update_mood(self):
        if self.happiness < 30 or self.hunger < 30:
            self.mood = Mood.SAD
        elif self.energy < 30:
            self.mood = Mood.SLEEPY
        elif self.hunger < 50:
            self.mood = Mood.HUNGRY
        elif self.happiness > 80 and self.energy > 60:
            self.mood = Mood.HAPPY
        elif self.energy > 80:
            self.mood = Mood.ENERGETIC
        else:
            self.mood = Mood.NEUTRAL
    
    def feed(self):
        self.hunger = min(100, self.hunger + 25)
        self.happiness = min(100, self.happiness + 10)
        self.energy = min(100, self.energy + 5)
        self.update_mood()
        
    def sleep(self):
        self.energy = min(100, self.energy + 30)
        self.happiness = max(0, self.happiness - 5)
        self.hunger = max(0, self.hunger - 10)
        self.update_mood()
        
    def play(self):
        self.happiness = min(100, self.happiness + 20)
        self.energy = max(0, self.energy - 15)
        self.hunger = max(0, self.hunger - 10)
        self.update_mood()
        
    def pet(self):
        self.happiness = min(100, self.happiness + 5)
        self.target_scale = 1.3
        self.purr_animation = time.time()
        self.update_mood()
        
    def update_animation(self):
        current_time = time.time()
        
        # Animación de parpadeo
        if current_time - self.blink_timer > random.uniform(3, 6):
            self.is_blinking = True
            self.blink_timer = current_time
        
        if self.is_blinking and current_time - self.blink_timer > 0.20:
            self.is_blinking = False
        
        # Animaciones según el estado de ánimo
        if self.mood == Mood.HAPPY:
            self.animation_offset = math.sin(current_time * 4) * 5
            self.target_scale = 1.1
            self.tail_angle = math.sin(current_time * 6) * 0.8
            self.ear_angle = math.sin(current_time * 3) * 0.2
        elif self.mood == Mood.SAD:
            self.target_scale = 0.9
            self.ear_angle = -0.3  # Orejas caídas
            self.tail_angle = -0.2  # Cola baja
        elif self.mood == Mood.ENERGETIC:
            self.animation_offset = math.sin(current_time * 8) * 10
            self.tail_angle = math.sin(current_time * 10) * 1.2
            self.ear_angle = math.sin(current_time * 4) * 0.4
        elif self.mood == Mood.HUNGRY:
            self.animation_offset = math.sin(current_time * 8) * 3
            self.ear_angle = math.sin(current_time * 6) * 0.3  # Orejas alertas
        elif self.mood == Mood.SLEEPY:
            self.target_scale = 0.95
            self.animation_offset = math.sin(current_time * 1) * 1  # Respiración lenta
            self.ear_angle = -0.1  # Orejas relajadas
        else:
            self.animation_offset = math.sin(current_time * 2) * 2  # Respiración normal
            self.tail_angle = math.sin(current_time * 2) * 0.3
            self.ear_angle = 0
            self.target_scale = 1.0
            
        # Suavizar la escala
        self.scale += (self.target_scale - self.scale) * 0.1
        
        # Degradación automática cada 5 segundos
        if current_time - self.last_time_decay > 5.0:
            self.hunger = max(0, self.hunger - 2)
            self.energy = max(0, self.energy - 1)
            self.happiness = max(0, self.happiness - 1)
            self.last_time_decay = current_time
            self.update_mood()
    
    def get_status_message(self):
        messages = {
            Mood.HAPPY: f"¡{self.name} está muy feliz!",
            Mood.SAD: f"{self.name} está triste... necesita cuidados",
            Mood.HUNGRY: f"{self.name} tiene hambre",
            Mood.SLEEPY: f"{self.name} está cansado",
            Mood.ENERGETIC: f"¡{self.name} está lleno de energía!",
            Mood.NEUTRAL: f"{self.name} está bien"
        }
        return messages[self.mood]

class Button:
    def __init__(self, x, y, width, height, text, color, text_color=WHITE):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.text_color = text_color
        self.font = pygame.font.Font(None, 24)
        self.is_hovered = False
        
    def draw(self, screen):
        color = (min(255, self.color[0] + 30), min(255, self.color[1] + 30), min(255, self.color[2] + 30)) if self.is_hovered else self.color
        pygame.draw.rect(screen, color, self.rect, border_radius=15)
        pygame.draw.rect(screen, WHITE, self.rect, 2, border_radius=15)
        
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Talking CAT")
        self.clock = pygame.time.Clock()
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 32)
        self.font_small = pygame.font.Font(None, 24)
        
        self.state = "setup"  # setup, game, minigame
        self.cat = None
        self.message = "¡Haz clic en tu gato para acariciarlo!"
        self.message_time = 0
        
        # Setup screen variables
        self.cat_name = ""
        self.selected_color = "Marrón"
        self.input_active = True
        
        # Minigame variables
        self.current_minigame = None
        self.minigame_score = 0
        self.minigame_objects = []
        self.minigame_timer = 0
        
        self.setup_buttons()
        
    def setup_buttons(self):
        # Botones de configuración
        self.color_buttons = []
        x_start = 200
        y_pos = 300
        for i, (color_name, color) in enumerate(CAT_COLORS.items()):
            button = Button(x_start + i * 120, y_pos, 100, 40, color_name, color, BLACK if color_name == "Blanco" else WHITE)
            self.color_buttons.append(button)
            
        self.start_button = Button(400, 400, 200, 60, "¡Empezar a Jugar!", PURPLE)
        
        # Botones del juego principal (sin el juego de atrapar)
        self.game_buttons = [
            Button(50, 500, 120, 50, "Alimentar", ORANGE),
            Button(190, 500, 120, 50, "Dormir", LIGHT_BLUE),
            Button(330, 500, 120, 50, "Memoria", PURPLE),
            Button(470, 500, 120, 50, "Palabras", PINK),
            Button(610, 500, 120, 50, "Cambiar Gato", GRAY)
        ]
        
        # Botón cerrar minijuego
        self.close_minigame_button = Button(400, 600, 200, 50, "Cerrar", RED)
    
    def draw_realistic_cat(self, x, y, scale=1.0):
        if not self.cat:
            return
            
        current_time = time.time()
        
        # Color del gato
        cat_color = self.cat.color
        
        # Color más claro para el pecho/barriga
        chest_color = tuple(min(255, c + 40) for c in cat_color)
        if self.cat.color_name == "Negro":
            chest_color = (40, 40, 40)
        
        # Cuerpo principal (más realista y alargado)
        body_width = int(80 * scale)
        body_height = int(50 * scale)
        body_rect = pygame.Rect(x - body_width//2, y - body_height//2, body_width, body_height)
        pygame.draw.ellipse(self.screen, cat_color, body_rect)
        
        # Pecho/barriga
        chest_width = int(40 * scale)
        chest_height = int(30 * scale)
        chest_rect = pygame.Rect(x - chest_width//2, y - chest_height//2 + int(5*scale), chest_width, chest_height)
        pygame.draw.ellipse(self.screen, chest_color, chest_rect)
        
        # Cabeza (más proporcionada)
        head_width = int(50 * scale)
        head_height = int(45 * scale)
        head_y = y - int(35 * scale)
        head_rect = pygame.Rect(x - head_width//2, head_y - head_height//2, head_width, head_height)
        pygame.draw.ellipse(self.screen, cat_color, head_rect)
        
        # Hocico
        muzzle_width = int(25 * scale)
        muzzle_height = int(15 * scale)
        muzzle_y = head_y + int(8 * scale)
        muzzle_rect = pygame.Rect(x - muzzle_width//2, muzzle_y - muzzle_height//2, muzzle_width, muzzle_height)
        pygame.draw.ellipse(self.screen, chest_color, muzzle_rect)
        
        # Orejas con animación según el estado de ánimo
        ear_base_offset = self.cat.ear_angle
        ear_size = int(18 * scale)
        
        # Oreja izquierda
        left_ear_points = [
            (x - int(20 * scale), head_y - int(15 * scale) + ear_base_offset * 10),
            (x - int(35 * scale), head_y - int(35 * scale) + ear_base_offset * 5),
            (x - int(10 * scale), head_y - int(25 * scale) + ear_base_offset * 8)
        ]
        pygame.draw.polygon(self.screen, cat_color, left_ear_points)
        
        # Interior de oreja izquierda
        left_ear_inner = [
            (x - int(18 * scale), head_y - int(18 * scale) + ear_base_offset * 8),
            (x - int(28 * scale), head_y - int(30 * scale) + ear_base_offset * 4),
            (x - int(15 * scale), head_y - int(24 * scale) + ear_base_offset * 6)
        ]
        pygame.draw.polygon(self.screen, PINK, left_ear_inner)
        
        # Oreja derecha
        right_ear_points = [
            (x + int(20 * scale), head_y - int(15 * scale) + ear_base_offset * 10),
            (x + int(35 * scale), head_y - int(35 * scale) + ear_base_offset * 5),
            (x + int(10 * scale), head_y - int(25 * scale) + ear_base_offset * 8)
        ]
        pygame.draw.polygon(self.screen, cat_color, right_ear_points)
        
        # Interior de oreja derecha
        right_ear_inner = [
            (x + int(18 * scale), head_y - int(18 * scale) + ear_base_offset * 8),
            (x + int(28 * scale), head_y - int(30 * scale) + ear_base_offset * 4),
            (x + int(15 * scale), head_y - int(24 * scale) + ear_base_offset * 6)
        ]
        pygame.draw.polygon(self.screen, PINK, right_ear_inner)
        
        # Patas (más realistas)
        paw_width = int(12 * scale)
        paw_height = int(20 * scale)
        
        # Patas delanteras
        front_left_paw = pygame.Rect(x - int(25 * scale), y + int(15 * scale), paw_width, paw_height)
        front_right_paw = pygame.Rect(x + int(13 * scale), y + int(15 * scale), paw_width, paw_height)
        pygame.draw.ellipse(self.screen, cat_color, front_left_paw)
        pygame.draw.ellipse(self.screen, cat_color, front_right_paw)
        
        # Patas traseras
        back_left_paw = pygame.Rect(x - int(10 * scale), y + int(15 * scale), paw_width, paw_height)
        back_right_paw = pygame.Rect(x + int(28 * scale), y + int(15 * scale), paw_width, paw_height)
        pygame.draw.ellipse(self.screen, cat_color, back_left_paw)
        pygame.draw.ellipse(self.screen, cat_color, back_right_paw)
        
        # Cola con animación
        tail_base_x = x + int(35 * scale)
        tail_base_y = y
        tail_angle = self.cat.tail_angle
        tail_length = int(40 * scale)
        
        # Segmentos de la cola para hacer una curva más natural
        segments = 8
        for i in range(segments):
            segment_angle = tail_angle + (i * 0.3)
            segment_x = tail_base_x + math.cos(segment_angle) * (tail_length * i / segments)
            segment_y = tail_base_y + math.sin(segment_angle) * (tail_length * i / segments)
            tail_thickness = int((8 - i) * scale)
            if tail_thickness > 0:
                pygame.draw.circle(self.screen, cat_color, (int(segment_x), int(segment_y)), tail_thickness)
        
        # Expresiones faciales según el estado de ánimo
        self.draw_cat_expression(x, head_y, scale)
        
        # Efectos especiales según el estado
        if self.cat.purr_animation > 0 and current_time - self.cat.purr_animation < 2:
            # Efecto de ronroneo con corazoncitos
            heart_y = head_y - int(50 * scale)
            for i in range(3):
                heart_x = x + (i - 1) * int(20 * scale)
                heart_alpha = max(0, 255 - int((current_time - self.cat.purr_animation) * 127))
                if heart_alpha > 50:
                    pygame.draw.circle(self.screen, PINK, (heart_x, heart_y), int(4 * scale))
    
    def draw_cat_expression(self, x, head_y, scale):
        current_time = time.time()
        
        # Posiciones base de los ojos
        left_eye_x = x - int(12 * scale)
        right_eye_x = x + int(12 * scale)
        eye_y = head_y - int(5 * scale)
        
        # Expresión según el estado de ánimo
        if self.cat.mood == Mood.HAPPY:
            # Ojos felices (cerrados sonriendo)
            pygame.draw.arc(self.screen, BLACK, 
                          (left_eye_x - int(8*scale), eye_y - int(4*scale), int(16*scale), int(8*scale)), 
                          0, math.pi, int(2*scale))
            pygame.draw.arc(self.screen, BLACK, 
                          (right_eye_x - int(8*scale), eye_y - int(4*scale), int(16*scale), int(8*scale)), 
                          0, math.pi, int(2*scale))
            # Boca sonriente
            pygame.draw.arc(self.screen, BLACK, 
                          (x - int(8*scale), head_y + int(15*scale), int(16*scale), int(8*scale)), 
                          0, math.pi, int(2*scale))
        
        elif self.cat.mood == Mood.SAD:
            # Ojos tristes
            pygame.draw.arc(self.screen, BLACK, 
                          (left_eye_x - int(6*scale), eye_y - int(2*scale), int(12*scale), int(8*scale)), 
                          math.pi, 2*math.pi, int(2*scale))
            pygame.draw.arc(self.screen, BLACK, 
                          (right_eye_x - int(6*scale), eye_y - int(2*scale), int(12*scale), int(8*scale)), 
                          math.pi, 2*math.pi, int(2*scale))
            # Pequeñas lágrimas
            pygame.draw.circle(self.screen, LIGHT_BLUE, 
                             (left_eye_x - int(8*scale), eye_y + int(8*scale)), int(2*scale))
            pygame.draw.circle(self.screen, LIGHT_BLUE, 
                             (right_eye_x + int(8*scale), eye_y + int(8*scale)), int(2*scale))
        
        elif self.cat.mood == Mood.SLEEPY:
            # Ojos somnolientos
            if self.cat.is_blinking or random.random() < 0.3:
                pygame.draw.line(self.screen, BLACK, 
                               (left_eye_x - int(6*scale), eye_y), 
                               (left_eye_x + int(6*scale), eye_y), int(2*scale))
                pygame.draw.line(self.screen, BLACK, 
                               (right_eye_x - int(6*scale), eye_y), 
                               (right_eye_x + int(6*scale), eye_y), int(2*scale))
            else:
                pygame.draw.ellipse(self.screen, BLACK, 
                                  (left_eye_x - int(3*scale), eye_y - int(2*scale), int(6*scale), int(4*scale)))
                pygame.draw.ellipse(self.screen, BLACK, 
                                  (right_eye_x - int(3*scale), eye_y - int(2*scale), int(6*scale), int(4*scale)))
            
            # Zzz
            z_x = x + int(30 * scale)
            z_y = head_y - int(20 * scale)
            z_text = self.font_small.render("Zzz", True, GRAY)
            self.screen.blit(z_text, (z_x, z_y))
        
        elif self.cat.mood == Mood.HUNGRY:
            # Ojos grandes y alertas
            pygame.draw.circle(self.screen, WHITE, (left_eye_x, eye_y), int(8*scale))
            pygame.draw.circle(self.screen, BLACK, (left_eye_x, eye_y), int(6*scale))
            pygame.draw.circle(self.screen, WHITE, (left_eye_x - int(2*scale), eye_y - int(2*scale)), int(2*scale))
            
            pygame.draw.circle(self.screen, WHITE, (right_eye_x, eye_y), int(8*scale))
            pygame.draw.circle(self.screen, BLACK, (right_eye_x, eye_y), int(6*scale))
            pygame.draw.circle(self.screen, WHITE, (right_eye_x - int(2*scale), eye_y - int(2*scale)), int(2*scale))
            
            # Lengua hambrienta
            tongue_points = [
                (x - int(3*scale), head_y + int(20*scale)),
                (x + int(3*scale), head_y + int(20*scale)),
                (x, head_y + int(25*scale))
            ]
            pygame.draw.polygon(self.screen, PINK, tongue_points)
        
        elif self.cat.mood == Mood.ENERGETIC:
            # Ojos muy abiertos y brillantes
            pygame.draw.circle(self.screen, WHITE, (left_eye_x, eye_y), int(8*scale))
            pygame.draw.circle(self.screen, BLACK, (left_eye_x, eye_y), int(5*scale))
            pygame.draw.circle(self.screen, WHITE, (left_eye_x - int(1*scale), eye_y - int(1*scale)), int(3*scale))
            
            pygame.draw.circle(self.screen, WHITE, (right_eye_x, eye_y), int(8*scale))
            pygame.draw.circle(self.screen, BLACK, (right_eye_x, eye_y), int(5*scale))
            pygame.draw.circle(self.screen, WHITE, (right_eye_x - int(1*scale), eye_y - int(1*scale)), int(3*scale))
            
            # Exclamación de energía
            exclamation_x = x + int(35 * scale)
            exclamation_y = head_y - int(25 * scale)
            exclamation_text = self.font_medium.render("!", True, YELLOW)
            self.screen.blit(exclamation_text, (exclamation_x, exclamation_y))
        
        else:  # NEUTRAL
            # Ojos normales con parpadeo
            if self.cat.is_blinking:
                pygame.draw.line(self.screen, BLACK, 
                               (left_eye_x - int(6*scale), eye_y), 
                               (left_eye_x + int(6*scale), eye_y), int(2*scale))
                pygame.draw.line(self.screen, BLACK, 
                               (right_eye_x - int(6*scale), eye_y), 
                               (right_eye_x + int(6*scale), eye_y), int(2*scale))
            else:
                pygame.draw.circle(self.screen, WHITE, (left_eye_x, eye_y), int(6*scale))
                pygame.draw.circle(self.screen, BLACK, (left_eye_x, eye_y), int(4*scale))
                pygame.draw.circle(self.screen, WHITE, (left_eye_x - int(2*scale), eye_y - int(1*scale)), int(2*scale))
                
                pygame.draw.circle(self.screen, WHITE, (right_eye_x, eye_y), int(6*scale))
                pygame.draw.circle(self.screen, BLACK, (right_eye_x, eye_y), int(4*scale))
                pygame.draw.circle(self.screen, WHITE, (right_eye_x - int(2*scale), eye_y - int(1*scale)), int(2*scale))
        
        # Nariz (siempre presente)
        nose_points = [
            (x, head_y + int(5 * scale)),
            (x - int(3 * scale), head_y + int(8 * scale)),
            (x + int(3 * scale), head_y + int(8 * scale))
        ]
        pygame.draw.polygon(self.screen, PINK, nose_points)
        
        # Bigotes
        whisker_length = int(15 * scale)
        whisker_y1 = head_y + int(3 * scale)
        whisker_y2 = head_y + int(8 * scale)
        
        # Bigotes izquierdos
        pygame.draw.line(self.screen, BLACK, 
                        (x - int(15*scale), whisker_y1), 
                        (x - int(15*scale) - whisker_length, whisker_y1), int(1*scale))
        pygame.draw.line(self.screen, BLACK, 
                        (x - int(15*scale), whisker_y2), 
                        (x - int(15*scale) - whisker_length, whisker_y2), int(1*scale))
        
        # Bigotes derechos
        pygame.draw.line(self.screen, BLACK, 
                        (x + int(15*scale), whisker_y1), 
                        (x + int(15*scale) + whisker_length, whisker_y1), int(1*scale))
        pygame.draw.line(self.screen, BLACK, 
                        (x + int(15*scale), whisker_y2), 
                        (x + int(15*scale) + whisker_length, whisker_y2), int(1*scale))
    
    def draw_setup_screen(self):
        self.screen.fill(LIGHT_BLUE)
        
        # Título
        title = self.font_large.render("Talking CAT - Realista", True, PURPLE)
        title_rect = title.get_rect(center=(WINDOW_WIDTH//2, 100))
        self.screen.blit(title, title_rect)
        
        # Input de nombre
        name_label = self.font_medium.render("Nombre de tu gato/gata:", True, BLACK)
        name_rect = name_label.get_rect(center=(WINDOW_WIDTH//2, 180))
        self.screen.blit(name_label, name_rect)
        
        # Campo de texto
        input_rect = pygame.Rect(350, 200, 300, 40)
        pygame.draw.rect(self.screen, WHITE, input_rect, border_radius=10)
        pygame.draw.rect(self.screen, BLACK, input_rect, 2, border_radius=10)
        
        name_text = self.font_small.render(self.cat_name + ("_" if self.input_active and time.time() % 1 < 0.5 else ""), True, BLACK)
        self.screen.blit(name_text, (input_rect.x + 10, input_rect.y + 10))
        
        # Etiqueta de colores
        color_label = self.font_medium.render("Elige el color de tu gato:", True, BLACK)
        color_rect = color_label.get_rect(center=(WINDOW_WIDTH//2, 260))
        self.screen.blit(color_label, color_rect)
        
        # Botones de color
        for i, button in enumerate(self.color_buttons):
            if list(CAT_COLORS.keys())[i] == self.selected_color:
                pygame.draw.rect(self.screen, YELLOW, button.rect.inflate(10, 10), 3, border_radius=20)
            button.draw(self.screen)
        
        # Botón de inicio
        self.start_button.draw(self.screen)
    
    def draw_stat_bar(self, x, y, width, height, value, max_value, color, label):
        # Fondo de la barra
        pygame.draw.rect(self.screen, GRAY, (x, y, width, height), border_radius=10)
        
        # Barra de progreso
        progress_width = int((value / max_value) * width)
        pygame.draw.rect(self.screen, color, (x, y, progress_width, height), border_radius=10)
        
        # Borde
        pygame.draw.rect(self.screen, BLACK, (x, y, width, height), 2, border_radius=10)
        
        # Etiqueta y porcentaje
        label_text = self.font_small.render(f"{label}: {value}%", True, BLACK)
        self.screen.blit(label_text, (x, y - 25))
    
    def draw_game_screen(self):
        # Fondo degradado
        for y in range(WINDOW_HEIGHT):
            color_ratio = y / WINDOW_HEIGHT
            r = int(BLUE[0] + (PURPLE[0] - BLUE[0]) * color_ratio)
            g = int(BLUE[1] + (PURPLE[1] - BLUE[1]) * color_ratio)
            b = int(BLUE[2] + (PURPLE[2] - BLUE[2]) * color_ratio)
            pygame.draw.line(self.screen, (r, g, b), (0, y), (WINDOW_WIDTH, y))
        
        # Nubes decorativas
        pygame.draw.ellipse(self.screen, WHITE, (100, 80, 120, 40))
        pygame.draw.ellipse(self.screen, WHITE, (700, 120, 100, 30))
        pygame.draw.ellipse(self.screen, WHITE, (500, 90, 80, 25))
        
        # Título con nombre del gato
        title = self.font_large.render(f"{self.cat.name} ({self.cat.color_name})", True, PURPLE)
        title_rect = title.get_rect(center=(WINDOW_WIDTH//2, 50))
        self.screen.blit(title, title_rect)
        
        # Dibujar gato realista con animación
        cat_x = int(self.cat.x)
        cat_y = int(self.cat.base_y + self.cat.animation_offset)
        self.draw_realistic_cat(cat_x, cat_y, self.cat.scale)
        
        # Barras de estado
        bar_width = 200
        bar_height = 20
        start_x = 50
        start_y = 600
        
        self.draw_stat_bar(start_x, start_y, bar_width, bar_height, 
                          self.cat.happiness, 100, PINK, "Felicidad")
        self.draw_stat_bar(start_x + 250, start_y, bar_width, bar_height, 
                          self.cat.energy, 100, LIGHT_BLUE, "Energía")
        self.draw_stat_bar(start_x + 500, start_y, bar_width, bar_height, 
                          self.cat.hunger, 100, ORANGE, "Comida")
        
        # Botones de acción
        for button in self.game_buttons:
            button.draw(self.screen)
        
        # Mensaje de estado
        if time.time() - self.message_time < 3:
            message_text = self.font_medium.render(self.message, True, BLACK)
        else:
            message_text = self.font_medium.render(self.cat.get_status_message(), True, BLACK)
        
        message_rect = pygame.Rect(50, 400, WINDOW_WIDTH - 100, 80)
        pygame.draw.rect(self.screen, WHITE, message_rect, border_radius=15)
        pygame.draw.rect(self.screen, BLACK, message_rect, 2, border_radius=15)
        
        text_rect = message_text.get_rect(center=message_rect.center)
        self.screen.blit(message_text, text_rect)
    
    def draw_minigame_screen(self):
        self.screen.fill(LIGHT_BLUE)
        
        if self.current_minigame == "memory":
            self.draw_memory_game()
        elif self.current_minigame == "words":
            self.draw_words_game()
        
        # Botón cerrar
        self.close_minigame_button.draw(self.screen)
        
        # Puntuación
        score_text = self.font_medium.render(f"Puntos: {self.minigame_score}", True, BLACK)
        self.screen.blit(score_text, (50, 50))
    
    def draw_memory_game(self):
        title = self.font_large.render("Juego de Memoria", True, PURPLE)
        title_rect = title.get_rect(center=(WINDOW_WIDTH//2, 100))
        self.screen.blit(title, title_rect)
        
        # Dibujar cartas
        for i, card in enumerate(self.minigame_objects):
            x = 300 + (i % 4) * 100
            y = 200 + (i // 4) * 100
            
            color = GREEN if card['flipped'] else BLUE
            pygame.draw.rect(self.screen, color, (x, y, 80, 80), border_radius=10)
            pygame.draw.rect(self.screen, BLACK, (x, y, 80, 80), 2, border_radius=10)
            
            if card['flipped']:
                number_text = self.font_large.render(str(card['number']), True, BLACK)
                text_rect = number_text.get_rect(center=(x + 40, y + 40))
                self.screen.blit(number_text, text_rect)
            else:
                question_text = self.font_medium.render("?", True, WHITE)
                text_rect = question_text.get_rect(center=(x + 40, y + 40))
                self.screen.blit(question_text, text_rect)
    
    def draw_words_game(self):
        title = self.font_large.render(f"¡Memoriza la secuencia con {self.cat.name}!", True, PURPLE)
        title_rect = title.get_rect(center=(WINDOW_WIDTH//2, 100))
        self.screen.blit(title, title_rect)
        
        current_time = time.time()
        
        # Instrucciones
        if hasattr(self, 'words_showing') and self.words_showing:
            instruction_text = self.font_medium.render("Memoriza esta secuencia:", True, BLACK)
            instruction_rect = instruction_text.get_rect(center=(WINDOW_WIDTH//2, 150))
            self.screen.blit(instruction_text, instruction_rect)
            
            # Mostrar la secuencia progresivamente
            if hasattr(self, 'words_show_timer') and current_time - self.words_show_timer > 1.0:
                self.words_show_index += 1
                self.words_show_timer = current_time
                
                if self.words_show_index >= len(self.words_sequence):
                    self.words_showing = False
                    self.words_show_index = -1
            
            # Mostrar la parte de la secuencia que debe mostrarse
            if self.words_show_index >= 0:
                sequence_to_show = self.words_sequence[:self.words_show_index + 1]
                sequence_text = " ".join(sequence_to_show)
                seq_surface = self.font_large.render(sequence_text, True, BLACK)
                seq_rect = seq_surface.get_rect(center=(WINDOW_WIDTH//2, 250))
                self.screen.blit(seq_surface, seq_rect)
        else:
            # Fase de input del jugador
            instruction_text = self.font_medium.render("Repite la secuencia haciendo clic en las palabras:", True, BLACK)
            instruction_rect = instruction_text.get_rect(center=(WINDOW_WIDTH//2, 150))
            self.screen.blit(instruction_text, instruction_rect)
            
            # Mostrar progreso actual
            if hasattr(self, 'words_player_sequence') and self.words_player_sequence:
                progress_text = " ".join(self.words_player_sequence)
                progress_surface = self.font_large.render(progress_text, True, PURPLE)
                progress_rect = progress_surface.get_rect(center=(WINDOW_WIDTH//2, 250))
                self.screen.blit(progress_surface, progress_rect)
            
            # Mostrar nivel actual
            level_text = self.font_medium.render(f"Nivel: {len(self.words_sequence)}", True, BLACK)
            self.screen.blit(level_text, (50, 150))
        
        # Botones de palabras
        button_labels = self.words_directions
        button_colors = [RED, ORANGE, GREEN, BLUE]
        for i, label in enumerate(button_labels):
            x = 250 + i * 120
            y = 400
            button_rect = pygame.Rect(x, y, 100, 60)
            
            # Solo hacer los botones clickeables si no estamos mostrando la secuencia
            clickable = not (hasattr(self, 'words_showing') and self.words_showing)
            color = button_colors[i] if clickable else GRAY
            
            pygame.draw.rect(self.screen, color, button_rect, border_radius=15)
            pygame.draw.rect(self.screen, BLACK, button_rect, 2, border_radius=15)
            
            dir_text = self.font_large.render(label, True, BLACK)
            text_rect = dir_text.get_rect(center=button_rect.center)
            self.screen.blit(dir_text, text_rect)
            
            # Guardar los rectángulos para detección de clic
            if not hasattr(self, 'direction_buttons'):
                self.direction_buttons = []
            if i >= len(self.direction_buttons):
                self.direction_buttons.append(button_rect)
            else:
                self.direction_buttons[i] = button_rect
    
    def start_memory_game(self):
        self.current_minigame = "memory"
        self.minigame_score = 0
        # Lista de números para el juego de memoria
        numbers = [1, 2, 3, 4, 5, 6] * 2  # 6 pares, total 12 cartas
        random.shuffle(numbers)
        
        self.minigame_objects = []
        for i, number in enumerate(numbers):
            self.minigame_objects.append({
                'number': number,
                'flipped': False,
                'matched': False,
                'index': i
            })
        
        self.memory_flipped = []
        self.memory_flip_time = 0
    
    def start_words_game(self):
        self.current_minigame = "words"
        self.minigame_score = 0
        self.words_sequence = []
        self.words_player_sequence = []
        # Palabras en vez de flechas
        self.words_directions = ["Gato", "Perro", "Sol", "Luna"]
        self.words_show_index = -1
        self.words_showing = False
        self.direction_buttons = []
        self.generate_words_sequence()
    
    def generate_words_sequence(self):
        self.words_sequence.append(random.choice(self.words_directions))
        self.show_words_sequence()
    
    def show_words_sequence(self):
        self.words_showing = True
        self.words_show_index = -1
        self.words_show_timer = time.time()
        self.words_player_sequence = []
    
    def update_minigames(self):
        current_time = time.time()
        
        if self.current_minigame == "memory":
            # Verificar si hay cartas volteadas para voltear de vuelta
            if len(self.memory_flipped) == 2 and current_time - self.memory_flip_time > 1.0:
                card1, card2 = self.memory_flipped
                if self.minigame_objects[card1]['number'] == self.minigame_objects[card2]['number']:
                    self.minigame_objects[card1]['matched'] = True
                    self.minigame_objects[card2]['matched'] = True
                    self.minigame_score += 20
                else:
                    self.minigame_objects[card1]['flipped'] = False
                    self.minigame_objects[card2]['flipped'] = False
                
                self.memory_flipped = []
                
                # Verificar si ganó
                if all(card['matched'] for card in self.minigame_objects):
                    self.end_minigame()
    
    def handle_minigame_click(self, pos):
        if self.current_minigame == "memory":
            # Verificar clic en cartas
            if len(self.memory_flipped) < 2:
                for i, card in enumerate(self.minigame_objects):
                    x = 300 + (i % 4) * 100
                    y = 200 + (i // 4) * 100
                    card_rect = pygame.Rect(x, y, 80, 80)
                    
                    if card_rect.collidepoint(pos) and not card['flipped'] and not card['matched']:
                        card['flipped'] = True
                        self.memory_flipped.append(i)
                        
                        if len(self.memory_flipped) == 2:
                            self.memory_flip_time = time.time()
                        return
        
        elif self.current_minigame == "words":
            # Solo permitir clics si no estamos mostrando la secuencia
            if hasattr(self, 'words_showing') and not self.words_showing:
                # Verificar clic en botones de palabras
                for i, label in enumerate(self.words_directions):
                    if hasattr(self, 'direction_buttons') and i < len(self.direction_buttons):
                        button_rect = self.direction_buttons[i]
                        
                        if button_rect.collidepoint(pos):
                            self.words_player_sequence.append(label)
                            
                            # Verificar secuencia
                            if len(self.words_player_sequence) <= len(self.words_sequence):
                                if self.words_player_sequence[-1] != self.words_sequence[len(self.words_player_sequence)-1]:
                                    # Secuencia incorrecta
                                    self.show_message("¡Secuencia incorrecta! Inténtalo de nuevo.")
                                    self.show_words_sequence()
                                    return
                                
                                if len(self.words_player_sequence) == len(self.words_sequence):
                                    # Secuencia completa correcta
                                    self.minigame_score += 15
                                    if len(self.words_sequence) >= 8:
                                        self.end_minigame()
                                    else:
                                        self.generate_words_sequence()
                            return

    def end_minigame(self):
        self.cat.play()
        
        if self.minigame_score >= 100:
            message = f"¡Excelente! {self.cat.name} está muy feliz"
        elif self.minigame_score >= 50:
            message = f"¡Buen trabajo! {self.cat.name} se divirtió"
        else:
            message = f"{self.cat.name} disfrutó jugar contigo"
        
        self.show_message(f"{message}\nPuntos totales: {self.minigame_score}")
        self.state = "game"
        self.current_minigame = None
    
    def show_message(self, message):
        self.message = message
        self.message_time = time.time()
    
    def handle_setup_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and self.cat_name:
                self.cat_name = self.cat_name[:-1]
            elif event.key == pygame.K_RETURN:
                if self.cat_name.strip():
                    self.start_main_game()
            elif event.unicode.isprintable() and len(self.cat_name) < 15:
                self.cat_name += event.unicode
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Verificar clic en botones de color
            for i, button in enumerate(self.color_buttons):
                if button.handle_event(event):
                    self.selected_color = list(CAT_COLORS.keys())[i]
            
            # Verificar clic en botón de inicio
            if self.start_button.handle_event(event):
                if self.cat_name.strip():
                    self.start_main_game()
        
        # Manejar hover de botones
        for button in self.color_buttons:
            button.handle_event(event)
        self.start_button.handle_event(event)
    
    def handle_game_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Verificar clic en el gato (área más grande para mejor interacción)
            cat_rect = pygame.Rect(self.cat.x - 80, self.cat.y - 70, 160, 140)
            if cat_rect.collidepoint(event.pos):
                self.cat.pet()
                self.show_message(f"¡A {self.cat.name} le gustan las caricias!")
                return
            
            # Verificar clic en botones
            for i, button in enumerate(self.game_buttons):
                if button.handle_event(event):
                    if i == 0:  # Alimentar
                        self.cat.feed()
                        self.show_message(f"¡Ñam ñam! A {self.cat.name} le gustó la comida")
                    elif i == 1:  # Dormir
                        self.cat.sleep()
                        self.show_message(f"{self.cat.name} está durmiendo... Zzz")
                    elif i == 2:  # Memoria
                        self.state = "minigame"
                        self.start_memory_game()
                    elif i == 3:  # Palabras
                        self.state = "minigame"
                        self.start_words_game()
                    elif i == 4:  # Nuevo Gato
                        self.state = "setup"
                        self.cat_name = ""
                        self.selected_color = "Marrón"
        
        # Manejar hover de botones
        for button in self.game_buttons:
            button.handle_event(event)
    
    def handle_minigame_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.close_minigame_button.handle_event(event):
                self.state = "game"
                self.current_minigame = None
            else:
                self.handle_minigame_click(event.pos)
        
        # Manejar hover
        self.close_minigame_button.handle_event(event)
    
    def start_main_game(self):
        name = self.cat_name.strip() or "Michi"
        self.cat = VirtualCat(name, self.selected_color)
        self.state = "game"
        self.show_message("¡Haz clic en tu gato para acariciarlo!")
    
    def run(self):
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                elif self.state == "setup":
                    self.handle_setup_events(event)
                elif self.state == "game":
                    self.handle_game_events(event)
                elif self.state == "minigame":
                    self.handle_minigame_events(event)
            
            # Actualizar lógica del juego
            if self.state == "game" and self.cat:
                self.cat.update_animation()
            elif self.state == "minigame":
                self.update_minigames()
            
            # Dibujar
            if self.state == "setup":
                self.draw_setup_screen()
            elif self.state == "game":
                self.draw_game_screen()
            elif self.state == "minigame":
                self.draw_minigame_screen()
            
            pygame.display.flip()
            self.clock.tick(FPS)
        
        pygame.quit()

def main():
    """
    TALKING CAT - VERSIÓN MEJORADA CON EXPRESIONES REALISTAS
    
    Cambios realizados:
    ✅ Eliminado completamente el juego de atrapar ratones
    ✅ Mini juego de palabras ahora funciona correctamente:
       - Muestra la secuencia progresivamente
       - Permite al jugador repetirla
       - Aumenta la dificultad gradualmente
       - Detecta errores y reinicia la secuencia
    ✅ Juego de memoria usa números del 1 al 6 en lugar de emojis
    ✅ Botones reorganizados sin el juego eliminado
    
    Instrucciones de instalación:
    
    1. Instalar Python (si no lo tienes): https://python.org
    2. Instalar Pygame:
       - Abre la terminal/comando
       - Ejecuta: pip install pygame
    3. Guardar este código en un archivo llamado: talking_cat_mejorado.py
    4. Ejecutar desde terminal: python talking_cat_mejorado.py
    
    O desde Visual Studio Code:
    1. Instalar la extensión de Python
    2. Abrir este archivo
    3. Presionar F5 o hacer clic en "Run Python File"
    
    CARACTERÍSTICAS:
    🐱 Gato realista con expresiones faciales
    😸 Estados de ánimo que afectan las animaciones
    🎮 Juego de memoria con números (1-6)
    🧠 Juego de secuencias de palabras/direcciones
    💝 Sistema de cuidado del gato (alimentar, dormir, acariciar)
    🎨 Múltiples colores de gato para elegir
    
    ¡Disfruta cuidando a tu gato virtual!
    """
    try:
        game = Game()
        game.run()
    except Exception as e:
        print(f"Error al ejecutar el juego: {e}")
        print("Asegúrate de tener pygame instalado: pip install pygame")

if __name__ == "__main__":
    main()