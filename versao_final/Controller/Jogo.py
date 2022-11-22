from Model.Personagem import Personagem
from Model.Batalha import Batalha
import os
from Controller.BatalhaController import time, inimigos, jogo, view
from Controller.PersonagemController import PersonagemController
from View.PersonagemView import PersonagemView
import pygame

class Jogo:
    def __init__(self):
        pygame.init()
        self.__window = pygame.display.set_mode((900, 500),
                                              pygame.RESIZABLE)
        self.__winw, self.__winh = self.__window.get_size()

        # Elementos a serem mostrados na tela
            
        self.__resultado = []

        self.__elements = ['']*7
        for i in range(7):
            self.__elements[i] = pygame.transform.scale(pygame.image.load(
                                                      os.path.join('versao_final/assets',
                                                      'retangulo.png')),
                                                      (50, 50))

    def update_window(self):
        self.__window.fill((255, 255, 255))
        for PersonagemView in time:
            PersonagemView.draw()
        for PersonagemView in inimigos:
            PersonagemView.draw()
        cont = 7
        for elemento in self.__elements:
            self.__window.blit(elemento, (self.__winw/22*cont,
                                        self.__winh-50))
            cont += 1
        for i in self.__resultado:
            self.__window.blit(i, (self.__winw/4, self.__winh/4))
        pygame.display.update()
        

    def main(self):
        fps = 60
        clock = pygame.time.Clock()


        run = True
        finished = False
        while run:
            clock.tick(fps)
            for event in pygame.event.get():
                finished = self.__jogo.watch(event, finished)
                if event.type == pygame.QUIT:
                    return False
                if finished:
                    result = pygame.transform.scale(
                        pygame.image.load(os.path.join('assets',
                                                       f'allies.png')),
                        (self.__winw/2, self.__winh/2))
                    self.__resultado.append(result)

            self.update_window()
