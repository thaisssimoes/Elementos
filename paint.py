import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1240,1080))
elementos = {frozenset("h"): (255,0,0), frozenset("o"): (0,255,0), frozenset("a"): (0,0,255), frozenset(["p", "b"]): (122,122,155)}

pressed_keys = set()
is_pintando = False



def desenhar_circulo():
    try:
        key = frozenset(pressed_keys)
        cor = elementos[key]
    except KeyError:
        cor = elementos['a']
    pygame.draw.circle(screen, cor, pygame.mouse.get_pos(), 20)
    pygame.display.update()

def devo_pintar():
    return is_pintando and pressed_keys



while (True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            tecla = pygame.key.name(event.key)
            pressed_keys.add(tecla)

        elif event.type == pygame.KEYUP:
            tecla = pygame.key.name(event.key)
            pressed_keys.remove(tecla)

        elif event.type== pygame.MOUSEBUTTONDOWN:
            is_pintando = True
            if devo_pintar():
                desenhar_circulo()

        elif event.type== pygame.MOUSEBUTTONUP:
            is_pintando = False

        elif event.type == pygame.MOUSEMOTION:
            if devo_pintar():
                desenhar_circulo()
