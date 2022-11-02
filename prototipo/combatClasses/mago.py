from personagem import Personagem
import pygame
import os

class Mago(Personagem):
    def __init__(self, nome:str, ataque:float, saude:float, tecnicas:list) -> None:
        self.__size = (70, 80)
        self.__image = None
        self.set_image()
        super().__init__(nome, ataque, saude, tecnicas, self.__image, self.__size)
    
    def set_image(self):
        tempImage = pygame.image.load(os.path.join('prototipo/assets', 'mago.png'))
        self.__image = pygame.transform.scale(tempImage, (self.__size[0], self.__size[1]))
    
    @property
    def image(self):
        return self.__image