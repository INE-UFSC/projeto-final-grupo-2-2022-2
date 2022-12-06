import pygame
import os
from abc import ABC,abstractmethod
class Cenario(ABC):
    def __init__(self, identificador:str, largura:int, altura:int,eixo_x:int, eixo_y:int):
        self.__id = identificador
        self.__identificador = identificador
        temp = os.getcwd().split(os.path.sep)
        temp.remove("View")
        temp = os.path.sep.join(temp)
        self.__caminho = os.path.join(temp,"assets")
        self.__image = pygame.image.load(os.path.join(self.__caminho,f'{identificador}')).convert()
        self.__image = pygame.transform.scale(self.__image,(largura, altura))
        self.__rect = self.imagem.get_rect()
        self.__rect.center = (eixo_x), (eixo_y)

    @property
    def imagem(self):
        return self.__image

    @property
    def rect(self):
        return self.__rect

    @property
    def cenario(self):
        return self.__lugar

class CenarioBatalha(Cenario):
    def __init__(self,identificador:str, largura:int, altura:int,eixo_x:int, eixo_y:int,inimigos):
        super().__init__(identificador,largura,altura,eixo_x,eixo_y)
        self.__inimigos = inimigos

    @property
    def inimigos(self):
        return self.__inimigos

#esta aqui apenas para indicar que vai existir essa classe, mas no momento, nao tem nada implementado

class CenarioLoja(Cenario):
    def __init__(self,identificador:str, largura:int, altura:int,eixo_x:int, eixo_y:int,itens: dict):
        super().__init__(identificador,largura,altura,eixo_x,eixo_y)
        self.__itens = itens
    @property
    def itens(self):
        return self.__itens

    def compra_item(self,item_pego):
        return self.__itens.pop(item_pego)

    def get_item(self,item_pego):
        return self.__itens[item_pego]



