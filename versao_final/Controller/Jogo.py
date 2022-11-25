from Model.Personagem import Personagem
import os
from Controller.BatalhaController import BatalhaController
from Controller.PersonagemController import PersonagemController
from View.PersonagemView import PersonagemView


from Model.Batalha import Batalha
from Controller.Menu import Menu
from View.Mapa import Mapa
from View.tela_mapa import TelaMapa


import pygame

class Jogo:
    def __init__(self):
        pygame.init()
        # self.__window = pygame.display.set_mode((900, 500),
        #                                       pygame.RESIZABLE)
        # self.__winw, self.__winh = self.__window.get_size()

        # # Elementos a serem mostrados na tela
            
        # self.__resultado = []

        # self.__elements = ['']*7
        # for i in range(7):
        #     self.__elements[i] = pygame.transform.scale(pygame.image.load(
        #                                               os.path.join('versao_final/assets',
        #                                               'retangulo.png')),
        #                                               (50, 50))

    def update_window(self):
        pass
        # self.__window.fill((255, 255, 255))
        # for PersonagemView in time:
        #     PersonagemView.draw()
        # for PersonagemView in inimigos:
        #     PersonagemView.draw()
        # cont = 7
        # for elemento in self.__elements:
        #     self.__window.blit(elemento, (self.__winw/22*cont,
        #                                 self.__winh-50))
        #     cont += 1
        # for i in self.__resultado:
        #     self.__window.blit(i, (self.__winw/4, self.__winh/4))
        # pygame.display.update()
        

    # Parâmetros temporários -> inimigos devem ser gerados pelo mapa e aliados provenientes
    # de serialização
    def run(self, aliados, inimigos):
        menu = Menu()
        play = menu.runMenu()
        if play:
            # mapa = TelaMapa()
                    # Mapa deve retornar os inimigos da fase clicada
                    # Mapa também deve retornar o cenário a ser enviado à batalha

            batalha = Batalha(aliados, inimigos)
            batalha.start()
        # fps = 60
        # clock = pygame.time.Clock()


        # run = True
        # finished = False
        # while run:
        #     clock.tick(fps)
        #     for event in pygame.event.get():
        #         finished = self.__jogo.watch(event, finished)
        #         if event.type == pygame.QUIT:
        #             return False
        #         if finished:
        #             result = pygame.transform.scale(
        #                 pygame.image.load(os.path.join('assets',
        #                                                f'allies.png')),
        #                 (self.__winw/2, self.__winh/2))
        #             self.__resultado.append(result)

        #     self.update_window()
