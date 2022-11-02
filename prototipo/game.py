from random import Random, random
from re import T

from combatClasses.mago import Mago


from Batalha import Batalha
from Acao import Acao, acoes
import pygame
import os
from element import Element

pygame.init()
window = pygame.display.set_mode((900, 500), pygame.RESIZABLE)

# Elementos a serem mostrados na tela
mago = Mago('belzebu', 5, 100, acoes)
char = Element(window, mago, 100, 200)
# char2 = Element(window, 'knight.png', 200, 100)
# char3 = Element(window, 'knight.png', 200, 300)


enemy1 = Element(window, mago, 700, 200)
enemy2 = Element(window, mago, 600, 100)
enemy3 = Element(window, mago, 600, 300)


# Lista de elementos
team = [
    char,
    # char2,
    # char3
]

team2 = [
    enemy1,
    enemy2,
    enemy3
]

def update_window(window):
    window.fill((255, 255, 255))
    for i, element in enumerate(team):
        element.draw()
    for i, element in enumerate(team2):
        element.draw()
    pygame.display.update()
    

def main(window):
    winw, winh = window.get_size()
    fps = 60
    clock = pygame.time.Clock()
    x_speed = 15
    click = False
    allies, enemies = [i.char for i in team], [i.char for i in team2]
    battle = Batalha(allies, enemies)
    finished = False
    

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
        
        if event.type == pygame.MOUSEBUTTONDOWN and not click and not finished:
            click = True
            if not enemies:
                print("allies win")
                finished = True
            elif not allies:
                print("enemies win")
                finished = True
            else:
                allies, enemies = battle.turno()
        
        if event.type == pygame.MOUSEBUTTONUP:
            click = False



            # if not attack:
            #     rand = Random()
            #     targetPos = rand.randint(0, 2)
            #     target = enemies[targetPos]
            #     x, y = char.rect.centerx - 10, char.rect.centery-10
            #     fireball = Element(window, 'fireball.png', x, y, 20, 20)
            #     team.append(fireball)
            #     attack = True
            # else:
            #     fireball.rect.x += x_speed
            #     match targetPos:
            #         case 0:
            #             pass
            #         case 1:
            #             fireball.rect.y -= x_speed/5
            #         case 2:
            #             fireball.rect.y += x_speed/5

            #     if fireball.rect.collidepoint(target.rect.center):
            #         attack = False
            #         team.remove(fireball)
            #         print("char2 -5 vida")
            


        update_window(window)

if __name__ == "__main__":
    main(window)