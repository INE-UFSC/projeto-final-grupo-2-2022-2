import random as r
import pygame
from Model.Sprite import Sprite
from Model.Acao import Acao
from Singleton.Animacao import Animacao

class Personagem:
    def __init__(self, nome:str, nivel:int,
                 tecnicas:list, classe:str):
        self.__nome = nome
        self.__nivel = nivel
        self.__saude_max = 100 + 10*nivel
        self.__ataque_max = 100 + 10*nivel
        self.__saude_at = self.__saude_max
        self.__ataque_at = self.__ataque_max
        self.__tecnicas = tecnicas
        self.__classe = classe
        self.__sprite = Sprite(classe)
        self.__batalhas = [0]            
    
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
        else:
            self.__sprite.kill()
        pass

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

    @property
    def nome(self) -> str:
        return self.__nome
    @nome.setter
    def nome(self, novo:str):
        self.__nome = novo

    @property
    def nivel(self) -> int:
        return self.__nivel
    @nivel.setter
    def nivel(self, novo:str):
        self.__nivel = novo

    @property
    def sprite(self) -> Sprite:
        return self.__sprite
    @sprite.setter
    def sprite(self, novo:Sprite):
        self.__sprite = novo

    @property
    def ataque_max(self) -> int:
        return self.__ataque_max

    @property
    def saude_max(self) -> int:
        return self.__saude_max

# as proximas duas só podem
# ser acessadas pelo Save

    def save_ataque_max(self, novo:int, senha):
        if senha == 'pode usar':
            self.__ataque_max = novo

    def save_saude_max(self, novo:int, senha):
        if senha == 'pode usar':
            self.__saude_max = novo

    @property
    def tecnicas(self) -> list[Acao]:
        return self.__tecnicas

    @property
    def classe(self) -> str:
        return self.__classe
    @classe.setter
    def classe(self, novo:str):
        self.__classe = novo
        self.sprite = Sprite(novo)

    @property
    def batalhas(self) -> list:
        return self.__batalhas
    @batalhas.setter
    def batalhas(self, novo):
        print('Não envie parâmetros!!!')

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

    def fim_da_batalha(self, nivel:int):
        self.__nivel = nivel
        self.__batalhas.append(self.__nivel)

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
        else:
            print('argumento invalido')

        self.__saude_max += (100*self.__nivel/10)//1
        self.__ataque_max += (100*self.__nivel/10)//1
        
