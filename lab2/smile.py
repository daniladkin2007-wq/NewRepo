import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

LIGHT_BLUE = (173, 216, 230)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

rect(screen, LIGHT_BLUE, (0, 0, 400, 400))

circle(screen, YELLOW, (200, 200), 100)
circle(screen, BLACK, (200, 200), 100, 2)

circle(screen, RED, (150, 170), 20)
circle(screen, BLACK, (150, 170), 8)

circle(screen, RED, (250, 170), 15)
circle(screen, BLACK, (250, 170), 7)

line(screen, BLACK, (110, 120), (160, 140), 8)
line(screen, BLACK, (290, 120), (240, 140), 8)

rect(screen, BLACK, (150, 240, 100, 20))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
