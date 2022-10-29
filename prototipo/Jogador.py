from Jogo import Jogo
from Acao import Acao
from Personagem import Personagem
import random as r

class Jogador:
    def __init__(self, equipe: list):
        self.__equipe = equipe
    
    def jogar_dados(self):
        return r.randint(1, 20)
    
    def executar_acao(self, dado:int, acao: Acao):
        pass