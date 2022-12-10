import pygame
from View.Sprite import Sprite
from View.SkillSlot import SkillSlot
from Model.Personagem import Personagem
import os

class BatalhaView:
    def __init__(self, 
                 aliados: pygame.sprite.Group, 
                 inimigos: pygame.sprite.Group,
                 posicoes: list) -> None:
        self.__aliados = aliados
        self.__inimigos = inimigos
        self.__slots = [SkillSlot(i) for i in posicoes]
        self.__spritesSlots = pygame.sprite.Group(self.__slots)
        self.__habilidades = pygame.sprite.Group()
        self.__projetilInimigo = pygame.sprite.Group()
    
    def draw(self, 
             screen:pygame.Surface,
             aliados: list[Personagem],
             inimigos: list[Personagem]):
        screen.fill((255, 255, 255))
        self.__aliados.draw(screen)
        self.__inimigos.draw(screen)
        self.__spritesSlots.draw(screen)
        self.__habilidades.draw(screen)
        self.__projetilInimigo.draw(screen)
        for aliado, inimigo in zip(aliados, inimigos):
            aliado.criaBarraDeVida(screen)
            inimigo.criaBarraDeVida(screen)

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
