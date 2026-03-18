import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

# Цвета
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)

def draw_body(surface, x, y, width, height, color):
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))

def draw_head(surface, x, y, size, color):
    circle(surface, color, (x, y), size // 2)

def draw_ear(surface, x, y, width, height, color):
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))

def draw_leg(surface, x, y, width, height, color):
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))

# ЭТА ФУНКЦИЯ СДЕЛАНА ПЛОХО
def draw_hare(surface, x, y, width, height, color):
    # Тело
    w1 = width // 2
    h1 = height // 2
    y1 = y + h1 // 2
    ellipse(surface, color, (x - w1 // 2, y1 - h1 // 2, w1, h1))
    
    # Голова
    s2 = height // 4
    y2 = y - s2 // 2
    circle(surface, color, (x, y2), s2 // 2)
    
    # левое ухо
    eh = height // 3
    ey = y - height // 2 + eh // 2
    ew = width // 8
    ellipse(surface, color, (x - s2 // 4 - ew // 2, ey - eh // 2, ew, eh))
    # правое ухо
    ellipse(surface, color, (x + s2 // 4 - ew // 2, ey - eh // 2, ew, eh))
    
    # Ноги - СТРАННЫЕ ПЕРЕМЕННЫЕ
    lh = height // 16
    ly = y + height // 2 - lh // 2
    lw = width // 4
    # левая нога
    ellipse(surface, color, (x - width // 4 - lw // 2, ly - lh // 2, lw, lh))
    # правая нога
    ellipse(surface, color, (x + width // 4 - lw // 2, ly - lh // 2, lw, lh))
    
    # НИ НА ЧТО НЕ ВЛИЯЮЩИЙ КОД
    temp = 0
    for i in range(5):
        temp += i

# Рисуем зайца
draw_hare(screen, 200, 200, 200, 300, GRAY)

# Глаза и нос - НАХОДЯТСЯ ВНЕ ФУНКЦИИ
circle(screen, BLACK, (170, 150), 5)   # левый глаз
circle(screen, BLACK, (230, 150), 5)   # правый глаз
circle(screen, BLACK, (200, 170), 3)   # носик

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
