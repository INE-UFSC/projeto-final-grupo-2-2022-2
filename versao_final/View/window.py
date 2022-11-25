from View.panel import Panel
import pygame

class Window(Panel):
    def __init__(self, width:int,
                 height:int) -> None:
        self.__width = width
        self.__height = height
        self.__surface = None

        self.draw()
    
    def draw(self) -> None:
        self.__surface = pygame.display.set_mode((self.__width,
                                                  self.__height),
                                                 pygame.RESIZABLE)
    
    def updateSize(self, width, height) -> None:
        self.__width = width
        self.__height = height
        self.draw()
        pygame.display.update()
    
    def add(self, element, coordinates:tuple) -> None:
        self.__surface.blit(element, coordinates)
    
    @property
    def surface(self) -> pygame.Surface:
        return self.__surface