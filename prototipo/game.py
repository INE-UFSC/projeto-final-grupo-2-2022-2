from random import Random, random
from re import T
from Acao import Acao, acoes
import pygame
import os
from element import Element

CHAR_WIDTH = 80
CHAR_HEIGHT = 70

pygame.init()
window = pygame.display.set_mode((900, 500), pygame.RESIZABLE)

# Elementos a serem mostrados na tela
char = Element(window, 'knight.png', 100, 200, CHAR_WIDTH, CHAR_HEIGHT)
char2 = Element(window, 'knight.png', 200, 100, CHAR_WIDTH, CHAR_HEIGHT)
char3 = Element(window, 'knight.png', 200, 300, CHAR_WIDTH, CHAR_HEIGHT)


enemy1 = Element(window, 'orc07.png', 700, 200, CHAR_WIDTH, CHAR_HEIGHT)
enemy2 = Element(window, 'orc07.png', 600, 100, CHAR_WIDTH, CHAR_HEIGHT)
enemy3 = Element(window, 'orc07.png', 600, 300, CHAR_WIDTH, CHAR_HEIGHT)


# Lista de elementos
team = [
    char,
    char2,
    char3
]

enemies = [
    enemy1,
    enemy2,
    enemy3
]

def update_window(window):
    window.fill((255, 255, 255))
    for i, element in enumerate(team):
        element.draw()
    for i, element in enumerate(enemies):
        element.draw()
    pygame.display.update()
    

def main(window):
    winw, winh = window.get_size()
    fps = 30
    clock = pygame.time.Clock()
    x_speed = 15
    y_speed = 15
    attack = False
    

    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.VIDEORESIZE:
                window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                winw, winh = window.get_size()
                pygame.display.update()

        keys_pressed = pygame.key.get_pressed()

        # if keys_pressed[pygame.K_LEFT] and char.x > 0:
        #     char.x -= x_speed
        #     char.file = 'knight_mirrored.png'

        # if keys_pressed[pygame.K_RIGHT] and char.x < winw - CHAR_WIDTH:
        #     char.x += x_speed
        #     char.file = 'knight.png'
        
        if event.type == pygame.MOUSEBUTTONDOWN or attack:
            if not attack:
                rand = Random()
                targetPos = rand.randint(0, 2)
                target = enemies[targetPos]
                x, y = char.rect.centerx - 10, char.rect.centery-10
                fireball = Element(window, 'fireball.png', x, y, 20, 20)
                team.append(fireball)
                attack = True
            else:
                fireball.rect.x += x_speed
                match targetPos:
                    case 0:
                        pass
                    case 1:
                        fireball.rect.y -= x_speed/5
                    case 2:
                        fireball.rect.y += x_speed/5

                if fireball.rect.collidepoint(target.rect.center):
                    attack = False
                    team.remove(fireball)
                    print("char2 -5 vida")
        
        # if keys_pressed[pygame.K_UP] and not jumping:
        #     jumping = True

        # elif jumping:
        #     char.y -= y_speed - jump_count
        #     jump_count += 1
        #     if jump_count > 2*y_speed:
        #         jumping = False
        #         jump_count = 0
            


        update_window(window)

if __name__ == "__main__":
    main(window)