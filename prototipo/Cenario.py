from Jogo import Jogo
import pygame
import os
class Cenario(pygame.sprite.Sprite):
    def __init__(self, identificador:str,largura:int,altura:int,eixo_x:int,eixo_y:int,x_hit,y_hit,hit_largura,hit_altura):
        self.__id = identificador
        pygame.sprite.Sprite.__init__(self)
        self.__clicked = False
        self.__identificador = identificador
        self.image = pygame.image.load(os.path.join("assets",f'{identificador}')).convert()
        self.image = pygame.transform.scale(self.image,(largura, altura))
        self.rect = self.imagem.get_rect()
        self.rect.center = (eixo_x), (eixo_y)
        self.__x_hit = x_hit
        self.__y_hit = y_hit
        self.__hitbox = pygame.Rect(x_hit, y_hit , hit_largura, hit_altura)

    @property
    def hitbox(self):
        return self.__hitbox
    @property
    def imagem(self):
        return self.image
    @property
    def clicked(self):
        return self.__clicked
    @clicked.setter
    def clicked(self,novo_clicked:bool):
        self.__clicked = novo_clicked

