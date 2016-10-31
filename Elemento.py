import pygame
import sys



class Elem(tuple):
    def __str__(self):
        return ''.join(e for e in self)


pygame.init()

screen = pygame.display.set_mode((1240, 1080))
elementos = {Elem("h"): (255, 0, 0), Elem("o"): (0, 255, 0), Elem("a"): (0, 0, 255),
             Elem(["p", "b"]): (122, 122, 155), Elem(["u", "u", "s"]): (125, 210, 130)}
pygame.font = pygame.font.SysFont('Arial', 25)

keys = []
LEFT=1
RIGHT=3
RADIUS = 30

def desenhar_circulo():
    key = Elem(keys)
    try:
        cor = elementos[key]
    except KeyError:
        key = Elem("a")
        cor = elementos[key]

    x, y = pygame.mouse.get_pos()

    siglas=pygame.font.render(str(key), True, (255, 255, 255))

    sigla = siglas.get_rect()

    pygame.draw.circle(screen, cor, (x,y), RADIUS)
    screen.blit(siglas, (x-sigla.centerx, y-sigla.centery))
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
            keys.append(tecla)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pressionando = True
            if event.button == LEFT:
                desenhar_circulo()
            elif event.button == RIGHT:
                keys = []
        elif event.type == pygame.MOUSEBUTTONUP:
            pressionando = False
