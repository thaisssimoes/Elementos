import pygame
import sys
import random

pygame.init()

screen = pygame.display.set_mode((1240,1080))
elementos = {"h": (255,0,0), "o": (0,255,0), "a": (0,0,255), "pb": (122,122,155)}
teclas={"a": pygame.K_a, "o": pygame.K_o, "h": pygame.K_h}

y=50
x=50

while (True):
    for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                for tecla in teclas:
                    if event.key == teclas[tecla]:
                        pygame.draw.circle(screen, elementos[tecla], pygame.mouse.get_pos(), 20)
                        pygame.display.update()

            elif event.type== pygame.MOUSEBUTTONDOWN:
                for tecla in teclas:
                    pygame.draw.circle(screen, elementos[tecla], pygame.mouse.get_pos(), 20)
                    pygame.display.update()

            elif event.type== pygame.MOUSEBUTTONUP:
                for tecla in teclas:
                    pygame.draw.circle(screen, elementos[tecla], pygame.mouse.get_pos(), 20)
                    pygame.display.update()

            elif event.type == pygame.MOUSEMOTION:
                for tecla in teclas:
                    pygame.draw.circle(screen, elementos[tecla], pygame.mouse.get_pos(), 20)
                    pygame.display.update()
