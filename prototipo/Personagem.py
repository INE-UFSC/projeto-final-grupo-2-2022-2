from Jogo import Jogo
from Acao import Acao
from Item import Item

class Personagem:
    def __init__(self, nome:str, ataque:int, pontos_de_vida:int, amigo:bool,
                defesa:int, equipamento:list, tecnicas:dict, raca:str):
        self.__nome = nome
        self.__raca = raca
        self.__amigo = amigo
        self.__ataque = ataque
        self.__defesa = defesa
        self.__tecnicas = tecnicas
        self.__equipamento = equipamento
        self.__pontos_de_vida = pontos_de_vida
    
    def executar_acao(self, dado:int, acao: Acao): -> Acao
        pass
    
    def evoluir_tecnica(self):
        pass
    
    def evoluir_atributo(self):
        pass