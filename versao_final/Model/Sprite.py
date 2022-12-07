import os
import pygame
from Singleton.Singleton import Singleton
from math import floor, ceil
class Sprite(pygame.sprite.Sprite):

    def __init__(self, filename:str) -> None:
        super().__init__()
        self.__filename = filename
        self.__width = Singleton().screenSize[0] / 15
        self.__height = Singleton().screenSize[0] / 15
        self.image = self.setImage()
        self.rect = self.image.get_rect()
        self.setRectPosition()
        self.__coord = [self.rect.x, self.rect.y]
        self.__position = pygame.math.Vector2(self.rect.center)
        self.__direction = pygame.math.Vector2()
        self.__defaultSize = (self.rect.x, self.rect.y)

    def setRectPosition(self):
        screenSize = Singleton().screenSize
        counter = Singleton().charCounter
        move = 0

        if counter == 2: move = - screenSize[0] // 10
        elif counter == 3: move = screenSize[0] // 10
        else: move = 0

        if counter % 2 == 0:
            self.rect.x = screenSize[0]//5 + move
        else:
            self.rect.x = screenSize[0] - self.__width - screenSize[0]//5 + move
        
        self.rect.y = screenSize[1]//5 * ceil((counter+1)/2)

    def update(self):
        self.__width = Singleton().screenSize[0] / 15
        self.__height = Singleton().screenSize[0] / 15

    def draw(self, screen:pygame.Surface):
        self.update()
        rect = pygame.Rect(*self.__coord, self.__width, self.__height)
        pygame.draw.rect(screen, (255, 255, 255), rect)

        screen.blit(self.image, self.rect)
        pygame.display.update()
    
    def move(self, 
             atacantePosition: list[float], 
             alvoPosition: list[float],
             alvoRect: pygame.Rect):
        self.position = atacantePosition
        self.direction = (pygame.math.Vector2(alvoPosition) - atacantePosition).normalize()
        self.position += self.direction * 5
        self.rect.center = round(self.position.x), round(self.position.y)
        
        if self.rect.colliderect(alvoRect):
            return True
        return False

    def setImage(self):
        img = pygame.image.load(os.path.join('versao_final', 'assets', f'{self.__filename}.png'))
        image = pygame.transform.scale(img, (self.__width, self.__height))
        return image
    
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

    @property
    def defaultSize(self):
        return self.__defaultSize
    @defaultSize.setter
    def defaultSize(self, defaultSize:int):
        self.__defaultSize = defaultSize

    @property
    def coord(self):
        return self.__coord
    @coord.setter
    def coord(self, coord:int):
        self.__coord = coord

    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, position:int):
        self.__position = position

    @property
    def direction(self):
        return self.__direction
    @direction.setter
    def direction(self, direction:int):
        self.__direction = direction
