import pygame
from Model.Personagem import Personagem
from View.Sprite import Sprite
from Controller.BatalhaController import BatalhaController
from Model.Acao import Acao
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
        self.__finished = False
        self.__winner = -1

        self.createSprites()


    def createSprites(self):

        self.__timeAliado = pygame.sprite.Group()
        self.__timeInimigo = pygame.sprite.Group()
        self.__elements = pygame.sprite.Group()
        self.__skills = pygame.sprite.Group()

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
            aliado.sprite = aliadoSprite
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
            inimigo.sprite = inimigoSprite
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
            self.__skills.add(skill)
            cont += 1
    
    def animation(self, atacante:Personagem, alvo:Personagem, habilidade:Acao):
        atacanteSprite = atacante.sprite
        alvoSprite = alvo.sprite

        default_width, default_height = 60, 80

        for i in range (10):
            atacanteSprite.rect.x += 2
            self.draw()
            
            # pygame.sprite.Group(atacante.sprite).draw(self.__window)
            # pygame.display.flip()
            
        time.sleep(0.5)
        multiplicador = r.randint(1, 20)

        habilidadeSprite = Sprite(filename = habilidade.nome, 
                                  width = default_width,
                                  height = default_height,
                                  x = atacante.sprite.rect.x,
                                  y = atacante.sprite.rect.y)

        if atacanteSprite in self.__timeAliado:    
            atacantePos = self.__timeAliado.sprites().index(atacanteSprite)
            alvoPos = self.__timeInimigo.sprites().index(alvoSprite)
        else:
            atacantePos = self.__timeInimigo.sprites().index(atacanteSprite)
            alvoPos = self.__timeAliado.sprites().index(alvoSprite)
        
        hit = False
        while not hit:
            hit, habilidadeSprite = habilidade.animation(atacanteSprite, alvoSprite, habilidadeSprite, atacantePos, alvoPos)
            self.__skills.add(habilidadeSprite)
            self.draw()
        habilidadeSprite.kill()

        habilidade.executar(alvo, multiplicador)

        for i in range (10):
            if i%2 == 0:
                alvoSprite.rect.x += 4
                alvoSprite.rect.y += 4
            else:
                alvoSprite.rect.x -= 4
                alvoSprite.rect.y -= 4

            self.draw()
            # pygame.sprite.Group(alvo.sprite).draw(self.__window)
            # pygame.display.flip()


    def checkForWinner(self):
        cont = 0
        for i in self.__aliadosPersonagens:
            if i.get_saude() >= 0:
                cont += 1
        if cont == 0:
            self.__finished = True
            self.__winner = 0
            return
        cont = 0
        for i in self.__inimigosPersonagens:
            if i.get_saude() >= 0:
                cont += 1
        if cont == 0:
            self.__finished = True
            self.__winner = 1
            return
    
    def turno(self, atacante: Personagem,
                    alvos:list[Personagem]):

        habilidade = atacante.get_acao()
        
        alvo = r.choice(alvos)
        while alvo.get_saude() <= 0:
            alvo = r.choice(alvos)

        if habilidade.tipo == 'suporte':
            pass

        self.animation(atacante, alvo, habilidade)

        self.__playerTurn = not self.__playerTurn
        self.checkForWinner()

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
        self.__timeAliado.draw(self.__window)
        self.__timeInimigo.draw(self.__window)
        self.__elements.draw(self.__window)
        self.__skills.draw(self.__window)
        self.drawHealthBars()
        pygame.display.flip()
    
    def showResult(self, winner:str):
        winw, winh = self.__window.get_size()
        result = pygame.image.load(os.path.join('versao_final/assets', f'{winner}.png'))
        result = pygame.transform.scale(result, (winw/2, winh/2))
        self.__window.blit(result, (winw/4, winh/4))
        pygame.display.update()

    def main(self):
        fps = 30
        clock = pygame.time.Clock()
        run = True
        
        while run:
            clock.tick(fps)

            for event in pygame.event.get():
                if event.type == pygame.VIDEORESIZE:
                    window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    pygame.display.update()
                
                if self.__finished:
                    if self.__winner == 0:
                        self.showResult('enemies')
                    else:
                        self.showResult('allies')
                else:
                    if self.__playerTurn:
                        atacantes, sprites = self.__aliadosPersonagens, self.__timeAliado
                        alvos = self.__inimigosPersonagens

                        for i, sprite in enumerate(sprites):
                            if event.type == pygame.MOUSEBUTTONDOWN and sprite.rect.collidepoint(pygame.mouse.get_pos()):
                                self.turno(atacantes[i], alvos)
                    else:
                        atacante = r.choice(self.__inimigosPersonagens)
                        while atacante.get_saude() <= 0:
                            atacante = r.choice(self.__inimigosPersonagens)

                        alvos = self.__aliadosPersonagens
                        time.sleep(0.5)
                        self.turno(atacante, alvos)

                    self.createSprites()
                    self.draw()

                if event.type == pygame.QUIT:
                    return False
