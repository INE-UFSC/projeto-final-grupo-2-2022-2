from Model.Acao import Acao
from Singleton.Singleton import Singleton
import pygame
import os

class SkillSlot(pygame.sprite.Sprite):

    def __init__(self) -> None:
        super().__init__()
        self.__side = Singleton().screenSize[0] // 24
        self.__x = self.__side * (8 + Singleton().slotCounter)
        self.__y = Singleton().screenSize[1] - self.__side
        self.image = self.setImage('retangulo')
        self.__skill = None
        self.rect = pygame.Rect(self.__x, self.__y, self.__side, self.__side)
    
    def setImage(self, filename:str):
        img = pygame.image.load(os.path.join('versao_final', 'assets', f'{filename}.png'))
        image = pygame.transform.scale(img, (self.__side, self.__side))
        return image
    
    def setSkill(self, skill):
        self.__skill = skill
        self.__skill.rect.x = self.rect.x + 4
        self.__skill.rect.y = self.rect.y + 4
        self.__skill.width = self.__side - 4
        self.__skill.height = self.__side - 4
        self.__skill.update()

    @property
    def skill(self):
        return self.__skill
    @skill.setter
    def skill(self, skill:Acao):
        self.setSkill(skill)
