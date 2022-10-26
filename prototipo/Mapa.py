from Jogo import Jogo
from Cenario import Cenario

class Mapa:
    def __init__(self, locais: list, caminhos:dict, posicao: Cenario):
        self.__locais = locais
        self.__posicao = posicao
        self.__caminhos = caminhos
    
    def viagem(self, destino: Cenario):
        pass