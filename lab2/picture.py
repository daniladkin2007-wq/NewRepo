import pygame
import math
from pygame.draw import *

pygame.init()


WIDTH, HEIGHT = 700, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

WALL_BROWN = (139, 90, 43)        
FLOOR_BEIGE = (222, 184, 135)
LIGHT_BROWN = (190, 110, 50)
EAR_PINK = (240, 200, 180)
GREEN = (120, 200, 0)
BLACK = (0, 0, 0)
DARK_BROWN = (101, 67, 33)
GRAY = (170, 170, 170)
WINDOW_FRAME = (200, 230, 220)
WINDOW_GLASS = (120, 180, 200)

clock = pygame.time.Clock()

def draw_cat():

    ellipse(screen, LIGHT_BROWN, (150, 240, 400, 150))
    ellipse(screen, DARK_BROWN, (150, 240, 400, 150), 2)


    circle(screen, LIGHT_BROWN, (190, 260), 70)
    circle(screen, DARK_BROWN, (190, 260), 70, 2)

    # Уши
    polygon(screen, LIGHT_BROWN, [(135, 210), (155, 140), (195, 190)])
    polygon(screen, DARK_BROWN, [(135, 210), (155, 140), (195, 190)], 2)
    
    polygon(screen, LIGHT_BROWN, [(200, 190), (240, 140), (255, 225)])
    polygon(screen, DARK_BROWN, [(200, 190), (240, 140), (255, 225)], 2)

    polygon(screen, EAR_PINK, [(145, 200), (155, 155), (185, 185)])
    polygon(screen, EAR_PINK, [(210, 185), (240, 155), (245, 210)])

    # Лапы
    ellipse(screen, LIGHT_BROWN, (120, 320, 80, 40))
    ellipse(screen, DARK_BROWN, (120, 320, 80, 40), 2)
    
    ellipse(screen, LIGHT_BROWN, (450, 340, 80, 40))
    ellipse(screen, DARK_BROWN, (450, 340, 80, 40), 2)

    # Хвост 
    ellipse(screen, LIGHT_BROWN, (520, 265, 170, 60))
    ellipse(screen, DARK_BROWN, (520, 265, 170, 60), 2)

    # Глаза
    ellipse(screen, GREEN, (150, 250, 25, 15))
    ellipse(screen, GREEN, (200, 250, 25, 15))

    # Зрачки
    ellipse(screen, BLACK, (165, 250, 5, 15))
    ellipse(screen, BLACK, (215, 250, 5, 15))

    # Нос 
    polygon(screen, (255, 180, 150), [(185, 290), (175, 280), (195, 280)])

    # Усы
    line(screen, BLACK, (140, 265), (80, 255), 2)
    line(screen, BLACK, (140, 270), (80, 270), 2)
    line(screen, BLACK, (140, 275), (80, 285), 2)
    line(screen, BLACK, (240, 265), (300, 255), 2)
    line(screen, BLACK, (240, 270), (300, 270), 2)
    line(screen, BLACK, (240, 275), (300, 285), 2)

def draw_window():
    # Окно
    rect(screen, WINDOW_FRAME, (400, 30, 250, 200))
    rect(screen, WINDOW_GLASS, (420, 50, 90, 70))
    rect(screen, WINDOW_GLASS, (530, 50, 90, 70))
    rect(screen, WINDOW_GLASS, (420, 130, 90, 80))
    rect(screen, WINDOW_GLASS, (530, 130, 90, 80))

def draw_ball():
    # Клубок
    circle(screen, GRAY, (450, 400), 45)

    for angle in range(0, 180, 30):
        x = 450 + 40 * math.cos(math.radians(angle))
        y = 400 + 40 * math.sin(math.radians(angle))
        line(screen, BLACK, (450, 400), (x, y), 1)

    line(screen, BLACK, (480, 390), (530, 370), 2)

running = True
while running:
    # Фон
    rect(screen, WALL_BROWN, (0, 0, WIDTH, HEIGHT//2))
    rect(screen, FLOOR_BEIGE, (0, HEIGHT//2, WIDTH, HEIGHT//2))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_window()
    draw_cat()
    draw_ball()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
