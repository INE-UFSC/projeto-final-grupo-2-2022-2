from Model.CenarioModel import CenarioModel
import pygame
import os


class Mapa():
    def __init__(self, locais:list[CenarioModel],
                 id_image:str, altura:int, largura:int,
                 eixo_x:int, eixo_y:int):
        pygame.sprite.Sprite.__init__(self)
        self.__altura = altura
        self.__largura = largura
        self.__eixo_x = eixo_x
        self.__eixo_y = eixo_y
        self.__locais = locais
        self.__id_image = id_image
        self.__image = pygame.image.load(os.path.join('versao_final',
                                                      'assets',
                                                      f'{self.__id_image}.png')
                                         ).convert()
        self.__image = pygame.transform.scale(self.__image,
                                              (largura, altura))
        self.__rect = self.__image.get_rect()
        self.__rect.center = (eixo_x), (eixo_y)

    @property
    def id_imagem(self) -> str:
        return self.__id_image

    @property
    def locais(self) -> list[CenarioModel]:
        return self.__locais

    def escolher_local(self, destino:int) -> CenarioModel:
        return self.__locais[destino]

    @property
    def imagem(self):
        return self.__image

    @property
    def rect(self):
        return self.__rect