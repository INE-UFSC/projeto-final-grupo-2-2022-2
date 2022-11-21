from View.PersonagemView import PersonagemView
from Model.Batalha import Batalha
from Model.Personagem import Personagem
import pygame
class BatalhaController(Batalha):
    def __init__(self, time:list[PersonagemView],
                 inimigos:list[PersonagemView]) -> None:
        self.__time = time
        self.__inimigos = inimigos
        self.__allies = [i.char for i in self.__time]
        self.__enemies = [i.char for i in self.__inimigos]
        super().__init__(self.__allies, self.__enemies)
        self.__player_turn = True
    
    def jogar(self):
        pass

    def watch(self, event, finished):
        click = False
        if event.type == pygame.VIDEORESIZE:
            window = pygame.display.set_mode((event.w, event.h),
                                             pygame.RESIZABLE)
            pygame.display.update()
        
        var = not click and not finished and self.__player_turn
        if event.type == pygame.MOUSEBUTTONDOWN and var:
            finished = self.batalhar(self.__time, self.__inimigos)
        
        if event.type == pygame.MOUSEBUTTONUP:
            click = False

        if not self.__player_turn and not finished:
            finished = self.batalhar(self.__inimigos, self.__time)
        
        return finished
            
    def batalhar(self, original_attackers:list[PersonagemView],
            original_targets:list[PersonagemView]):

        attackers = [i.char for i in original_attackers]
        targets = [i.char for i in original_targets]
        finished = False
        if attackers and targets:
            targets, attackers = super().turno(targets, attackers)
            if len(attackers) != len(original_attackers):
                self.remove_dead(attackers, original_attackers)
            if len(targets) != len(original_targets):
                self.remove_dead(targets, original_targets)

        finished = self.check_winner(attackers, targets)

        self.__player_turn = not self.__player_turn
        return finished
    

    def remove_dead(self, affected_team:list[PersonagemView],
                    original_team:list[PersonagemView]):
        for i in original_team:
            if i.char not in affected_team:
                original_team.remove(i)
    
    def check_winner(self, team1, team2):
        vencedor:str = ''
        finished = False
        if ((not team1 and team1 == self.__time) or
             not team2 and team2 == self.__time):
            print("enemies win")
            finished = True
        elif ((not team1 and team1 == self.__inimigos) or 
             (not team2 and team2 == self.__inimigos)):
            print("allies win")
            for i in self.__allies:
                i.fim_da_batalha()
            finished = True
        
        return finished

    