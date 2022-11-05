from abc import ABC, abstractmethod
import pygame

class Panel(ABC):
    def __init__(self, width, height, pos_x, pos_y) -> None:
        self.__width = width
        self.__height = height
        self.__pos_x = pos_x
        self.__pos_y = pos_y
    
    @abstractmethod
    def draw():
        pass
    

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, height):
        self.__height = height
    
    @property
    def pos_x(self):
        return self.__pos_x
    @pos_x.setter
    def pos_x(self, pos_x):
        self.__pos_x = pos_x

    @property
    def pos_y(self):
        return self.__pos_y
    @pos_y.setter
    def pos_y(self, pos_y):
        self.__pos_y = pos_y