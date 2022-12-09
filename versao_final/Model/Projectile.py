from Model.Sprite import Sprite
from Singleton.Singleton import Singleton
import pygame

class Projectile(Sprite):
    def __init__(self, filename: str) -> None:
        super().__init__(filename)
        self.__width = super().width
        self.__height = super().height 
    
    def draw(self, screen:pygame.Surface):
        screen.blit(self.image, self.rect)
        pygame.display.update()
    
    def setRectPosition(self):
        self.rect.x = super().width * (8 + Singleton().slotCounter)
        self.rect.y = Singleton().screenSize[1] - super().height