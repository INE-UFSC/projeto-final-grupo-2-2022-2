import pygame
from Model.Batalha import Batalha
from PersonagemView import PersonagemView
from Controller.BatalhaController import BatalhaController

class BatalhaView(Batalha):
    def __init__(self, aliados: list[PersonagemView],
                 inimigos: list[PersonagemView]):
        self.__aliados_view = aliados
        self.__inimigos_view = inimigos
        self.__allies = [i.char for i in aliados]
        self.__enemies = [i.char for i in inimigos]
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
        self.__window = pygame.display.set_mode((900, 500), pygame.RESIZABLE)
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
