import pygame
from Model.Personagem import Personagem
from Controller.BatalhaController import BatalhaController
import os
class BatalhaView():
    def __init__(self, aliados: list[Personagem],
                 inimigos: list[Personagem]):
        self.__aliados_view = [i.controller.view for i in aliados]
        self.__inimigos_view = [i.controller.view for i in inimigos]
        self.__allies = aliados
        self.__enemies = inimigos
        self.__window = pygame.display.set_mode((900, 500), pygame.RESIZABLE)
        self.__controller = BatalhaController(aliados, inimigos)

        self.__skillSlots = [None]*7

        for i in range(7):
            self.__skillSlots[i] = pygame.transform.scale(
                pygame.image.load(
                    os.path.join('versao_final/assets', 'retangulo.png')),
                    (50, 50))

    def draw(self):
        self.__window.fill((255, 255, 255))
        for personagem in self.__aliados_view:
            personagem.draw()
        for personagem in self.__inimigos_view:
            personagem.draw()

        winw, winh = self.__window.get_size()
        
        cont = 7
        for elemento in self.__skillSlots:
            self.__window.blit(elemento, (winw/22*cont,
                                        winh-50))
            cont += 1

        pygame.display.update()
    
    def start(self):
        pygame.init()
        self.draw()

    
    def main(self):
        fps = 60
        clock = pygame.time.Clock()
        run = True
        
        while run:
            clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.VIDEORESIZE:
                    window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    pygame.display.update()

                self.__aliados_view, self.__inimigos_view = self.__controller.watch(event)

                if event.type == pygame.QUIT:
                    return False

            self.draw()

