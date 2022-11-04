import os
from Personagem import Personagem
import pygame

class Element:
    def __init__(self, surface:pygame.Surface,
                 char:Personagem, x:float, y:float) -> None:
        self.__surface = surface
        self.__char = char
        self.__rect = pygame.Rect(x, y, char.size[0], char.size[1])
        # self.__image = pygame.image.load(os.path.join('prototipo/assets', file))
        # self.__image = pygame.transform.scale(self.__image, (width, height))
        self.draw()
    
    def draw(self):
        self.__surface.blit(self.__char.image, (self.__rect.x, self.__rect.y))
        health = str(self.__char.get_saude())
        font = pygame.font.SysFont('Comic Sans MS', 20)
        text = font.render(health, True, (0, 0, 0))
        x, y, w = self.__rect.x, self.__rect.y, self.__rect.width
        self.__surface.blit(text, text.get_rect(center=(x + w/2, y)))
    


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
    def width(self, width:float):
        self.__width = width

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, height:float):
        self.__height = height

    @property
    def char(self):
        return self.__char
    @char.setter
    def char(self, char:str):
        self.__char = char

    @property
    def rect(self):
        return self.__rect
    @rect.setter
    def rect(self, rect:pygame.Rect):
        self.__rect = rect
    
