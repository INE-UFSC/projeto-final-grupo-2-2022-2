import os
import pygame

class Sprite(pygame.sprite.Sprite):

    def __init__(self, filename:str, width:float, height:float, x:float, y:float) -> None:
        super().__init__()
        self.__filename = filename
        self.__width = width
        self.__height = height
        self.image = self.setImage()
        self.coord = [x, y]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.position = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2()
        self.__defaultSize = (x, y)

    def draw(self, screen:pygame.Surface):
        screen.blit(self.image, self.rect)
        pygame.display.update()
    
    def move(self, atacantePosition: list[float], alvoPosition: list[float]):
        self.direction = (pygame.math.Vector2(alvoPosition) - atacantePosition).normalize()
        self.position += self.direction * 5
        self.rect.center = round(self.position.x), round(self.position.y)

        if self.rect.collidepoint(alvoPosition):
            return True
        return False

    def setImage(self):
        img = pygame.image.load(os.path.join('versao_final', 'assets', f'{self.__filename}.png'))
        image = pygame.transform.scale(img, (self.__width, self.__height))
        return image

    # def set_image(self, filename):
    #     filename += '.png'
    #     tempImage = pygame.image.load(os.path.join('versao_final/assets', filename))
    #     self.image = pygame.transform.scale(tempImage, (self.__width, self.__height))
    
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
