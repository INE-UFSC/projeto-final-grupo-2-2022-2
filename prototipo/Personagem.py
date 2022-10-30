from Jogo import Jogo
from Acao import Acao

class Personagem:
    def __init__(self, nome:str, ataque:int, saude:int,
                raca:str, amigo:bool, tecnicas:list):
        self.__nome = nome
        self.__raca = raca
        self.__amigo = amigo
        self.__saude_max = saude
        self.__ataque_max = ataque
        self.__saude_at = saude
        self.__ataque_at = ataque
        self.__tecnicas = tecnicas
    
    def e_amigo(self):
        return self.__amigo
    
    def get_saude(self):
        return self.__saude_at
    
    def set_saude(self, novo):
        self.__saude_at = novo
    
    def get_ataque(self):
        return self.__ataque_at
    
    def set_ataque(self, novo):
        self.__ataque_at = novo
    
    def get_nome(self):
        return self.__nome
    
    def get_raca(self):
        return self.__raca
    
    def receber_dano(self, dano):
        self.__saude_at -= abs(dano)
    
    def reduzir_ataque(self, dano):
        self.__ataque_at -= abs(dano)
    
    def boost_ataque(self, boost):
        self.__ataque_at += abs(boost)
    
    def boost_saude(self, boost):
        self.__saude_at += abs(boost)
    
    def fim_da_batalha(self):
        self.__saude_at = self.__saude_max
        self.__ataque_at = self.__ataque_max
    
    def aprender_tecnica(self, novo):
        self.__tecnicas.append(novo)
    
    def evoluir_tecnica(self, tecnica):
        if tecnica in self.__tecnicas:
            tecnica.evolucao()
        else: print("tecnica invalida")

    def evoluir_atributo(self, atributo: str):
        if atributo == 'ataque':
            self.__ataque += 5
        if atributo == 'saude':
            self.__saude += 5
    
    def executar_acao(self, dado:int, acao:str):
        pass