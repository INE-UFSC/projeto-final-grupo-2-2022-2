from Jogo import Jogo
from Acao import Acao
from Personagem import Personagem
import random as r

class Jogador:
    def __init__(self, equipe: list):
        self.__equipe = equipe