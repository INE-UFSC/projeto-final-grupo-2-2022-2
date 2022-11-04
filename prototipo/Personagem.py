from Acao import Acao
import random as r

from pygame import Surface

class Personagem:
    def __init__(self, nome:str, ataque:int,  saude:int,
                 tecnicas:list, image:Surface, size:tuple):
        self.__nome = nome
        self.__saude_max = saude
        self.__ataque_max = ataque
        self.__saude_at = saude
        self.__ataque_at = ataque
        self.__tecnicas = tecnicas
        self.__image = image
        self.__size = size

    @property
    def image(self):
        return self.__image
    @image.setter
    def image(self, image) -> None:
        self.__image = image

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, size) -> None:
        self.__size = size
    
    def get_nome(self):
        return self.__nome

# retornam a saude e o ataque atual, em batalha

    def get_saude(self):
        return self.__saude_at
    
    def get_ataque(self):
        return self.__ataque_at

# escolhe uma teçnica aleatoria

    def get_acao(self) -> Acao:
        return r.choice(self.__tecnicas)

# recebem o efeito ofensivo ou de suporte

    def afeta_saude(self, efeito):
        self.__saude_at += efeito
    
    def afeta_ataque(self, efeito):
        self.__ataque_at += efeito

# resetam os status depois da batalha

    def fim_da_batalha(self):
        self.__saude_at = self.__saude_max
        self.__ataque_at = self.__ataque_max

    def aprender_tecnica(self, novo: Acao):
        self.__tecnicas.append(novo)
    
    def evoluir_tecnica(self, tecnica: Acao):
        if tecnica in self.__tecnicas:
            tecnica.evolucao()
        else: print("tecnica invalida")

    def evoluir_atributo(self, atributo: str):
        if atributo == 'ataque':
            self.__ataque += 5
        if atributo == 'saude':
            self.__saude += 5