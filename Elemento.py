import pygame
import sys



class Elem(frozenset):
    def __str__(self):
        return ''.join(e for e in self)


pygame.init()

screen = pygame.display.set_mode((1240, 1080))
elementos = {Elem("h"): (255, 0, 0), Elem("o"): (0, 255, 0), Elem("a"): (0, 0, 255),
             Elem(["p", "b"]): (122, 122, 155)}
pygame.font = pygame.font.SysFont('Arial', 25)

keys = set()
LEFT=1
RIGHT=3

def desenhar_circulo():
    key = Elem(keys)
    try:
        cor = elementos[key]
    except KeyError:
        key = Elem("a")
        cor = elementos[key]

    x, y = pygame.mouse.get_pos()

    siglas=pygame.font.render(str(key), True, (255, 255, 255))

    pygame.draw.circle(screen, cor, pygame.mouse.get_pos(), 20)
    screen.blit(siglas, (x-13, y-15))
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

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pressionando = True
            if event.button == LEFT:
                desenhar_circulo()
            elif event.button == RIGHT:
                keys.clear()

        elif event.type == pygame.MOUSEBUTTONUP:
            pressionando = False
