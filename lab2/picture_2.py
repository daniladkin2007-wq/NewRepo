import pygame
import math
from pygame.draw import *

pygame.init()

WIDTH, HEIGHT = 1400, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("7 котов")

# Цвета
WALL_BROWN = (139, 90, 43)
FLOOR_BEIGE = (222, 184, 135)
ORANGE = (255, 140, 0)
GRAY = (128, 128, 128)
LIGHT_GRAY = (169, 169, 169)
EAR_PINK = (240, 200, 180)
GREEN = (120, 200, 0)
BLUE = (100, 150, 255)
BLACK = (0, 0, 0)
DARK_BROWN = (101, 67, 33)
YARN_GRAY = (170, 170, 170)
YARN_DARK = (105, 105, 105)
WINDOW_FRAME = (200, 230, 220)
WINDOW_GLASS = (120, 180, 200)

clock = pygame.time.Clock()

# Функция для большого кота (лапы и хвост сдвинуты влево на 40)
def draw_big_cat(x, y, color, eye_color):
    # Тело
    ellipse(screen, color, (x, y, 400, 150))
    ellipse(screen, DARK_BROWN, (x, y, 400, 150), 2)

    # Голова
    circle(screen, color, (x + 40, y + 20), 70)
    circle(screen, DARK_BROWN, (x + 40, y + 20), 70, 2)

    # Уши
    polygon(screen, color, [(x - 15, y - 30), (x + 5, y - 80), (x + 45, y - 30)])
    polygon(screen, DARK_BROWN, [(x - 15, y - 30), (x + 5, y - 80), (x + 45, y - 30)], 2)
    polygon(screen, color, [(x + 50, y - 30), (x + 90, y - 80), (x + 105, y - 30)])
    polygon(screen, DARK_BROWN, [(x + 50, y - 30), (x + 90, y - 80), (x + 105, y - 30)], 2)

    # Розовые уши
    polygon(screen, EAR_PINK, [(x - 5, y - 35), (x + 5, y - 65), (x + 35, y - 35)])
    polygon(screen, EAR_PINK, [(x + 60, y - 35), (x + 90, y - 65), (x + 95, y - 35)])

    # Лапы (СДВИНУТЫ ВЛЕВО на 40)
    ellipse(screen, color, (x + 80, y + 80, 80, 40))    # было 120, стало 80
    ellipse(screen, DARK_BROWN, (x + 80, y + 80, 80, 40), 2)
    ellipse(screen, color, (x + 410, y + 90, 80, 40))   # было 450, стало 410
    ellipse(screen, DARK_BROWN, (x + 410, y + 90, 80, 40), 2)

    # Хвост (СДВИНУТ ВЛЕВО на 40)
    ellipse(screen, color, (x + 480, y + 40, 170, 60))   # было 520, стало 480
    ellipse(screen, DARK_BROWN, (x + 480, y + 40, 170, 60), 2)

    # Глаза
    ellipse(screen, eye_color, (x, y + 10, 25, 15))
    ellipse(screen, eye_color, (x + 50, y + 10, 25, 15))

    # Зрачки
    ellipse(screen, BLACK, (x + 10, y + 10, 5, 15))
    ellipse(screen, BLACK, (x + 60, y + 10, 5, 15))

    # Нос 
    polygon(screen, (255, 180, 150), [(x + 35, y + 50), (x + 25, y + 40), (x + 45, y + 40)])

    # Усы
    line(screen, BLACK, (x - 10, y + 25), (x - 60, y + 15), 2)
    line(screen, BLACK, (x - 10, y + 30), (x - 60, y + 30), 2)
    line(screen, BLACK, (x - 10, y + 35), (x - 60, y + 45), 2)
    line(screen, BLACK, (x + 90, y + 25), (x + 140, y + 15), 2)
    line(screen, BLACK, (x + 90, y + 30), (x + 140, y + 30), 2)
    line(screen, BLACK, (x + 90, y + 35), (x + 140, y + 45), 2)

