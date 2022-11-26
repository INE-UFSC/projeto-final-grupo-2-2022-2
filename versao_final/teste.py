import pygame
from View.Sprite import Sprite

sprites = pygame.sprite.Group()

sprites.add(Sprite('mago', 80, 60, 200, 100))
sprites.add(Sprite('orc', 80, 60, 200, 200))
sprites.add(Sprite('knight', 80, 60, 200, 300))

window = pygame.display.set_mode((900, 500), pygame.RESIZABLE)
window.fill((255, 255, 255))

run = True
clock = pygame.time.Clock()


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    sprites.update()
    pygame.display.flip()
    sprites.draw(window)

    clock.tick(60)