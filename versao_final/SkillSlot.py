import pygame
import os

class SkillSlot(pygame.sprite.Sprite):
    def __init__(self, posicao:tuple[int]) -> None:
        super().__init__()
        self.__width, self.__height = 50, 50

        self.__filename = 'retangulo'
        self.image = self.setImage()
        self.rect = self.image.get_rect()

        self.rect.center = posicao
    
    def setImage(self):
        img = pygame.image.load(os.path.join('assets', f'{self.__filename}.png'))
        image = pygame.transform.scale(img, (self.__width, self.__height))
        return image
    
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height