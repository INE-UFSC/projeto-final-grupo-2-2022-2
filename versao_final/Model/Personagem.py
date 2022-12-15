from View.Sprite import Sprite
from Model.Habilidade import Habilidade
from Singleton.Animacao import Animacao
import pygame
import random as r

class Personagem:
    def __init__(self, 
                 classe:str, 
                 nivel:int, 
                 habilidades:list[Habilidade],
                 posicao: tuple[float]=(0, 0),
                 nome:str='Joao'):
        self.__nome = nome
        self.__nivel = nivel
        self.__saude = nivel*100
        self.__saude_max = nivel*100
        self.__ataque = nivel
        self.__classe = classe
        self.__sprite = Sprite(classe, posicao)
        self.__habilidades = habilidades
    
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

# expande as tecnicas

    def aprender_tecnica(self, novo):
        self.__habilidades.append(novo)

# resetam os status e evoluem depois da batalha

    def reset(self):
        self.__saude = self.__saude_max

    def fim_da_batalha(self, nivel:int):

        self.__nivel = nivel

        # var = r.choice(['ataque', 'saude'])
        # self.evoluir_atributo(var)

        print(self.__saude_max)
        print(self.__ataque)
        self.__saude = nivel*100
        self.__saude_max = nivel*100
        self.__ataque = nivel
        print(self.__saude_max)
        print(self.__ataque)

        var = r.choice(self.__habilidades)
        self.evoluir_tecnica(var)

    
    def evoluir_tecnica(self, tecnica:Habilidade):
        if tecnica in self.__habilidades:
            tecnica.evolucao()
        else: print("tecnica invalida")

    # def evoluir_atributo(self, atributo: str):
    #     if atributo == 'ataque':
    #         self.__ataque += 5
    #     if atributo == 'saude':
    #         self.__saude_max += 5
    #     else:
    #         print('argumento invalido')

    #     self.__saude_max += (100*self.__nivel/10)//1
    #     self.__ataque += (100*self.__nivel/10)//1

    @property
    def nome(self) -> str:
        return self.__nome
    @nome.setter
    def nome(self, novo:str):
        self.__nome = novo

    @property
    def nivel(self) -> int:
        return self.__nivel
    
    @property
    def saude(self):
        return self.__saude

    @property
    def sprite(self):
        return self.__sprite
    @sprite.setter
    def sprite(self, novo: Sprite):
        self.__sprite = novo

    @property
    def classe(self) -> str:
        return self.__classe
    @classe.setter
    def classe(self, novo:str):
        self.__classe = novo

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

    @property
    def ataque(self) -> int:
        return self.__ataque

    @property
    def saude_max(self) -> int:
        return self.__saude_max

# as proximas duas só podem
# ser acessadas pelo Save

    def save_ataque(self, novo:int, senha:str):
        if senha == 'ataque_autorizado':
            self.__ataque = novo

    def save_saude_max(self, novo:int, senha:str):
        if senha == 'vida_autorizada':
            self.__saude_max = novo
