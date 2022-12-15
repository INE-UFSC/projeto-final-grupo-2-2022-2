from Model.Botao import Botao
import pygame
from View.Tela import Tela
#from Singleton.Constantes import Constantes
import os


class Menu():
    def __init__(self, tela:Tela):
        self.__tela = tela
        self.__size = self.__tela.display.get_size()
        self.__botoes = [Botao('play', self.__size[0]/2, self.__size[1]/2)]
        self.__image = pygame.image.load(os.path.join('assets','menu.jpeg')).convert()
        self.__image = pygame.transform.scale(self.__image, self.__size)
        self.__rect = self.__image.get_rect()
        self.__centro_largura,self.__centro_altura = self.__size
        self.__rect.center = (self.__centro_largura/2,self.__centro_altura/2)

    def run(self):
        run = True
        play = False

        self.__tela.display.blit(self.image, self.rect)

        for botao in range(len(self.botoes)):
            pygame.draw.rect(self.__tela.display, self.botoes[botao].cor_fundo, self.botoes[botao].rect)
            self.__tela.display.blit(self.botoes[botao].texto, self.botoes[botao].rect_texto)

        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE:
                self.__tela.size = event.w, event.h
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                posicao = pygame.mouse.get_pos()
                if event.button == 1:
                    for botao in range(len(self.botoes)):
                        if self.botoes[botao].rect.collidepoint(posicao):
                            play = True
        
        pygame.display.flip()
        return (run, play)

    @property
    def botoes(self) -> list[Botao]:
        return self.__botoes

    @property
    def rect(self):
        return self.__rect

    @property
    def image(self):
        return self.__image


    def inicia(self):
        pass
