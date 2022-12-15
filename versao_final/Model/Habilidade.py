from View.Projetil import Projetil
from Singleton.Animacao import Animacao
import random as rand

class Habilidade:
    def __init__(self, 
                nome: str, 
                fator: int, 
                efeito: str, 
                tipo: str):
        self.__nome = nome
        self.__fator = fator
        self.__efeito = efeito
        self.__tipo = tipo
        
        self.__projetil = Projetil(nome)

    def executar(self, posicao: list[float]):
        self.__projetil.move(posicao)
        if Animacao().fase == 2:
            return self.calculaDano()
        else:
            return 0

    def calculaDano(self) -> float:
        multiplicador = rand.randint(1, 20)
        return self.__fator * multiplicador

    def evolucao(self):
        if self.__fator > 0:
            self.__fator += 5
        else:
            self.__fator -= 5
    
    @property
    def projetil(self) -> Projetil:
        return self.__projetil

    @property
    def nome(self):
        return self.__nome

    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self, novo:str):
        self.__tipo = novo


    @property
    def fator(self):
        return self.__fator    
    @fator.setter
    def fator(self, novo:int):
        self.__fator = novo


    @property
    def efeito(self):
        return self.__efeito
    @efeito.setter
    def efeito(self, novo:str):
        self.__efeito = novo
