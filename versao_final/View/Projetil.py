import pygame
import os
from Singleton.Animacao import Animacao

class Projetil(pygame.sprite.Sprite):
    def __init__(self, filename: str, posicao: list[float] = (0, 0)) -> None:
        super().__init__()
        self.__filename = filename
        self.__width, self.__height = 50, 50
        self.image = self.setImage()
        self.rect = self.image.get_rect()
        self.rect.center = posicao
        self.__posicao = pygame.math.Vector2()
        self.__direcao = pygame.math.Vector2(posicao)
        self.__posicaoInicial = posicao
    
    def move(self, posicao: list[float]):
        self.__direcao = (pygame.math.Vector2(posicao) - self.__posicao).normalize()
        self.__posicao += self.__direcao * 15
        self.rect.center = round(self.__posicao.x), round(self.__posicao.y)
        
        if self.rect.collidepoint(posicao):
            Animacao().fase = 2
            self.rectCenter = self.__posicaoInicial # Volta a sprite para a posição original
            self.kill()
            return True
        return False
    
    def setImage(self):
        img = pygame.image.load(os.path.join('assets', f'{self.__filename}.png'))
        image = pygame.transform.scale(img, (self.__width, self.__height))
        return image
    
    @property
    def rectCenter(self):
        return self.rect.center
    @rectCenter.setter
    def rectCenter(self, posicao):
        self.rect.center = posicao
        self.__posicao = pygame.math.Vector2(posicao)
        self.__direcao = pygame.math.Vector2(posicao)
        self.__posicaoInicial = posicao
    
    @property
    def nome(self):
        return self.__filename
    
    @property
    def size(self):
        return self.__width, self.__height