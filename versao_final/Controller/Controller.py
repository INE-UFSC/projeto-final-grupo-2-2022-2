from Model.Personagem import Personagem

import pygame
import random as r

class Controller():
    def __init__(self, time:list[Personagem],
                 inimigos:list[Personagem]) -> None:
        self.__alliesPersonagens = time
        self.__enemiesPersonagens = inimigos
        self.__player_turn = True
        self.__finished = False
        self.__winner = -1
    
    @property
    def finished(self) -> bool:
        return self.__finished
    @property
    def winner(self) -> int:
        return self.__winner

    def checkForWinner(self, 
                       aliados:list[Personagem], 
                       inimigos:list[Personagem]) -> int:
        cont = 0
        for i in self.__alliesPersonagens:
            if i.get_saude() >= 0:
                cont += 1
        if cont == 0:
            return 0
        cont = 0
        for i in self.__enemiesPersonagens:
            if i.get_saude() >= 0:
                cont += 1
        if cont == 0:
            return 1
        
        return -1
    


    def selecionaAlvoEHabilidade(self, atacante: Personagem,
              alvos:list[Personagem]):

        habilidade = atacante.get_acao()
        
        # Caso o alvo escolhido não tenha vida restante, tenta selecionar outro
        alvo = r.choice(alvos)
        while alvo.get_saude() <= 0:
            alvo = r.choice(alvos)

        # TODO: habilidades do tipo suporte
        if habilidade.tipo == 'suporte':
            pass

        return alvo, habilidade
