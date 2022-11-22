import pygame
from View.panel import Panel
from View.window import Window

class Button(Panel):
    def __init__(self, width, height, pos_x, pos_y, window:Window, text:str) -> None:
        super().__init__(width, height, pos_x, pos_y)
        self.__button = None
        self.__window = window
        self.__text = text
        self.__font = pygame.font.SysFont('Comic Sans MS', 35)

    def draw(self) -> pygame.Surface:
        # Atribuição de variáveis width, height, pos_x, e pos_y
        w, h, x, y = super().width, super().height, super().pos_x, super().pos_y
        # Criação e desenho do botão
        self.__button = pygame.Rect(x, y, w, h)
        pygame.draw.rect(self.__window.surface, (255, 0, 0), self.__button)
        # Criação do texto do botão
        btn = self.__font.render(self.__text, True, (255, 255, 255))
        btnRect = btn.get_rect()
        btnRect.left, btnRect.top = x, y
        # Atualização da tela com o texto
        print(btn.get_rect(center=(x + w/2, y + h/2)))
        self.__window.add(btn, btn.get_rect(center=(x + w/2, y + h/2)))
        # Atualização do display
        pygame.display.update()
        return btnRect
    
    @property
    def button(self):
        return self.__button
    @button.setter
    def button(self, button):
        self.__button = button

    @property
    def window(self):
        return self.__window
    @window.setter
    def window(self, window):
        self.__window = window