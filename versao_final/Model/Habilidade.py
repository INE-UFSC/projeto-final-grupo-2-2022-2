from View.Projetil import Projetil
from Singleton.Animacao import Animacao
import random as rand

class Habilidade:
    def __init__(self, 
                nome: str, 
                fator: int, 
                efeito: str, 
                tipo: str) -> None:
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
    
    @property
    def projetil(self):
        return self.__projetil
    @property
    def nome(self):
        return self.__nome
