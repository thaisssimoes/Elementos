import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1240,1080))
elementos = {frozenset("h"): (255,0,0), frozenset("o"): (0,255,0), frozenset("a"): (0,0,255), frozenset(["p","b"]): (122,122,155)}
pygame.font = pygame.font.SysFont('Arial', 25)

keys = set()

def desenhar_circulo():
    try:
        key = frozenset(keys)
        cor = elementos[key]
    except KeyError:
        cor = elementos[frozenset(["a"])]

    x,y = pygame.mouse.get_pos()
    pygame.draw.circle(screen, cor, pygame.mouse.get_pos(), 20)
    screen.blit(pygame.font.render(str(key), True, (255, 255, 255)), (x - 6, y - 14))
    pygame.display.update()

def devo_pintar():
    return pressionando and keys


while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            tecla = pygame.key.name(event.key)
            keys.add(tecla)

        elif event.type == pygame.KEYUP:
            tecla = pygame.key.name(event.key)
            if tecla == "escape":
                keys.clear()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pressionando = True
            desenhar_circulo()

        elif event.type == pygame.MOUSEBUTTONUP:
            pressionando = False