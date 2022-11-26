import os
import pygame

class Sprite(pygame.sprite.Sprite):

    def __init__(self, filename:str, width:float, height:float, x:float, y:float) -> None:
        super().__init__()
        self.__filename = filename
        self.__width = width
        self.__height = height
        self.image = self.setImage()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    
    def setImage(self):
        img = pygame.image.load(os.path.join('versao_final', 'assets', f'{self.__filename}.png'))
        image = pygame.transform.scale(img, (self.__width, self.__height))
        return image

    def set_image(self, filename):
        filename += '.png'
        tempImage = pygame.image.load(os.path.join('versao_final/assets', filename))
        self.image = pygame.transform.scale(tempImage, (self.__width, self.__height))
    
    def set_health(self, health:int):
        self.__health = health

    @property
    def surface(self):
        return self.__surface
    @surface.setter
    def surface(self, surface:pygame.Surface):
        self.__surface = surface

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, width:int):
        self.__width = width

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, height:int):
        self.__height = height
