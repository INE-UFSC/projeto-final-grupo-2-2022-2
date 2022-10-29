from Jogo import Jogo
from Acao import Acao
from Item import Item

class Personagem:
    def __init__(self, nome:str, ataque:int, saude:int, raca:str,
                amigo:bool, equipamento:list, tecnicas:dict):
        self.__nome = nome
        self.__raca = raca
        self.__saude = saude
        self.__amigo = amigo
        self.__ataque = ataque
        self.__tecnicas = tecnicas
        self.__equipamento = equipamento
    
    def evoluir_tecnica(self, tecnica):
        self.__tecnicas[tecnica].evolucao()
    
    def evoluir_atributo(self, atributo: str):
        if atributo == 'ataque':
            self.__ataque += 5
        if atributo == 'saude':
            self.__saude += 5