import pygame

from View.button import Button
from View.window import Window
from View.tela_mapa import TelaMapa

class Menu():
    def __init__(self) -> None:
        # self.__mapa = TelaMapa()
        self.__play = False

    def showElements(self, menu:Window) -> dict[str, pygame.Surface]:
        menuW, menuH = menu.surface.get_size()
        btnW, btnH = 200, 50
        btnPos_x, btnPos_y = menuW/2 - btnW/2, menuH/4 - btnH/2

        elements = {'buttonPlay': Button(btnW, btnH, btnPos_x, btnPos_y, menu, 'PLAY'),
                    'buttonOptions': Button(btnW, btnH, btnPos_x, btnPos_y + 2*btnH, menu, 'OPTIONS'),
                    'buttonQuit': Button(btnW, btnH, btnPos_x, btnPos_y + 4*btnH, menu, 'QUIT')}
        
        for element in elements.values():
            element.draw()

        pygame.display.update()

        return elements

    def runMenu(self):
        run = True
        menu = Window(900, 500)
        fps = 10
        clock = pygame.time.Clock()

        elements = self.showElements(menu)

        while run:
            clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.VIDEORESIZE:
                    menu.updateSize(event.w, event.h)
                    elements = self.showElements(menu)
                if event.type == pygame.MOUSEBUTTONDOWN and elements['buttonPlay'].button.collidepoint(pygame.mouse.get_pos()):
                    return True
                if event.type == pygame.MOUSEBUTTONDOWN and elements['buttonQuit'].button.collidepoint(pygame.mouse.get_pos()):
                    run = False
                    
                # if elements['buttonPlay'].collidepoint(pygame.mouse.get_pos()):
                #     print("play")
                # if elements['buttonOptions'].collidepoint(pygame.mouse.get_pos()):
                #     print("Options")
                # if elements['buttonQuit'].collidepoint(pygame.mouse.get_pos()):
                #     print("Quit")
                # if newGameButton.get_rect().collidepoint(pygame.mouse.get_pos()):
                #     print "mouse is over 'newGameButton'"
        pygame.quit()
    
    @property
    def play(self) -> None:
        return self.__play