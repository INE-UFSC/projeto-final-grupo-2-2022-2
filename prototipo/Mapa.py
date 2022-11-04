from Jogo import Jogo
from Cenario import Cenario
import pygame

class Mapa(pygame.sprite.Sprite):
    def __init__(self, locais, id_image,altura,largura,eixo_x,eixo_y):
        pygame.sprite.Sprite.__init__(self)
        self.__altura = altura
        self.__largura = largura
        self.__eixo_x = eixo_x
        self.__eixo_y = eixo_y
        self.__locais = locais
        self.__id_image = id_image
        self.image = pygame.image.load(f'assets/{id_image}.jpg').convert()
        self.image = pygame.transform.scale(self.image, (largura, altura))
        self.rect = self.image.get_rect()
        self.rect.center = (eixo_x), (eixo_y)
    
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
        return self.image