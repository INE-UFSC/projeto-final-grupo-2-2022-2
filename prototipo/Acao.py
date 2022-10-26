from Jogo import Jogo

class Acao:
    def __init__(self, nome:str, efeito:list, 
                condicoes:list, niveis:list):
        self.__nome = nome
        self.__efeito = efeito
        self.__niveis = niveis
        self.__condicoes = condicoes
    def evolucao(self, novo_efeito):
        pass