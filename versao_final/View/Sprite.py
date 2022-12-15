import pygame
import os
from Singleton.Animacao import Animacao
from time import sleep

class Sprite(pygame.sprite.Sprite):
    def __init__(self, filename:str, posicao: list[float]) -> None:
        super().__init__()
        self.__filename = filename
        self.__width, self.__height = 80, 80
        self.image = self.setImage()
        self.rect.center = posicao
        self.__posicao = posicao
        self.__progressoAnimacao = 0
    
    def setImage(self):
        img = pygame.image.load(os.path.join('assets', f'{self.__filename}.png'))
        image = pygame.transform.scale(img, (self.__width, self.__height))
        self.rect = image.get_rect()
        return image

    def moveAtacante(self):
        if Animacao().fase == 0:
            self.rect.x += 2
            self.__progressoAnimacao += 1
            
            if self.__progressoAnimacao == 10:
                Animacao().fase = 1

        elif Animacao().fase == 1 and self.__progressoAnimacao != 0:
            self.rect.x -= 2
            self.__progressoAnimacao -= 1


    def moveAlvo(self):
        if self.__progressoAnimacao == 0:
            self.rect.x += 4
            self.rect.y += 4
            self.__progressoAnimacao += 1
            
        elif self.__progressoAnimacao == 1:
            self.rect.x -= 4
            self.rect.y -= 4
            self.__progressoAnimacao += 1
        else:
            sleep(0.5)
            Animacao().fase = 0
            Animacao().finished = True
            self.__progressoAnimacao = 0
    @property
    def posicao(self):
        return self.__posicao
    
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, new:int):
        self.__width = new
        self.setImage()
    
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, new:int):
        self.__height = new
        self.setImage()
    
    @property
    def posicao(self):
        return self.__posicao
    @posicao.setter
    def posicao(self, new:int):
        self.__posicao = new
        self.rect.center = new
