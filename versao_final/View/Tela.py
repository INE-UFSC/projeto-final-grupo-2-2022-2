import pygame

class Tela:
    def __init__(self) -> None:
        self.__largura = 1600
        self.__altura = 900

        self.__display = pygame.display.set_mode((self.__largura,
                                                  self.__altura),
                                                  pygame.RESIZABLE)
        pygame.display.set_caption("mapa")
        self.__display.fill((255, 255, 255))
    
    @property
    def display(self):
        return self.__display
    @display.setter
    def display(self, display):
        self.__display = display

    
    @property
    def size(self):
        return self.__largura, self.__altura
    @size.setter
    def size(self, size:tuple[float] | list[float]):
        self.__largura, self.__altura = size
        self.__display = pygame.display.set_mode(size, pygame.RESIZABLE)