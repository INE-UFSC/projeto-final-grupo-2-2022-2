import pygame

class Tela:
    def __init__(self) -> None:
        self.__largura = 1200
        self.__altura = 600
        self.__preto = pygame.Color(255, 255, 255)

        self.__display = pygame.display.set_mode((self.__largura,
                                                  self.__altura),
                                                  pygame.RESIZABLE)
        pygame.display.set_caption("mapa")
        self.__display.fill((255, 255, 255))
    
    @property
    def display(self):
        return self.__display
    
    @property
    def size(self):
        return self.__largura, self.__altura
    @size.setter
    def size(self, size:tuple[float] | list[float]):
        self.__largura, self.__altura = size
        self.__display = pygame.display.set_mode(size, pygame.RESIZABLE)