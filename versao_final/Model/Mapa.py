from DAO.JogoDAO import JogoDAO
from Singleton.Locais import Locais
from View.Tela import Tela
from View.Sprite import Sprite
import pygame
import os

class Mapa():
    def __init__(self, tela:Tela):
        self.__tela = tela
        self.__locais = Locais().locais
        self.__image = pygame.image.load(os.path.join('assets', 'mapa.png')
                                         )
        self.__image = pygame.transform.scale(self.__image, tela.display.get_size())
    
    def inicia(self):
        run = True

        self.__tela.display.blit(self.__image, self.__image.get_rect())
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                posicao = pygame.mouse.get_pos()
                if event.button == 1:
                    for lugar in self.__locais:
                        if lugar.hitbox.collidepoint(posicao):
                            lugar.clicked = True

            for lugar in self.__locais:
            # essas condições servem para que não
            # se possa ir a uma lugar não desbloqueado
                cond = lugar.clicked
                cond2 = False
                if cond:
                    at = self.__locais.index(lugar)
                    lugar.clicked = False
                    nivel = JogoDAO().get()
                    cond2 = at <= nivel
                if cond2:
                    print(nivel)
                    return lugar.cenario.inimigos, nivel, run
        
        return [], 0, run

                            # batalha = BatalhaModel(aliados,
                            # lugar.cenario.inimigos())
                            # return batalha.start()
