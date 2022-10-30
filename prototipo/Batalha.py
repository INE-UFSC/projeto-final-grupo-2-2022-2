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

    def ataque(self, amigo:bool, dano:int):
        if amigo: oponente = self.__inimigos
        else: oponente = self.__aliados
        a = r.random.choice(oponente)
        a.receber_dano(dano)


    def suporte(self, amigo:bool, efeito:str, boost:int):
        if amigo: oponente = self.__aliados
        else: oponente = self.__inimigos
        if efeito.lower() == 'saude':
            a = r.random.choice(oponente)
            a.boost_saude(boost)
        elif efeito.lower() == 'ataque': 
            a = r.random.choice(oponente)
            a.boost_ataque(boost)
        else: print('efeito invalido')