import pygame

class Elem(tuple):
    def __str__(self):
        return ''.join(e for e in self)


class elemento():
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1240, 1080))
        self.elementos = {Elem("h"): (255, 0, 0),
                          Elem("o"): (0, 255, 0),
                          Elem("i"): (0, 0, 255),
                          Elem(["p", "b"]): (122, 122, 155),
                          Elem(["u", "u", "s"]): (125, 210, 130),
                          Elem("v"): (100, 140, 173),
                          Elem(["t","e"]): (89, 115, 220),
                          Elem(["a","s"]): (220, 205, 2)}

        pygame.font = pygame.font.SysFont('Verdana', 25)
        self.keys = []

        self.RADIUS = 30

    def desenhar_circulo(self):
        self.key = Elem(self.keys)
        try:
            cor = self.elementos[self.key]
        except KeyError:
            self.key = Elem("i")
            cor = self.elementos[self.key]

        self.x, self.y = pygame.mouse.get_pos()
        pygame.draw.circle(self.screen, cor, (self.x,self.y), self.RADIUS)
        self.escrever_elemento()
        pygame.display.update()

    def escrever_elemento(self):
        self.siglas = pygame.font.render(str(self.key).capitalize(), True, (255, 255, 255))
        self.sigla = self.siglas.get_rect()
        self.screen.blit(self.siglas, (self.x-self.sigla.centerx, self.y-self.sigla.centery))
