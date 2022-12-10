from Model.Botao import Botao
import pygame
#from Singleton.Constantes import Constantes
import os


class Menu():
    def __init__(self):
        self.__botoes = [Botao('play', 600, 400)]
        self.__image = pygame.image.load(os.path.join('assets','orc.png')).convert()
        self.__image = pygame.transform.scale(self.__image,(1200, 600))
        self.__rect = self.__image.get_rect()
        self.__centro_largura,self.__centro_altura = (1200, 600)
        self.__rect.center = (self.__centro_largura/2,self.__centro_altura/2)

    def run(self, tela:pygame.Surface):
        run = True
        play = False

        tela.blit(self.image,self.rect)

        for botao in range(len(self.botoes)):
            pygame.draw.rect(tela, self.botoes[botao].cor_fundo, self.botoes[botao].rect)
            tela.blit(self.botoes[botao].texto, self.botoes[botao].rect_texto)

        for event in pygame.event.get():
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

