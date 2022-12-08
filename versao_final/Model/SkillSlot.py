from Model.Acao import Acao
from Singleton.Constantes import Constantes
import pygame
import os

class SkillSlot(pygame.sprite.Sprite):

    def __init__(self) -> None:
        super().__init__()
        self.__side = Constantes().screenSize[0] // 24
        self.__x = self.__side * (8 + Constantes().slotCounter)
        self.__y = Constantes().screenSize[1] - self.__side
        self.image = self.setImage('retangulo')
        self.__skill = None
        self.rect = pygame.Rect(self.__x, self.__y,
                                self.__side, self.__side)
    
    def setImage(self, filename:str):
        img = pygame.image.load(os.path.join('versao_final',
                                             'assets',
                                             f'{filename}.png'))
        image = pygame.transform.scale(img, (self.__side,
                                             self.__side))
        return image
    
    def setSkill(self, skill):
        self.__skill = skill
        self.__skill.sprite.rect.x = self.rect.x
        self.__skill.sprite.rect.y = self.rect.y
        self.__skill.sprite.width = self.__side 
        self.__skill.sprite.height = self.__side 

    @property
    def skill(self):
        return self.__skill
    @skill.setter
    def skill(self, skill:Acao):
        self.setSkill(skill)