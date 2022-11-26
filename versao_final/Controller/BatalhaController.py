from Model.Personagem import Personagem

import pygame
import random as r

class BatalhaController():
    def __init__(self, time:list[Personagem],
                 inimigos:list[Personagem]) -> None:
        self.__alliesPersonagens = time
        self.__enemiesPersonagens = inimigos
        # self.__alliesView = [i.controller.view for i in self.__alliesPersonagens]
        # self.__enemiesView = [i.controller.view for i in self.__enemiesPersonagens]
        self.__player_turn = True
        self.__finished = False
        self.__winner = -1
    
    @property
    def finished(self) -> bool:
        return self.__finished
    @property
    def winner(self) -> int:
        return self.__winner

    # def updateViews(self):
    #     self.__alliesView = [i.controller.view for i in self.__alliesPersonagens]
    #     self.__enemiesView = [i.controller.view for i in self.__enemiesPersonagens]


    def watch(self, event):
        click = False  
        
        condicaoAliados = not click and self.__player_turn and not self.__finished
        condicaoInimigos = not click and not self.__player_turn and not self.__finished

        if event.type == pygame.MOUSEBUTTONDOWN and condicaoAliados:
            self.turno(self.__alliesPersonagens, self.__enemiesPersonagens)
            click = True

        if event.type == pygame.MOUSEBUTTONDOWN and condicaoInimigos:
            self.turno(self.__enemiesPersonagens, self.__alliesPersonagens)
            click = True
        
        if event.type == pygame.MOUSEBUTTONUP:
            click = False

        return self.__alliesPersonagens, self.__enemiesPersonagens

    
    def checkForWinner(self):
        cont = 0
        for i in self.__alliesPersonagens:
            if i.get_saude() >= 0:
                cont += 1
        if cont == 0:
            self.__finished = True
            return
        cont = 0
        for i in self.__enemiesPersonagens:
            if i.get_saude() >= 0:
                cont += 1
        if cont == 0:
            self.__finished = True
            return
    


    def turno(self, executores:list[Personagem],
                    alvos:list[Personagem]):

        atacante = r.choice(executores)
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



    # def batalhar(self):
    #     pass
    #     attackers = [i.char for i in self.__alliesPersonagens]
    #     targets = [i.char for i in original_targets]
    #     finished = False
    #     if attackers and targets:
    #         targets, attackers = super().turno(targets, attackers)
    #         if len(attackers) != len(self.__alliesPersonagens):
    #             self.remove_dead(attackers, self.__alliesPersonagens)
    #         if len(targets) != len(original_targets):
    #             self.remove_dead(targets, original_targets)

    #     finished = self.check_winner(attackers, targets)

    #     self.__player_turn = not self.__player_turn
    #     return finished
    

    # def remove_dead(self, affected_team:list[PersonagemView],
    #                 original_team:list[PersonagemView]):
    #     for i in original_team:
    #         if i.char not in affected_team:
    #             original_team.remove(i)
    
    # def check_winner(self, team1, team2):
    #     finished = False
    #     if ((not team1 and team1 == self.__alliesView) or
    #          not team2 and team2 == self.__alliesView):
    #         print("enemies win")
    #         finished = True
    #     elif ((not team1 and team1 == self.__enemiesView) or 
    #          (not team2 and team2 == self.__enemiesView)):
    #         print("allies win")
    #         for i in self.__alliesPersonagens:
    #             i.fim_da_batalha()
    #         finished = True
        
    #     return finished
    


# save = JogoDAO('Personagem')

# acoes = [
#         Acao('fireball', -5, 'saude', 'ofensivo'),
#         Acao('boost', 5, 'ataque', 'suporte')
#         ]

# magos = ['']*3
# orcs = ['']*3
# time = ['']*3
# inimigos = ['']*3
# for i in range(3):
#     inimigos[i] = PersonagemView(window,
#                                     600, 100 + i*100,
#                                     70, 80)
#     orcs[i] = Personagem('Mateus' + str(i), 10,
#                                 100, acoes, 'orc',
#                                 PersonagemController(inimigos[i]) )
#     time[i] = PersonagemView(window,
#                                     200, 100 + i*100,
#                                     70, 80)
#     magos[i] = Personagem('Joao' + str(i), 10,
#                                 100, acoes, 'mago',
#                                 PersonagemController(time[i]))
#     save.add(magos[i])
# view = BatalhaView(magos, orcs)
# jogo = BatalhaController(magos, orcs)