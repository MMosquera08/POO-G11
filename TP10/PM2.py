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

# Colores de gato disponibles con características específicas
CAT_COLORS = {
    "Marrón": {
        "body": (139, 69, 19),
        "darker": (101, 50, 14),
        "eyes": (255, 215, 0),  # Ojos dorados
        "style": "solid"
    },
    "Negro": {
        "body": (30, 30, 30),
        "darker": (0, 0, 0),
        "eyes": (255, 215, 0),  # Ojos amarillos brillantes
        "style": "solid"
    },
    "Naranja": {
        "body": (255, 140, 0),
        "darker": (204, 85, 0),
        "eyes": (0, 255, 0),  # Ojos verdes
        "style": "striped"
    },
    "Gris": {
        "body": (128, 128, 128),
        "darker": (96, 96, 96),
        "eyes": (144, 238, 144),  # Ojos verde claro
        "style": "solid"
    },
    "Blanco": {
        "body": (245, 245, 245),
        "darker": (200, 200, 200),
        "eyes": (0, 0, 0),  # Ojos negros
        "style": "solid"
    }
}

class VirtualCat:
    def __init__(self, name, color_name):
        self.name = name
        self.color_name = color_name
        self.color_info = CAT_COLORS[color_name]
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
        self.update_mood()
        
    def update_animation(self):
        # Animaciones según el estado de ánimo
        current_time = time.time()
        
        if self.mood == Mood.HAPPY:
            self.animation_offset = math.sin(current_time * 4) * 5
            self.target_scale = 1.1
        elif self.mood == Mood.SAD:
            self.target_scale = 0.8
        elif self.mood == Mood.ENERGETIC:
            self.animation_offset = math.sin(current_time * 6) * 10
        elif self.mood == Mood.HUNGRY:
            self.animation_offset = math.sin(current_time * 8) * 3
        elif self.mood == Mood.SLEEPY:
            self.target_scale = 0.9
        else:
            self.animation_offset = 0
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
        x_start = 150
        y_pos = 300
        for i, (color_name, color_info) in enumerate(CAT_COLORS.items()):
            button = Button(x_start + i * 140, y_pos, 120, 40, color_name, color_info["body"], 
                          BLACK if color_name == "Blanco" else WHITE)
            self.color_buttons.append(button)
            
        self.start_button = Button(400, 400, 200, 60, "¡Empezar a Jugar!", PURPLE)
        
        # Botones del juego principal
        self.game_buttons = [
            Button(50, 500, 120, 50, "Alimentar", ORANGE),
            Button(190, 500, 120, 50, "Dormir", LIGHT_BLUE),
            Button(330, 500, 120, 50, "Atrapar", RED),
            Button(470, 500, 120, 50, "Memoria", PURPLE),
            Button(610, 500, 120, 50, "Bailar", PINK),
            Button(750, 500, 120, 50, "Cambiar Gato", GRAY)
        ]
        
        # Botón cerrar minijuego
        self.close_minigame_button = Button(400, 600, 200, 50, "Cerrar", RED)
    
    def draw_setup_screen(self):
        self.screen.fill(LIGHT_BLUE)
        
        # Título
        title = self.font_large.render("Talking CAT", True, PURPLE)
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
    
    def draw_improved_cat(self, x, y, scale=1.0):
        """Dibuja el gato con estilos mejorados según la imagen de referencia"""
        if not self.cat:
            return
            
        color_info = self.cat.color_info
        body_color = color_info["body"]
        darker_color = color_info["darker"]
        eye_color = color_info["eyes"]
        style = color_info["style"]
        
        # Tamaños escalados
        body_width = int(80 * scale)
        body_height = int(50 * scale)
        head_size = int(50 * scale)
        
        # Posición ajustada
        body_y = y + int(10 * scale)
        head_y = y - int(20 * scale)
        
        # Dibujar cuerpo (forma más cuadrada como en la imagen)
        body_rect = pygame.Rect(x - body_width//2, body_y - body_height//2, body_width, body_height)
        pygame.draw.rect(self.screen, body_color, body_rect, border_radius=int(15 * scale))
        
        # Dibujar cabeza (más cuadrada)
        head_rect = pygame.Rect(x - head_size//2, head_y - head_size//2, head_size, head_size)
        pygame.draw.rect(self.screen, body_color, head_rect, border_radius=int(20 * scale))
        
        # Dibujar patas
        paw_width = int(12 * scale)
        paw_height = int(25 * scale)
        paw_y = body_y + body_height//2 - int(5 * scale)
        
        # Patas delanteras
        pygame.draw.rect(self.screen, body_color, 
                        (x - int(25 * scale), paw_y, paw_width, paw_height), 
                        border_radius=int(6 * scale))
        pygame.draw.rect(self.screen, body_color, 
                        (x + int(13 * scale), paw_y, paw_width, paw_height), 
                        border_radius=int(6 * scale))
        
        # Patas traseras (más atrás)
        pygame.draw.rect(self.screen, body_color, 
                        (x - int(15 * scale), paw_y, paw_width, paw_height), 
                        border_radius=int(6 * scale))
        pygame.draw.rect(self.screen, body_color, 
                        (x + int(3 * scale), paw_y, paw_width, paw_height), 
                        border_radius=int(6 * scale))
        
        # Dibujar orejas triangulares
        ear_size = int(18 * scale)
        left_ear = [
            (x - int(20 * scale), head_y - head_size//2),
            (x - int(35 * scale), head_y - int(35 * scale)),
            (x - int(5 * scale), head_y - int(30 * scale))
        ]
        right_ear = [
            (x + int(20 * scale), head_y - head_size//2),
            (x + int(35 * scale), head_y - int(35 * scale)),
            (x + int(5 * scale), head_y - int(30 * scale))
        ]
        
        pygame.draw.polygon(self.screen, body_color, left_ear)
        pygame.draw.polygon(self.screen, body_color, right_ear)
        
        # Interior de las orejas
        pygame.draw.polygon(self.screen, PINK, [
            (x - int(18 * scale), head_y - int(28 * scale)),
            (x - int(25 * scale), head_y - int(32 * scale)),
            (x - int(12 * scale), head_y - int(28 * scale))
        ])
        pygame.draw.polygon(self.screen, PINK, [
            (x + int(18 * scale), head_y - int(28 * scale)),
            (x + int(25 * scale), head_y - int(32 * scale)),
            (x + int(12 * scale), head_y - int(28 * scale))
        ])
        
        # Dibujar rayas si es naranja
        if style == "striped" and self.cat.color_name == "Naranja":
            stripe_color = darker_color
            # Rayas en la cabeza
            for i in range(3):
                stripe_y = head_y - int(10 * scale) + i * int(8 * scale)
                pygame.draw.rect(self.screen, stripe_color, 
                               (x - int(20 * scale), stripe_y, int(40 * scale), int(3 * scale)))
            
            # Rayas en el cuerpo
            for i in range(2):
                stripe_y = body_y - int(15 * scale) + i * int(15 * scale)
                pygame.draw.rect(self.screen, stripe_color, 
                               (x - int(35 * scale), stripe_y, int(70 * scale), int(4 * scale)))
        
        # Ojos según el estado de ánimo
        eye_radius = int(8 * scale) if self.cat.mood != Mood.SLEEPY else int(3 * scale)
        
        if self.cat.mood == Mood.SLEEPY:
            # Ojos cerrados (líneas)
            pygame.draw.line(self.screen, BLACK, 
                           (x - int(15 * scale), head_y - int(5 * scale)), 
                           (x - int(5 * scale), head_y - int(5 * scale)), 3)
            pygame.draw.line(self.screen, BLACK, 
                           (x + int(5 * scale), head_y - int(5 * scale)), 
                           (x + int(15 * scale), head_y - int(5 * scale)), 3)
        else:
            # Ojos abiertos con color específico
            pygame.draw.circle(self.screen, eye_color, 
                             (x - int(12 * scale), head_y - int(5 * scale)), eye_radius)
            pygame.draw.circle(self.screen, eye_color, 
                             (x + int(12 * scale), head_y - int(5 * scale)), eye_radius)
            
            # Pupilas
            pupil_radius = int(4 * scale)
            pygame.draw.circle(self.screen, BLACK, 
                             (x - int(12 * scale), head_y - int(5 * scale)), pupil_radius)
            pygame.draw.circle(self.screen, BLACK, 
                             (x + int(12 * scale), head_y - int(5 * scale)), pupil_radius)
        
        # Nariz triangular
        nose_points = [
            (x, head_y + int(5 * scale)),
            (x - int(4 * scale), head_y + int(10 * scale)),
            (x + int(4 * scale), head_y + int(10 * scale))
        ]
        pygame.draw.polygon(self.screen, PINK, nose_points)
        
        # Boca simple
        pygame.draw.arc(self.screen, BLACK, 
                       (x - int(8 * scale), head_y + int(8 * scale), int(16 * scale), int(10 * scale)), 
                       0, math.pi, 2)
        
        # Cola curvada
        tail_start_x = x + body_width//2
        tail_start_y = body_y
        
        # Cola con curva usando puntos
        tail_points = [
            (tail_start_x, tail_start_y),
            (tail_start_x + int(20 * scale), tail_start_y - int(10 * scale)),
            (tail_start_x + int(30 * scale), tail_start_y - int(20 * scale)),
            (tail_start_x + int(35 * scale), tail_start_y - int(35 * scale))
        ]
        
        if len(tail_points) >= 2:
            for i in range(len(tail_points) - 1):
                pygame.draw.line(self.screen, body_color, tail_points[i], tail_points[i + 1], int(8 * scale))
    
    def draw_mouse(self, x, y, scale=1.0):
        """Dibuja un ratón más realista"""
        # Cuerpo oval del ratón
        body_width = int(25 * scale)
        body_height = int(15 * scale)
        body_rect = pygame.Rect(x - body_width//2, y - body_height//2, body_width, body_height)
        pygame.draw.ellipse(self.screen, (150, 150, 150), body_rect)
        
        # Cabeza más pequeña
        head_radius = int(10 * scale)
        head_x = x - int(12 * scale)
        pygame.draw.circle(self.screen, (170, 170, 170), (head_x, y - int(3 * scale)), head_radius)
        
        # Orejas grandes y redondas
        ear_radius = int(6 * scale)
        pygame.draw.circle(self.screen, (140, 140, 140), 
                         (head_x - int(8 * scale), y - int(10 * scale)), ear_radius)
        pygame.draw.circle(self.screen, (140, 140, 140), 
                         (head_x - int(2 * scale), y - int(12 * scale)), ear_radius)
        
        # Interior rosado de las orejas
        pygame.draw.circle(self.screen, PINK, 
                         (head_x - int(8 * scale), y - int(10 * scale)), int(3 * scale))
        pygame.draw.circle(self.screen, PINK, 
                         (head_x - int(2 * scale), y - int(12 * scale)), int(3 * scale))
        
        # Ojos pequeños y negros
        pygame.draw.circle(self.screen, BLACK, 
                         (head_x - int(6 * scale), y - int(6 * scale)), int(2 * scale))
        pygame.draw.circle(self.screen, BLACK, 
                         (head_x - int(2 * scale), y - int(7 * scale)), int(2 * scale))
        
        # Nariz pequeña y rosada
        pygame.draw.circle(self.screen, PINK, 
                         (head_x - int(4 * scale), y - int(2 * scale)), int(1 * scale))
        
        # Cola larga y curvada
        tail_start_x = x + body_width//2
        tail_end_x = tail_start_x + int(20 * scale)
        tail_end_y = y - int(8 * scale)
        
        # Dibujar cola como línea gruesa
        pygame.draw.line(self.screen, (120, 120, 120), 
                        (tail_start_x, y), 
                        (tail_end_x, tail_end_y), 
                        int(3 * scale))
        
        # Patas pequeñas
        paw_size = int(2 * scale)
        pygame.draw.circle(self.screen, (130, 130, 130), 
                         (x - int(8 * scale), y + int(8 * scale)), paw_size)
        pygame.draw.circle(self.screen, (130, 130, 130), 
                         (x + int(2 * scale), y + int(8 * scale)), paw_size)
        pygame.draw.circle(self.screen, (130, 130, 130), 
                         (x + int(8 * scale), y + int(8 * scale)), paw_size)
        pygame.draw.circle(self.screen, (130, 130, 130), 
                         (x - int(2 * scale), y + int(8 * scale)), paw_size)
    
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
            r = int(BLUE[0] + (GREEN[0] - BLUE[0]) * color_ratio)
            g = int(BLUE[1] + (GREEN[1] - BLUE[1]) * color_ratio)
            b = int(BLUE[2] + (GREEN[2] - BLUE[2]) * color_ratio)
            pygame.draw.line(self.screen, (r, g, b), (0, y), (WINDOW_WIDTH, y))
        
        # Nubes decorativas
        pygame.draw.ellipse(self.screen, WHITE, (100, 80, 120, 40))
        pygame.draw.ellipse(self.screen, WHITE, (700, 120, 100, 30))
        pygame.draw.ellipse(self.screen, WHITE, (500, 90, 80, 25))
        
        # Título con nombre del gato
        title = self.font_large.render(f"{self.cat.name} ({self.cat.color_name})", True, PURPLE)
        title_rect = title.get_rect(center=(WINDOW_WIDTH//2, 50))
        self.screen.blit(title, title_rect)
        
        # Dibujar gato con estilo mejorado
        cat_x = int(self.cat.x)
        cat_y = int(self.cat.base_y + self.cat.animation_offset)
        self.draw_improved_cat(cat_x, cat_y, self.cat.scale)
        
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
        
        if self.current_minigame == "catch":
            self.draw_catch_game()
        elif self.current_minigame == "memory":
            self.draw_memory_game()
        elif self.current_minigame == "dance":
            self.draw_dance_game()
        
        # Botón cerrar
        self.close_minigame_button.draw(self.screen)
        
        # Puntuación
        score_text = self.font_medium.render(f"Puntos: {self.minigame_score}", True, BLACK)
        self.screen.blit(score_text, (50, 50))
    
    def draw_catch_game(self):
        title = self.font_large.render("¡Atrapa los Ratones!", True, PURPLE)
        title_rect = title.get_rect(center=(WINDOW_WIDTH//2, 100))
        self.screen.blit(title, title_rect)
        
        time_left = max(0, 15 - (time.time() - self.minigame_timer))
        timer_text = self.font_medium.render(f"Tiempo: {int(time_left)}s", True, BLACK)
        self.screen.blit(timer_text, (50, 100))
        
        # Dibujar ratones mejorados
        for mouse in self.minigame_objects:
            self.draw_mouse(mouse['pos'][0], mouse['pos'][1], 1.0)
        
        if time_left <= 0:
            self.end_minigame()
    
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
                emoji_text = self.font_medium.render(card['emoji'], True, BLACK)
                text_rect = emoji_text.get_rect(center=(x + 40, y + 40))
                self.screen.blit(emoji_text, text_rect)
            else:
                question_text = self.font_medium.render("?", True, WHITE)
                text_rect = question_text.get_rect(center=(x + 40, y + 40))
                self.screen.blit(question_text, text_rect)
    
    def draw_dance_game(self):
        title = self.font_large.render(f"¡Baila con {self.cat.name}!", True, PURPLE)
        title_rect = title.get_rect(center=(WINDOW_WIDTH//2, 100))
        self.screen.blit(title, title_rect)
        
        # Mostrar secuencia actual si existe
        if hasattr(self, 'dance_sequence') and self.dance_sequence:
            sequence_text = " ".join(self.dance_sequence[:self.dance_show_index + 1])
            seq_surface = self.font_large.render(sequence_text, True, BLACK)
            seq_rect = seq_surface.get_rect(center=(WINDOW_WIDTH//2, 250))
            self.screen.blit(seq_surface, seq_rect)
        
        # Botones de dirección
        directions = ["I", "Ar", "Ab", "D"]
        for i, direction in enumerate(directions):
            x = 250 + i * 120
            y = 400
            button_rect = pygame.Rect(x, y, 100, 60)
            pygame.draw.rect(self.screen, PINK, button_rect, border_radius=15)
            pygame.draw.rect(self.screen, BLACK, button_rect, 2, border_radius=15)
            
            dir_text = self.font_large.render(direction, True, BLACK)
            text_rect = dir_text.get_rect(center=button_rect.center)
            self.screen.blit(dir_text, text_rect)
    
    def start_catch_game(self):
        self.current_minigame = "catch"
        self.minigame_score = 0
        self.minigame_objects = []
        self.minigame_timer = time.time()
    
    def start_memory_game(self):
        self.current_minigame = "memory"
        self.minigame_score = 0
        emojis = ["1", "2", "3", "4", "5", "6"] * 2
        random.shuffle(emojis)
        
        self.minigame_objects = []
        for i, emoji in enumerate(emojis):
            self.minigame_objects.append({
                'emoji': emoji,
                'flipped': False,
                'matched': False,
                'index': i
            })
        
        self.memory_flipped = []
        self.memory_flip_time = 0
    
    def start_dance_game(self):
        self.current_minigame = "dance"
        self.minigame_score = 0
        self.dance_sequence = []
        self.dance_player_sequence = []
        self.dance_directions = ["I", "Ar", "Ab", "D"]
        self.dance_show_index = -1
        self.dance_showing = False
        self.generate_dance_sequence()
    
    def generate_dance_sequence(self):
        self.dance_sequence.append(random.choice(self.dance_directions))
        self.show_dance_sequence()
    
    def show_dance_sequence(self):
        self.dance_showing = True
        self.dance_show_index = -1
        self.dance_show_timer = time.time()
        self.dance_player_sequence = []
    
    def update_minigames(self):
        current_time = time.time()
        
        if self.current_minigame == "catch":
            # Generar ratones aleatoriamente
            if random.random() < 0.02 and len(self.minigame_objects) < 5:
                mouse = {
                    'pos': [random.randint(50, WINDOW_WIDTH-50), random.randint(150, 450)],
                    'birth_time': current_time,
                    'vx': random.uniform(-2, 2),
                    'vy': random.uniform(-2, 2)
                }
                self.minigame_objects.append(mouse)
            
            # Mover ratones
            for mouse in self.minigame_objects:
                mouse['pos'][0] += mouse['vx']
                mouse['pos'][1] += mouse['vy']
                
                # Rebotar en los bordes
                if mouse['pos'][0] <= 30 or mouse['pos'][0] >= WINDOW_WIDTH - 30:
                    mouse['vx'] *= -1
                if mouse['pos'][1] <= 150 or mouse['pos'][1] >= 550:
                    mouse['vy'] *= -1
            
            # Remover ratones viejos
            self.minigame_objects = [mouse for mouse in self.minigame_objects 
                                   if current_time - mouse['birth_time'] < 4.0]
        
        elif self.current_minigame == "memory":
            # Verificar si hay cartas volteadas para voltear de vuelta
            if len(self.memory_flipped) == 2 and current_time - self.memory_flip_time > 1.0:
                card1, card2 = self.memory_flipped
                if self.minigame_objects[card1]['emoji'] == self.minigame_objects[card2]['emoji']:
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
        
        elif self.current_minigame == "dance":
            # Mostrar secuencia
            if self.dance_showing:
                if current_time - self.dance_show_timer > 0.8:
                    self.dance_show_index += 1
                    self.dance_show_timer = current_time
                    
                    if self.dance_show_index >= len(self.dance_sequence):
                        self.dance_showing = False
                        self.dance_show_index = -1
    
    def handle_minigame_click(self, pos):
        if self.current_minigame == "catch":
            # Verificar clic en ratones (área más grande para facilitar)
            for mouse in self.minigame_objects[:]:
                mouse_rect = pygame.Rect(mouse['pos'][0] - 25, mouse['pos'][1] - 15, 50, 30)
                if mouse_rect.collidepoint(pos):
                    self.minigame_objects.remove(mouse)
                    self.minigame_score += 10
                    return
        
        elif self.current_minigame == "memory":
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
        
        elif self.current_minigame == "dance":
            # Verificar clic en botones de dirección
            if not self.dance_showing:
                directions = ["I", "Ar", "Ab", "D"]
                for i, direction in enumerate(directions):
                    x = 250 + i * 120
                    y = 400
                    button_rect = pygame.Rect(x, y, 100, 60)
                    
                    if button_rect.collidepoint(pos):
                        self.dance_player_sequence.append(direction)
                        
                        # Verificar secuencia
                        if len(self.dance_player_sequence) <= len(self.dance_sequence):
                            if self.dance_player_sequence[-1] != self.dance_sequence[len(self.dance_player_sequence)-1]:
                                # Secuencia incorrecta
                                self.show_message("¡Secuencia incorrecta! Inténtalo de nuevo.")
                                self.show_dance_sequence()
                                return
                            
                            if len(self.dance_player_sequence) == len(self.dance_sequence):
                                # Secuencia completa correcta
                                self.minigame_score += 15
                                if len(self.dance_sequence) >= 8:
                                    self.end_minigame()
                                else:
                                    self.generate_dance_sequence()
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
            # Verificar clic en el gato (área más grande)
            cat_rect = pygame.Rect(self.cat.x - 80, self.cat.y - 80, 160, 140)
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
                    elif i == 2:  # Atrapar
                        self.state = "minigame"
                        self.start_catch_game()
                    elif i == 3:  # Memoria
                        self.state = "minigame"
                        self.start_memory_game()
                    elif i == 4:  # Bailar
                        self.state = "minigame"
                        self.start_dance_game()
                    elif i == 5:  # Nuevo Gato
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
    Instrucciones de instalación:
    
    1. Instalar Python (si no lo tienes): https://python.org
    2. Instalar Pygame:
       - Abre la terminal/comando
       - Ejecuta: pip install pygame
    3. Guardar este código en un archivo llamado: mi_gato_virtual.py
    4. Ejecutar desde terminal: python mi_gato_virtual.py
    
    O desde Visual Studio Code:
    1. Instalar la extensión de Python
    2. Abrir este archivo
    3. Presionar F5 o hacer clic en "Run Python File"
    
    ¡Disfruta jugando con tu gato virtual!
    """
    try:
        game = Game()
        game.run()
    except Exception as e:
        print(f"Error al ejecutar el juego: {e}")
        print("Asegúrate de tener pygame instalado: pip install pygame")

if __name__ == "__main__":
    main()