import os
import pygame
class Element:
    def __init__(self, surface:pygame.Surface, file:str, x:float, y:float, width:float, height:float) -> None:
        self.__surface = surface
        self.__file = file
        self.__width = width
        self.__height = height
        self.__rect = pygame.Rect(x, y, width, height)
        self.__image = pygame.image.load(os.path.join('projeto-final-grupo-2-2022-2/prototipo/assets', file))
        self.__image = pygame.transform.scale(self.__image, (width, height))
        self.draw()
    
    def draw(self):
        self.__surface.blit(self.__image, (self.__rect.x, self.__rect.y))
    


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
    def image(self):
        return self.__image
    @image.setter
    def image(self, image:pygame.Surface):
        self.__image = image

    @property
    def file(self):
        return self.__file
    @file.setter
    def file(self, file:str):
        self.__file = file

    @property
    def rect(self):
        return self.__rect
    @rect.setter
    def rect(self, rect:pygame.Rect):
        self.__rect = rect
    