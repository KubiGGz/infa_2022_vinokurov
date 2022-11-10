import pygame
from pygame.draw import *
from pygame.color import THECOLORS
import sys

pygame.init()
#Дисплей
screen = pygame.display.set_mode((1200, 800))
#Голова
pygame.draw.circle(screen, (255,255,153) , (600, 400), 300, width=0)
#Брови
pygame.draw.lines(screen, (105,105,105), False, [(350, 200), (550, 250)], width=25)
pygame.draw.lines(screen, (105,105,105), False, [(650, 250), (850, 200)], width=25)
#Глаза
pygame.draw.circle(screen, (255,0,0), (450, 330), 70, width=0)
pygame.draw.circle(screen, (255,0,0), (750, 330), 70, width=0)
pygame.draw.circle(screen, (0,0,0), (450, 330), 30, width=0)
pygame.draw.circle(screen, (0,0,0), (750, 330), 30, width=0)
#Рот
pygame.draw.line(screen, (0,0,0), (450, 500), (730, 500), width=35)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()


