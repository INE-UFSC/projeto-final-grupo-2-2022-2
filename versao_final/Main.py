from Controller.Controller import Controller
import pygame

pygame.init()

jogo = Controller()

run = True
fps = 60
clock = pygame.time.Clock()

while run:
    clock.tick(fps)
    
    run = jogo.rodaBatalha()

    pygame.display.update()