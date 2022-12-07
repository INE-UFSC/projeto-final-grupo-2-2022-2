from Model.Sprite import Sprite
from Singleton.Singleton import Singleton
from Model.Acao import Acao

class SkillSlot(Sprite):

    def __init__(self) -> None:
        super().__init__('retangulo')
        self.__width = Singleton().screenSize[0]/24
        self.__height = Singleton().screenSize[0]/24
        print(self.__width)
        self.rect.x = self.__width * (8 + Singleton().slotCounter)
        self.rect.y = Singleton().screenSize[1] - self.__height
        self.__skill = None
    
    @property
    def skill(self):
        return self.__skill
    @skill.setter
    def skill(self, skill:Acao):
        self.__skill = skill
