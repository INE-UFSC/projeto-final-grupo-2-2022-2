import pygame
from View.Sprite import Sprite
from View.SkillSlot import SkillSlot
from Model.Personagem import Personagem
from View.Tela import Tela
import os

class BatalhaView:
    def __init__(self, 
                 aliados: pygame.sprite.Group, 
                 inimigos: pygame.sprite.Group,
                 posicoes: list,
                 tela:Tela) -> None:
        self.__aliados = aliados
        self.__inimigos = inimigos
        self.__tela = tela
        self.__slots = [SkillSlot(i) for i in posicoes]
        self.__spritesSlots = pygame.sprite.Group(self.__slots)
        self.__habilidades = pygame.sprite.Group()
        self.__projetilInimigo = pygame.sprite.Group()
        self.__image = pygame.image.load(os.path.join('assets', 'background.png'))
        self.__image = pygame.transform.scale(self.__image, tela.display.get_size())
        self.__rect = self.__image.get_rect()
        
    
    def draw(self,
             aliados: list[Personagem],
             inimigos: list[Personagem]):
        self.__tela.display.blit(self.__image, self.__rect)
        self.__aliados.draw(self.__tela.display)
        self.__inimigos.draw(self.__tela.display)
        self.__spritesSlots.draw(self.__tela.display)
        self.__habilidades.draw(self.__tela.display)
        self.__projetilInimigo.draw(self.__tela.display)
        for aliado, inimigo in zip(aliados, inimigos):
            aliado.criaBarraDeVida(self.__tela.display)
            inimigo.criaBarraDeVida(self.__tela.display)

        pygame.display.update()
    
    def mostraHabilidades(self, habilidades: list[Sprite]):
        self.__habilidades.empty()

        for i, sprite in enumerate(habilidades):
            slot = self.__slots[i]
            sprite.rect.center = slot.rect.center
            sprite.width, sprite.height = slot.width - 4, slot.height - 4

            self.__habilidades.add(sprite)
    
    def mostraResultado(self, screen:pygame.Surface, vencedor:str):
        image = pygame.image.load(os.path.join('assets', f'{vencedor}.png'))
        largura = screen.get_size()[0] / 2
        altura = screen.get_size()[1] / 2
        image = pygame.transform.scale(image, (largura, altura))
        rect = pygame.Rect(largura/2, altura/2, largura, altura)
        screen.blit(image, rect)
        pygame.display.update()
    
    @property
    def projetilInimigo(self):
        return self.__projetilInimigo
    @projetilInimigo.setter
    def projetilInimigo(self, projetil):
        self.__projetilInimigo = pygame.sprite.Group(projetil)
