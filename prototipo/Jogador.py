from Jogo import Jogo
from Acao import Acao
from Item import Item
from Personagem import Personagem
import random as r

class Jogador:
    def __init__(self, equipe: list):
        self.__equipe = equipe
    
    def jogar_dados(self): -> int
        return r.randint(1, 20)
    
    def executar_acao(self, dado:int, acao: Acao): -> Acao
        pass
    
    def usar_item(self, dado:int, item: Item): -> Item
        pass