# Функция для маленького кота (лапы и хвост сдвинуты влево пропорционально)
def draw_small_cat(x, y, color, eye_color):
    # Тело
    ellipse(screen, color, (x, y, 133, 50))
    ellipse(screen, DARK_BROWN, (x, y, 133, 50), 1)

    # Голова
    circle(screen, color, (x + 13, y + 7), 23)
    circle(screen, DARK_BROWN, (x + 13, y + 7), 23, 1)

    # Уши
    polygon(screen, color, [(x - 5, y - 10), (x + 2, y - 27), (x + 15, y - 10)])
    polygon(screen, DARK_BROWN, [(x - 5, y - 10), (x + 2, y - 27), (x + 15, y - 10)], 1)
    polygon(screen, color, [(x + 17, y - 10), (x + 30, y - 27), (x + 35, y - 10)])
    polygon(screen, DARK_BROWN, [(x + 17, y - 10), (x + 30, y - 27), (x + 35, y - 10)], 1)

    # Розовые уши
    polygon(screen, EAR_PINK, [(x - 2, y - 12), (x + 2, y - 22), (x + 12, y - 12)])
    polygon(screen, EAR_PINK, [(x + 20, y - 12), (x + 30, y - 22), (x + 32, y - 12)])

    # Лапы (СДВИНУТЫ ВЛЕВО на 13)
    ellipse(screen, color, (x + 27, y + 27, 27, 13))    # было 40, стало 27
    ellipse(screen, DARK_BROWN, (x + 27, y + 27, 27, 13), 1)
    ellipse(screen, color, (x + 137, y + 30, 27, 13))   # было 150, стало 137
    ellipse(screen, DARK_BROWN, (x + 137, y + 30, 27, 13), 1)

    # Хвост (СДВИНУТ ВЛЕВО на 13)
    ellipse(screen, color, (x + 160, y + 13, 57, 20))   # было 173, стало 160
    ellipse(screen, DARK_BROWN, (x + 160, y + 13, 57, 20), 1)

    # Глаза
    ellipse(screen, eye_color, (x, y + 3, 8, 5))
    ellipse(screen, eye_color, (x + 17, y + 3, 8, 5))

    # Зрачки
    ellipse(screen, BLACK, (x + 3, y + 3, 2, 5))
    ellipse(screen, BLACK, (x + 20, y + 3, 2, 5))

    # Нос
    polygon(screen, (255, 180, 150), [(x + 12, y + 17), (x + 8, y + 13), (x + 16, y + 13)])

    # Усы
    line(screen, BLACK, (x - 3, y + 8), (x - 20, y + 5), 1)
    line(screen, BLACK, (x - 3, y + 10), (x - 20, y + 10), 1)
    line(screen, BLACK, (x - 3, y + 12), (x - 20, y + 15), 1)
    line(screen, BLACK, (x + 30, y + 8), (x + 47, y + 5), 1)
    line(screen, BLACK, (x + 30, y + 10), (x + 47, y + 10), 1)
    line(screen, BLACK, (x + 30, y + 12), (x + 47, y + 15), 1)

def draw_ball(x, y, size=1.0):
    radius = int(45 * size)
    circle(screen, YARN_GRAY, (x, y), radius)
    for angle in range(0, 180, 30):
        x1 = x + int(40 * size) * math.cos(math.radians(angle))
        y1 = y + int(40 * size) * math.sin(math.radians(angle))
        line(screen, YARN_DARK, (x, y), (x1, y1), max(1, int(2 * size)))
    line(screen, YARN_DARK, (x + int(30 * size), y - int(10 * size)), 
         (x + int(80 * size), y - int(30 * size)), max(1, int(2 * size)))

def draw_windows():
    for i in range(3):
        x = 200 + i * 350
        rect(screen, WINDOW_FRAME, (x, 50, 220, 170))
        rect(screen, WINDOW_GLASS, (x + 30, 80, 70, 50))
        rect(screen, WINDOW_GLASS, (x + 120, 80, 70, 50))
        rect(screen, WINDOW_GLASS, (x + 30, 140, 70, 50))
        rect(screen, WINDOW_GLASS, (x + 120, 140, 70, 50))

# Главный цикл
running = True
while running:
    # Фон
    rect(screen, WALL_BROWN, (0, 0, WIDTH, HEIGHT//2))
    rect(screen, FLOOR_BEIGE, (0, HEIGHT//2, WIDTH, HEIGHT//2))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_windows()
    
    # КОТЫ
    draw_big_cat(50, 200, ORANGE, GREEN)        # большой оранжевый
    draw_big_cat(550, 220, GRAY, BLUE)          # большой серый
    draw_small_cat(600, 100, ORANGE, GREEN)     # маленький оранжевый над серым
    draw_small_cat(50, 550, LIGHT_GRAY, BLUE)   # серый котёнок в левом углу
    draw_small_cat(150, 450, ORANGE, GREEN)     # рыжий под оранжевым
    draw_small_cat(300, 500, ORANGE, GREEN)     # ещё рыжий
    draw_small_cat(800, 600, LIGHT_GRAY, BLUE)  # серый котёнок внизу
    
    # Клубки
    draw_ball(1000, 350, 1.5)   # самый большой
    draw_ball(250, 400, 1.0)    # средний
    draw_ball(450, 600, 1.0)    # средний
    draw_ball(200, 550, 0.5)    # маленький
    draw_ball(350, 650, 0.5)    # маленький
    draw_ball(700, 500, 0.5)    # маленький
    draw_ball(900, 650, 0.5)    # маленький

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
