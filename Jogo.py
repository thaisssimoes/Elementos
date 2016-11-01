import sys
import pygame
from Elementos import elemento

LEFT=1
RIGHT=3

elemento = elemento()

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            tecla = pygame.key.name(event.key)
            elemento.keys.append(tecla)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == LEFT:
                elemento.desenhar_circulo()
            elif event.button == RIGHT:
                elemento.keys = []

