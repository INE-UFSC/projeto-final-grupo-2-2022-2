import pygame
from View.Cenario import Cenario, CenarioIcone
from View.Mapa import Mapa
import os

class TelaMapa:
    def __init__(self):
        self.__LARGURA = 800
        self.__ALTURA = 500
        self.__QUADROS_POR_SEGUNDO = 60

        self.__preto = pygame.Color(0, 0, 0)

        pygame.init()
        self.__tela = pygame.display.set_mode((self.__LARGURA, self.__ALTURA))
        pygame.display.set_caption("mapa")
        self.__clock = pygame.time.Clock()
        self.__tela.fill(self.__preto)

        self.__rodando = True
        self.__in_mapa = True
        self.__in_lugar = False

        self.__sprites_jogo = pygame.sprite.Group()
        self.__mapa = Mapa({"Saffron": Cenario("Saffron.jpg",
                                               800,500,400,250,
                                               431,148,75,83)},
                           "mapa.jpg",500,800,400,250)
        self.main()
        pygame.display.flip()
        pygame.quit()

    def main(self):

        while self.__rodando:

            self.__clock.tick(self.__QUADROS_POR_SEGUNDO)
            if self.__in_mapa:
                for i in self.__sprites_jogo:
                    self.__sprites_jogo.remove(i)
                imagem_tela = self.__mapa
                self.__tela.blit(imagem_tela.imagem, imagem_tela.rect)
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
                for i in self.__sprites_jogo:
                    self.__sprites_jogo.remove(i)
                self.__tela.blit(prox_lugar.imagem, prox_lugar.rect)
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


#back está mal implementado, ainda nao pensei em uma boa maneira de coloca-lo no codigo.