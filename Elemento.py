import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1240,1080))
elementos = {"h": (255,0,0), "o": (0,255,0), "a": (0,0,255), "pb": (122,122,155)}
teclas={"a": pygame.K_a, "o": pygame.K_o, "h": pygame.K_h}
pygame.font = pygame.font.SysFont('Arial', 25)


while (True):
    x,y = pygame.mouse.get_pos()
    for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                for tecla in teclas:
                    if event.key == teclas[tecla]:
                        pygame.draw.circle(screen, elementos[tecla], pygame.mouse.get_pos(), 20)
                        screen.blit(pygame.font.render(tecla, True, (255, 255, 255)), (x-5, y-16) )
                        pygame.display.update()




