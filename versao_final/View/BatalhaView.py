import pygame
from Model.Batalha import Batalha
from Model.Personagem import Personagem
from Controller.BatalhaController import BatalhaController

window = pygame.display.set_mode((900, 500), pygame.RESIZABLE)

class BatalhaView(Batalha):
    def __init__(self, aliados: list[Personagem],
                 inimigos: list[Personagem]):
        self.__aliados_view = [i.controller.view for i in aliados]
        self.__inimigos_view = [i.controller.view for i in inimigos]
        self.__allies = aliados
        self.__enemies = inimigos
        super().__init__(self.__allies, self.__enemies)

    def draw(self):
        self.__window.fill((255, 255, 255))
        for personagem in self.__aliados_view:
            personagem.draw()
        for personagem in self.__inimigos_view:
            personagem.draw()
        pygame.display.update()
    
    def start(self):
        pygame.init()
        self.__window = window # pygame.display.set_mode((900, 500), pygame.RESIZABLE)
        self.draw()

    
    def main(self):
        fps = 60
        clock = pygame.time.Clock()
        run = True
        finished = False
        
        while run:
            clock.tick(fps)
            for event in pygame.event.get():
                finished = BatalhaController.watch(super(),
                                                   event,
                                                   finished)
                if event.type == pygame.QUIT:
                    return False

            self.draw(self.__window)

