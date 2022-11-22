import pygame
import os


class Mapa():
    def __init__(self, locais, id_image, altura, largura, eixo_x, eixo_y):
        pygame.sprite.Sprite.__init__(self)
        self.__altura = altura
        self.__largura = largura
        self.__eixo_x = eixo_x
        self.__eixo_y = eixo_y
        self.__locais = locais
        self.__id_image = id_image
        temp = os.getcwd().split(os.path.sep)
        temp.remove("View")
        temp = os.path.sep.join(temp)
        self.__caminho = os.path.join(temp, "assets")
        self.__image = pygame.image.load(os.path.join(self.__caminho, f'{id_image}')).convert()
        self.__image = pygame.transform.scale(self.__image, (largura, altura))
        self.__rect = self.__image.get_rect()
        self.__rect.center = (eixo_x), (eixo_y)

    @property
    def id_imagem(self):
        return self.__id_image

    @property
    def locais(self):
        return self.__locais

    def escolher_local(self, destino: str):
        local_escolhido = self.__locais[destino]
        return local_escolhido

    @property
    def imagem(self):
        return self.__image

    @property
    def rect(self):
        return self.__rect
