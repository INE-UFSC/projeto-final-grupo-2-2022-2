import pygame
from Singleton.Constantes import Constantes

class Tela:
    def __init__(self) -> None:
        size = Constantes().screenSize

        self.__preto = pygame.Color(255, 255, 255)

        self.__display = pygame.display.set_mode(size,
                                        pygame.RESIZABLE)
        pygame.display.set_caption("mapa")
        self.__display.fill((255, 255, 255))
    
    @property
    def display(self):
        return self.__display