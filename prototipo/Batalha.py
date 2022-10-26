from Jogo import Jogo
from Cenario import Cenario
from Jogador import Jogador

class Batalha:
    def __init__(self, aliados:list, inimigos:list):
        self.__aliados = aliados
        self.__inimigos = inimigos