from Model.Cenario import Cenario
from Model.Personagem import Personagem
import pygame, os

class CenarioBatalha(Cenario):
    def __init__(self,
                 filename:str, 
                 largura:int,
                 altura:int, 
                 eixo_x:int, 
                 eixo_y:int,
                 nivel:int,
                 inimigos):
        super().__init__(filename, largura,
                         altura, eixo_x, eixo_y)

        self.__background = self.setBackground(filename)
        self.__inimigos = inimigos
    
    def setBackground(self, filename):
        image = pygame.image.load(os.path.join('assets', filename))
        return image

    @property
    def inimigos(self) -> list[Personagem]:
        return self.__inimigos
