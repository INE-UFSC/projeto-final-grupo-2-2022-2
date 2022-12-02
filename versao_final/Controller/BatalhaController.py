from Model.Personagem import Personagem

import pygame
import random as r

class BatalhaController():
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


    # def watch(self, event):
    #     click = False  
        
    #     condicaoAliados = not click and self.__player_turn
    # and not self.__finished
    #     condicaoInimigos = not click and not self.__pl]yer_turn
    # and not self.__finished

    #     if event.type == pygame.MOUSEBUTTONDOWN and condicaoAliados:
    #         self.turno(self.__alliesPersonagens, self.__enemiesPersonagens)
    #         click = True

    #     if event.type == pygame.MOUSEBUTTONDOWN and condicaoInimigos:
    #         self.turno(self.__enemiesPersonagens, self.__alliesPersonagens)
    #         click = True
        
    #     if event.type == pygame.MOUSEBUTTONUP:
    #         click = False

    #     return self.__alliesPersonagens, self.__enemiesPersonagens

    
    def checkForWinner(self):
        cont = 0
        for i in self.__alliesPersonagens:
            if i.get_saude() >= 0:
                cont += 1
        if cont == 0:
            self.__finished = True
            self.__winner = 0
            return
        cont = 0
        for i in self.__enemiesPersonagens:
            if i.get_saude() >= 0:
                cont += 1
        if cont == 0:
            self.__finished = True
            self.__winner = 1
            return
    


    def turno(self, atacante: Personagem,
              alvos:list[Personagem]):

        habilidade = atacante.get_acao()
        
        troca = False
        if habilidade.tipo == 'suporte':
            executores, alvos = alvos, executores
            troca = True

        alvo = r.choice(alvos)
        multiplicador = r.randint(1, 20)
        habilidade.executar(alvo, multiplicador)

        self.__player_turn = not self.__player_turn
        self.checkForWinner()
