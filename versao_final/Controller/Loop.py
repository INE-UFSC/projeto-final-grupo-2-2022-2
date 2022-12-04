# vou fazer um loop novo para o jogo,depois podemos discutir como ele deve ser feito
from View.tela_mapa import Tela
from View.Mapa import Mapa
from Menu import Menu
import pygame
from View.Cenario import *
class Loop():
    def __init__(self):
        self.__tela = Tela()
        self.__rodando = True
        self.__in_mapa = True
        self.__in_lugar = False
        self.__menu = Menu()
        self.__mapa = Mapa({"Saffron": CenarioIcone(Cenario("Saffron.jpg",
                                               800,500,400,250),
                                               431,148,75,83)},
                           "mapa.jpg",500,800,400,250)
    def main(self):
        while self.__rodando:

            self.__clock.tick(self.__tela.fps)
            if self.__in_mapa:
                imagem_tela = self.__mapa
                self.__tela.display.blit(imagem_tela.imagem, imagem_tela.rect)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.__rodando = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        posicao = pygame.mouse.get_pos()
                        if event.button == 1:
                            for lugar in self.__mapa.locais.keys():
                                if self.__mapa.locais[lugar].hitbox.collidepoint(posicao):
                                    self.__mapa.locais[lugar].clicked = True

                    for lugar in self.__mapa.locais.keys():
                        if self.__mapa.locais[lugar].clicked:
                            self.__in_mapa = False
                            self.__in_lugar = True
                            self.__mapa.locais[lugar].clicked = False
                            prox_lugar = self.__mapa.locais[lugar].cenario
            elif self.__in_lugar:
                self.__tela.display.blit(prox_lugar.imagem, prox_lugar.rect)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.__rodando = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:

                        posicao = pygame.mouse.get_pos()
                        if event.button == 1:
                            temp = self.back(posicao)
                            self.__in_mapa = temp
                            self.__in_lugar = not temp
            self.__sprites_jogo.update()

            # desenha
            self.__sprites_jogo.draw(self.__tela)
            pygame.display.flip()
        pygame.quit()