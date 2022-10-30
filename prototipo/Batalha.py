from Jogo import Jogo
from Acao import Acao
from Cenario import Cenario
from Jogador import Jogador
from Personagem import Personagem
import random as r

class Batalha:
    def __init__(self, aliados:list, inimigos:list):
        self.__aliados = aliados
        self.__inimigos = inimigos

    def ataque(self, amigo:bool, efeito:str, dano:int):
        if amigo: oponente = self.__inimigos
        else: oponente = self.__aliados
        a = r.random.choice(oponente)
        if efeito.lower() == 'saude':
            a.receber_dano(dano)
        elif efeito.lower() == 'ataque':
            a.reduzir_ataque(dano)
        else: print('efeito invalido')

    def suporte(self, amigo:bool, efeito:str, boost:int):
        if amigo: oponente = self.__aliados
        else: oponente = self.__inimigos
        a = r.random.choice(oponente)
        if efeito.lower() == 'saude':
            a.boost_saude(boost)
        elif efeito.lower() == 'ataque': 
            a.boost_ataque(boost)
        else: print('efeito invalido')
    
    def jogar_dados(self):
        return r.randint(1, 20)
    
    def batalhar(self, ):
        pass