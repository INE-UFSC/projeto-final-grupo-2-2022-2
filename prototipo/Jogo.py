from element import Element
from Batalha import Batalha
from Personagem import Personagem
import pygame
class Jogo:
    def __init__(self, time:list[Element], inimigos:list[Element], window:pygame.Surface) -> None:
        self.__time = time
        self.__inimigos = inimigos
        self.__player_turn = True
    
    def jogar(self):
        pass

    def watch(self, battle, event, finished):
        allies, enemies = [i.char for i in self.__time], [i.char for i in self.__inimigos]
        click = False

        if event.type == pygame.VIDEORESIZE:
            window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN and not click and not finished and self.__player_turn:
            finished = self.turn(battle, allies, enemies, self.__time, self.__inimigos)
        
        if event.type == pygame.MOUSEBUTTONUP:
            click = False

        if not self.__player_turn and not finished:
            finished = self.turn(battle, enemies, allies, self.__inimigos, self.__time)
        
        return finished
            
    def turn(self, 
            battle:Batalha, 
            attackers:list[Personagem], 
            targets:list[Personagem],
            original_attackers:list[Element],
            original_targets:list[Element]):
        finished = False
        if attackers and targets:
            targets, attackers = battle.turno(targets, attackers)
            if len(attackers) != len(original_attackers): self.remove_dead(attackers, original_attackers)
            if len(targets) != len(original_targets): self.remove_dead(targets, original_targets)

        finished = self.check_winner(attackers, targets)

        self.__player_turn = not self.__player_turn
        return finished
    

    def remove_dead(self, affected_team:list[Element], original_team:list[Element]):
        for i in original_team:
            if i.char not in affected_team:
                original_team.remove(i)
    
    def check_winner(self, team1, team2):
        finished = False
        if ((not team1 and team1 == self.__time) or
             not team2 and team2 == self.__time):
            print("enemies win")
            finished = True
        elif ((not team1 and team1 == self.__inimigos) or 
             (not team2 and team2 == self.__inimigos)):
            print("allies win")
            finished = True
        
        return finished

    