import os
from Model.Personagem import Personagem
import pygame

class PersonagemView:
    def __init__(self, surface:pygame.Surface,
                 char:Personagem, x:float, y:float,
                 width:int, height:int):
        self.__surface = surface
        self.__char = char
        self.__width = width
        self.__height = height
        self.__rect = pygame.Rect(x, y, width, height)
        self.__image = self.set_image()
        self.draw()
    
    def draw(self):
        self.__surface.blit(self.__image, (self.__rect.x, self.__rect.y))
        health = str(self.__char.get_saude())
        font = pygame.font.SysFont('Comic Sans MS', 20)
        text = font.render(health, True, (0, 0, 0))
        x, y, w = self.__rect.x, self.__rect.y, self.__rect.width
        self.__surface.blit(text, text.get_rect(center=(x + w/2, y)))
    


    def set_image(self):
        var = self.__char.classe + '.png'
        tempImage = pygame.image.load(os.path.join('versao_final/assets',
                                                   var))
        return pygame.transform.scale(tempImage,
                                      (self.__width,
                                       self.__height))

    @property
    def surface(self):
        return self.__surface
    @surface.setter
    def surface(self, surface:pygame.Surface):
        self.__surface = surface
        self.draw()

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

    @property
    def char(self):
        return self.__char
    @char.setter
    def char(self, char:Personagem):
        self.__char = char

    @property
    def rect(self):
        return self.__rect
    @rect.setter
    def rect(self, rect:pygame.Rect):
        self.__rect = rect