from button import Button
import pygame
from window import Window
from panel import Panel

def menuElements(menu:Window) -> dict[str, pygame.Surface]:
    menuW, menuH = menu.surface.get_size()
    btnW, btnH = 200, 50
    btnPos_x, btnPos_y = menuW/2 - btnW/2, menuH/4 - btnH/2

    elements = {'buttonPlay': Button(btnW, btnH, btnPos_x, btnPos_y, menu, 'PLAY').draw(),
                'buttonOptions': Button(btnW, btnH, btnPos_x, btnPos_y + 2*btnH, menu, 'OPTIONS').draw(),
                'buttonQuit': Button(btnW, btnH, btnPos_x, btnPos_y + 4*btnH, menu, 'QUIT').draw()}

    pygame.display.update()

    return elements

def menu():
    run = True
    menu = Window(800, 600)
    fps = 10
    clock = pygame.time.Clock()

    elements = menuElements(menu)

    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.VIDEORESIZE:
                menu.updateSize(event.w, event.h)
                elements = menuElements(menu)
            for element in elements:
                if elements[element].collidepoint(pygame.mouse.get_pos()):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

                
            # if elements['buttonPlay'].collidepoint(pygame.mouse.get_pos()):
            #     print("play")
            # if elements['buttonOptions'].collidepoint(pygame.mouse.get_pos()):
            #     print("Options")
            # if elements['buttonQuit'].collidepoint(pygame.mouse.get_pos()):
            #     print("Quit")
            # if newGameButton.get_rect().collidepoint(pygame.mouse.get_pos()):
            #     print "mouse is over 'newGameButton'"
    pygame.quit()

pygame.init()
menu()