from Acao import Acao
import random as r
import os
import pygame

class Personagem:
    def __init__(self, nome:str, ataque:int,  saude:int,
                 tecnicas:list, classe:str='mago.png',
                 size:tuple=(70, 80)):
        self.__nome = nome
        self.__saude_max = saude
        self.__ataque_max = ataque
        self.__saude_at = saude
        self.__ataque_at = ataque
        self.__tecnicas = tecnicas
        self.__image = self.set_image(classe)
        self.__size = size

    @property
    def image(self):
        return self.__image
    @image.setter
    def image(self, image) -> None:
        self.__image = image

    def set_image(self, origem:str='mago.png'):
        tempImage = pygame.image.load(os.path.join('assets',
                                                   origem))
        return pygame.transform.scale(tempImage,
                                      (self.__size[0],
                                       self.__size[1]))

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

# escolhe uma tecnica 

    def get_acao(self, num:int=0) -> Acao:
        return self.__tecnicas[num]

# recebem o efeito ofensivo ou de suporte

    def afeta_saude(self, efeito):
        self.__saude_at += efeito
    
    def afeta_ataque(self, efeito):
        self.__ataque_at += efeito

# expande as tecnicas

    def aprender_tecnica(self, novo: Acao):
        self.__tecnicas.append(novo)

# resetam os status e evoluem depois da batalha

    def fim_da_batalha(self):
        var = r.choice(['ataque', 'saude'])
        self.evoluir_atributo(var)

        self.__saude_at = self.__saude_max
        self.__ataque_at = self.__ataque_max

        var = r.choice(self.__tecnicas)
        self.evoluir_tecnica(var)
    
    def evoluir_tecnica(self, tecnica: Acao):
        if tecnica in self.__tecnicas:
            tecnica.evolucao()
        else: print("tecnica invalida")

    def evoluir_atributo(self, atributo: str):
        if atributo == 'ataque':
            self.__ataque_max += 5
        if atributo == 'saude':
            self.__saude_max += 5