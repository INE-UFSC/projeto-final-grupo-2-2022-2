import pygame
import os

class Tela:
    def __init__(self):
        self.__largura = 800
        self.__altura = 500
        self.__fps = 60

        self.__preto = pygame.Color(0, 0, 0)

        pygame.init()
        self.__display = pygame.display.set_mode((self.__largura,
                                                  self.__altura))
        pygame.display.set_caption("mapa")
        self.__clock = pygame.time.Clock()
        self.__display.fill(self.__preto)


    @property
    def fps(self):
        return self.__fps

    @property
    def display(self):
        return self.__display

    @property
    def clock(self):
        return self.__clock
