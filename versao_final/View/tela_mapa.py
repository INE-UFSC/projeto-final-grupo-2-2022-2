import pygame
from Cenario import Cenario, CenarioIcone, CenarioBatalha
from Mapa import Mapa
import os

class TelaMapa:
    def __init__(self):
        self.__LARGURA = 800
        self.__ALTURA = 500
        self.__QUADROS_POR_SEGUNDO = 60

        self.__preto = pygame.Color(0,0,0)
        self.__branco = pygame.Color(255,255,255)

        pygame.init()
        self.__tela = pygame.display.set_mode((self.__LARGURA, self.__ALTURA))
        pygame.display.set_caption("mapa")
        self.__clock = pygame.time.Clock()
        self.__tela.fill(self.__preto)

        self.__rodando = True
        self.__in_mapa = True
        self.__in_lugar = False

        self.__sprites_jogo = pygame.sprite.Group()
        self.__mapa = Mapa({"Saffron": CenarioIcone(CenarioBatalha("Saffron.jpg",
                                               800,500,400,250)
                                               ,431,148,75,83)},
                           "mapa.jpg",500,800,400,250)
        self.main()


    def back(self,click):
        #temp = os.getcwd().split(os.path.sep)
        #temp.remove("View")
        #temp = os.path.sep.join(temp)
        #caminho = os.path.join(temp, "assets")
        #imagem_back = pygame.image.load(os.path.join(caminho, 'back_buttom.png')).convert()
        #imagem_back = pygame.transform.scale(imagem_back, (50, 50))
        #back_rect = imagem_back.get_rect()
        #back_rect_center = (750, 550)
        hit_back = pygame.Rect(750, 450, 50, 50)
        #self.__tela.blit(imagem_back,back_rect_center)
        if hit_back.collidepoint(click):
            return True
        return False
        #essas partes estao comentadas pois nao estao funcionando direito, vou corrigir depois
    def main(self):
        while self.__rodando:
            self.__clock.tick(self.__QUADROS_POR_SEGUNDO)
            if self.__in_mapa:
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
                self.__tela.blit(prox_lugar.imagem, prox_lugar.rect)
                temp = os.getcwd().split(os.path.sep)
                temp.remove("View")
                temp = os.path.sep.join(temp)
                caminho = os.path.join(temp, "assets")
                imagem_back = pygame.image.load(os.path.join(caminho, 'back_buttom.png')).convert()
                imagem_back = pygame.transform.scale(imagem_back, (50, 50))
                back_rect = (750, 450)
                self.__tela.blit(imagem_back, back_rect)

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

t = TelaMapa()

#back está mal implementado, ainda nao pensei em uma boa maneira de coloca-lo no codigo
