from Model.CenarioModel import CenarioModel
from Model.CenarioBatalha import CenarioBatalha
from Singleton.Constantes import Constantes
from DAO.PersonagemDAO import PersonagemDAO
import pygame
import os


class Mapa:
    def __init__(self,id_image:str, altura:int,
                 largura:int, eixo_x:int,
                 eixo_y:int):
        pygame.sprite.Sprite.__init__(self)
        self.__altura = altura
        self.__largura = largura
        self.__eixo_x = eixo_x
        self.__eixo_y = eixo_y
        self.__locais = self.__define_locais()
        self.__id_image = id_image
        self.__image = pygame.image.load(os.path.join('versao_final',
                                                      'assets',
                                                      f'{self.__id_image}')
                                         ).convert()
        self.__image = pygame.transform.scale(self.__image,
                                              (largura, altura))
        self.__rect = self.__image.get_rect()
        self.__rect.center = (eixo_x), (eixo_y)
        
        
    def __define_locais(self):
        locais = [None]*10
        const = Constantes().locais
        get_inimigos = PersonagemDAO()
        inimigos = [None]*3

        for i in range(10):
            b = const[0]
            m = const[1] + const[2] + const[3] + const[4]
            for j in range(3):
                nome = 'Inimigo' + str(i) + str(j)
                inimigos[j] = get_inimigos.get(nome)
            locais[i] = CenarioModel(CenarioBatalha(b[0], b[1], b[2],
                                                    b[3], b[4], i,
                                                    inimigos),
                                    m[0], m[1], m[2], m[3],)
        return locais

    @property
    def id_imagem(self) -> str:
        return self.__id_image

    @property
    def locais(self) -> list[CenarioModel]:
        return self.__locais

    def escolher_local(self, destino:int) -> CenarioModel:
        return self.__locais[destino]

    @property
    def imagem(self):
        return self.__image

    @property
    def rect(self):
        return self.__rect
