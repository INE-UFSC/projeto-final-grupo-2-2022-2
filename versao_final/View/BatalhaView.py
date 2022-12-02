import pygame
from Model.Personagem import Personagem
from View.Sprite import Sprite
from Controller.BatalhaController import BatalhaController
import os
import time
import random as r
class BatalhaView():
    def __init__(self, aliados: list[Personagem],
                 inimigos: list[Personagem]):
        self.__window = pygame.display.set_mode((1000, 500), pygame.RESIZABLE)

        self.__aliadosPersonagens = aliados
        self.__inimigosPersonagens = inimigos

        self.__timeAliado = pygame.sprite.Group()
        self.__timeInimigo = pygame.sprite.Group()
        self.__elements = pygame.sprite.Group()

        self.__playerTurn = True

        self.createSprites()

        self.__controller = BatalhaController(aliados, inimigos)

    def createSprites(self):

        self.__timeAliado = pygame.sprite.Group()
        self.__timeInimigo = pygame.sprite.Group()
        self.__elements = pygame.sprite.Group()

        winw, winh = self.__window.get_size()

        for i in range (3):
            default_width, default_height = 60, 80

            shift = 0
            if i == 1:
                shift = winw/10
            
            aliado = self.__aliadosPersonagens[i]

            if aliado.get_saude() <= 0:
                default_width, default_height = 0, 0

            aliadoSprite = Sprite(filename = aliado.classe, 
                                width = default_width, 
                                height = default_height, 
                                x = winw/5 - shift, 
                                y = winh/5 * (i+1))
            self.__timeAliado.add(aliadoSprite)

            default_width, default_height = 60, 80

            inimigo = self.__inimigosPersonagens[i]

            if inimigo.get_saude() <= 0:
                default_width, default_height = 0, 0

            inimigoSprite = Sprite(filename = inimigo.classe, 
                                width = default_width, 
                                height = default_height, 
                                x = winw - (winw/5 - shift + 60), 
                                y = winh/5 * (i+1))
            if aliado.get_saude() <= 0:
                aliadoSprite.width = 0
                aliadoSprite.height = 0
            self.__timeInimigo.add(inimigoSprite)
        
        cont = 7
        for i in range (7):
            ret = Sprite('retangulo', 50, 50, winw/22*cont, winh-50)
            self.__elements.add(ret)
            # if self.__aliadosPersonagens[i].get_acao()
            skill = Sprite('fireball', 46, 46, winw/22*cont - 2, winh-52)
            self.__elements.add(skill)
            cont += 1
    

    def drawHealthBars(self):
        for i, (aliado, inimigo) in enumerate(zip(self.__timeAliado, self.__timeInimigo)):
            w = 60
            h = 15

            if self.__aliadosPersonagens[i].get_saude() >= 0:
                xAliado, yAliado = aliado.rect.x, aliado.rect.y - 20
                pygame.draw.rect(self.__window, (0, 0, 0), pygame.Rect(xAliado, yAliado, w, h), 1)
                progressAliado = self.__aliadosPersonagens[i].get_saude() / self.__aliadosPersonagens[i].saude_max

                innerPos = (xAliado+3, yAliado+3)
                innerSize = ((w-6)*progressAliado, h-6)

                pygame.draw.rect(self.__window, (0, 255, 0), pygame.Rect(*innerPos, *innerSize))

            if self.__inimigosPersonagens[i].get_saude() >= 0:
                xInimigo, yInimigo = inimigo.rect.x, inimigo.rect.y - 20
                pygame.draw.rect(self.__window, (0, 0, 0), pygame.Rect(xInimigo, yInimigo, w, h), 1)
                progressInimigo = self.__inimigosPersonagens[i].get_saude() / self.__inimigosPersonagens[i].saude_max

                innerPos = (xInimigo+3, yInimigo+3)
                innerSize = ((w-6)*progressInimigo, h-6)

                pygame.draw.rect(self.__window, (0, 255, 0), pygame.Rect(*innerPos, *innerSize))

    def draw(self):
        self.__window.fill((255, 255, 255))
        self.__timeAliado.update(self.__window)
        self.__timeAliado.draw(self.__window)
        self.__timeInimigo.update(self.__window)
        self.__timeInimigo.draw(self.__window)
        self.__elements.update(self.__window)
        self.__elements.draw(self.__window)
        self.drawHealthBars()
        pygame.display.flip()
    
    def showResult(self, winner:str):
        winw, winh = self.__window.get_size()
        result = pygame.image.load(os.path.join('versao_final/assets', f'{winner}.png'))
        result = pygame.transform.scale(result, (winw/2, winh/2))
        self.__window.blit(result, (winw/4, winh/4))
        pygame.display.update()

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
                
                if self.__controller.finished:
                    if self.__controller.winner == 0:
                        self.showResult('enemies')
                    else:
                        self.showResult('allies')
                else:
                    if self.__playerTurn:
                        atacantes, sprites = self.__aliadosPersonagens, self.__timeAliado
                        alvos = self.__inimigosPersonagens

                        for i, sprite in enumerate(sprites):
                            if event.type == pygame.MOUSEBUTTONDOWN and sprite.rect.collidepoint(pygame.mouse.get_pos()):
                                self.__controller.turno(atacantes[i], alvos)
                                self.__playerTurn = not self.__playerTurn
                    else:
                        atacante = r.choice(self.__aliadosPersonagens)
                        alvos = self.__aliadosPersonagens
                        time.sleep(0.5)
                        self.__controller.turno(atacante, alvos)
                        self.__playerTurn = not self.__playerTurn

                    
                    self.createSprites()
                    self.draw()

                if event.type == pygame.QUIT:
                    return False
