import pygame
import os
from abc import ABC, abstractmethod

class Cenario(ABC):
    def __init__(self, identificador:str,
                 largura:int, altura:int,
                 eixo_x:int, eixo_y:int):
        self.__id_image = identificador
        self.__image = pygame.image.load(os.path.join('assets',
                                                      self.__id_image))
        self.__image = pygame.transform.scale(self.__image,
                                              (largura,
                                               altura))
        self.__rect = self.imagem.get_rect()
        self.__rect.center = (eixo_x), (eixo_y)

    @property
    def imagem(self):
        return self.__image

    @property
    def rect(self):
        return self.__rect
