from View.panel import Panel
import pygame

class Window(Panel):
    def __init__(self, width:int, height:int) -> None:
        self.__width = width
        self.__height = height
        self.__surface = None

        self.draw()
    
    def draw(self) -> None:
        self.__surface = pygame.display.set_mode((self.__width, self.__height), pygame.RESIZABLE)
    
    def updateSize(self, width, height) -> None:
        self.__width = width
        self.__height = height
        self.draw()
        pygame.display.update()
    
    def add(self, element, coordinates:tuple) -> None:
        self.__surface.blit(element, coordinates)







    @property
    def surface(self):
        return self.__surface
    @surface.setter
    def surface(self, surface):
        self.__surface = surface

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