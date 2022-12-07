import random as r
from Model.Sprite import Sprite
from Singleton.Singleton import Singleton
from time import sleep
from Model.Acao import Acao
import pygame
# from Controller.PersonagemController import PersonagemController

class Personagem:
    def __init__(self, nome:str, nivel:int,
                 tecnicas:list[Acao], classe:str):
        self.__nome = nome
        self.__saude_max = (100 + 10*nivel)/1
        self.__ataque_max = (100 + 10*nivel)/1
        self.__saude_at = (100 + 10*nivel)/1
        self.__ataque_at = (100 + 10*nivel)/1
        self.__tecnicas = tecnicas
        self.__classe = classe
        self.__sprite = Sprite(classe)
        self.__batalhas = []
    
    def animacao(self, index:int):
        modificador = 2 if self.__sprite.rect.x < Singleton().screenSize[0]/2 else -2
        if index == 0:
            for i in range (10):
                self.__sprite.rect.x += modificador
                self.__sprite.draw()
        else:
            self.__sprite.rect.x += 4
            self.__sprite.rect.y += 4
            self.__sprite.draw()
            self.__sprite.rect.x -= 4
            self.__sprite.rect.y -= 4
            self.__sprite.draw()

            sleep(0.5)
            self.__sprite.rect.x = self.__sprite.defaultSize[0]
    
    def getHabilidades(self) -> list[Sprite]:
        listaAcoes = []
        for acao in self.__tecnicas:
            listaAcoes.append(acao.sprite)
        return listaAcoes
            
    
    def desenhaBarraDeVida(self, screen:pygame.Surface):
        x = self.sprite.rect.centerx
        y = self.sprite.rect.centery - 50
        w = 60
        h = 15

        saude = self.__saude_at
        if self.__saude_at > 0:
            outerRect = pygame.Rect(x, y, w, h)
            outerRect.center = (x, y)
            pygame.draw.rect(screen, (0, 0, 0), outerRect, 1)
            progresso = saude / self.__saude_max

            innerPosition = (outerRect.x+3, outerRect.y+3)
            innerSize = ((w-6)*progresso, h-6)

            innerRect = pygame.Rect(*innerPosition, *innerSize)

            pygame.draw.rect(screen, (0, 255, 0), innerRect)
        pass

    @property
    def nome(self) -> str:
        return self.__nome
    @nome.setter
    def nome(self, novo:str):
        self.__nome = novo
        
    @property
    def sprite(self) -> Sprite:
        return self.__sprite
    @sprite.setter
    def sprite(self, novo:str):
        self.__sprite = novo

    @property
    def tecnicas(self) -> list:
        return self.__tecnicas
    @tecnicas.setter
    def tecnicas(self, novo:str):
        self.__tecnicas = novo

    @property
    def classe(self) -> str:
        return self.__classe
    @classe.setter
    def classe(self, novo:str):
        self.__classe = novo

    @property
    def batalhas(self) -> list:
        return self.__batalhas
    @batalhas.setter
    def batalhas(self, novo):
        print('Não envie parâmetros!!!')
    
    @property
    def saude_max(self) -> int:
        return self.__saude_max

# retornam a saude e o ataque atual, em batalha

    def get_saude(self) -> int:
        return self.__saude_at
    
    def get_ataque(self) -> int:
        return self.__ataque_at

# escolhe uma tecnica 

    def get_acao(self, num=0):
        if len(self.__tecnicas) > num:
            return self.__tecnicas[num]
        return None

# recebem o efeito ofensivo ou de suporte

    def afeta_saude(self, efeito:int):
        self.__saude_at += efeito
    
    def afeta_ataque(self, efeito:int):
        self.__ataque_at += efeito

# expande as tecnicas

    def aprender_tecnica(self, novo):
        self.__tecnicas.append(novo)

# resetam os status e evoluem depois da batalha

    def fim_da_batalha(self, id_battle: int):
        self.__batalhas.append(id_battle)

        var = r.choice(['ataque', 'saude'])
        self.evoluir_atributo(var)

        self.__saude_at = self.__saude_max
        self.__ataque_at = self.__ataque_max

        var = r.choice(self.__tecnicas)
        self.evoluir_tecnica(var)

    
    def evoluir_tecnica(self, tecnica):
        if tecnica in self.__tecnicas:
            tecnica.evolucao()
        else: print("tecnica invalida")

    def evoluir_atributo(self, atributo: str):
        if atributo == 'ataque':
            self.__ataque_max += 5
        if atributo == 'saude':
            self.__saude_max += 5