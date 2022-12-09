from Sprite import Sprite
from Habilidade import Habilidade
from Animacao import Animacao
import pygame

class Personagem:
    def __init__(self, 
                 classe:str, 
                 nivel:int, 
                 habilidades:list[Habilidade],
                 posicao: tuple[float]=(0, 0)) -> None:
        self.__saude = nivel*100
        self.__saude_max = nivel*100
        self.__ataque = nivel
        self.__sprite = Sprite(classe, posicao)
        self.__habilidades = habilidades
        self.__saude = 100
    
    def atacar(self, index: int, posicaoAlvo: list[float]):
        self.__sprite.moveAtacante()
        if Animacao().fase == 1:
            dano = self.__habilidades[index].executar(posicaoAlvo)
            dano *= self.__ataque
            return dano
        else:
            return 0
    
    def defender(self, dano: float):
        self.__sprite.moveAlvo()
        self.__saude -= dano
    
    def criaBarraDeVida(self, screen:pygame.Surface):
        x = self.__sprite.rect.centerx
        y = self.__sprite.rect.centery - 50
        w = 60
        h = 15

        saude = self.__saude
        if saude > 0:
            outerRect = pygame.Rect(x, y, w, h)
            outerRect.center = (x, y)
            pygame.draw.rect(screen, (0, 0, 0), outerRect, 1)
            progresso = saude / self.__saude_max

            innerPosition = (outerRect.x+3, outerRect.y+3)
            innerSize = ((w-6)*progresso, h-6)

            innerRect = pygame.Rect(*innerPosition, *innerSize)

            pygame.draw.rect(screen, (0, 255, 0), innerRect)
        else:
            self.__sprite.kill()

    
    @property
    def saude(self):
        return self.__saude

    @property
    def sprite(self):
        return self.__sprite

    @property
    def habilidades(self):
        return self.__habilidades
    
    @property
    def posicao(self):
        return self.sprite.posicao
    @posicao.setter
    def posicao(self, new):
        self.__sprite.posicao = new
        for habilidade in self.__habilidades:
            habilidade.projetil.rectCenter = new