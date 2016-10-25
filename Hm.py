import pygame
import sys
import random


pygame.init()

screen = pygame.display.set_mode((1640,1480))
elementos = {"h": (255,0,0), "o": (0,255,0), "a": (0,0,255), "pb": (122,122,155)}
y=50

teclas={"a": pygame.K_a}

while (True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            for tecla in teclas:
                if event.key == teclas[tecla]:
                    pygame.draw.circle(screen, elementos[tecla], (50,y), 20)
                    pygame.display.update()

