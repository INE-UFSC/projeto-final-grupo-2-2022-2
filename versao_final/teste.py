import pygame

window = pygame.display.set_mode((1200, 600), pygame.RESIZABLE)
window.fill((255, 255, 255))
pygame.init()

run = True
fps = 60
clock = pygame.time.Clock()
while run:
    clock.tick(fps)

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
