from Jogo import Jogo
from Personagem import Personagem
import random as r

class Jogador:
    def __init__(self, equipe: list):
        self.__equipe = equipe
    
    def jogar_dados(self): -> int
        return r.randint(1, 20)