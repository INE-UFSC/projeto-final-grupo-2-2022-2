from Jogo import Jogo
from Acao import Acao
from personagem import Personagem
import random as r

class Jogador:
    def __init__(self, equipe:list(Personagem)):
        self.__equipe = equipe