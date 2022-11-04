from combatClasses.mago import Mago
from Batalha import Batalha
from Acao import Acao, acoes
from BatalhaController import BatalhaController
import pygame
from element import Element

class BatalhaView(Batalha):
    def __init__(self, aliados: list[Element], inimigos: list[Element]) -> None:
        self.__allies = [i.char for i in aliados]
        self.__enemies = [i.char for i in inimigos]
        super().__init__(self.__allies, self.__enemies)
    
    def draw(self):
        self.__window.fill((255, 255, 255))
        for element in super().aliados:
            element.draw()
        for element in super().inimigos:
            element.draw()
        pygame.display.update()
    
    def start(self):
        pygame.init()
        self.__window = pygame.display.set_mode((900, 500), pygame.RESIZABLE)
        self.draw()

    
    def main(self):
        fps = 60
        clock = pygame.time.Clock()
        run = True
        finished = False
        
        while run:
            clock.tick(fps)
            for event in pygame.event.get():
                finished = BatalhaController.watch(super(), event, finished)
                if event.type == pygame.QUIT:
                    return False

            self.draw(self.__window)




# Elementos a serem mostrados na tela
# mago = Mago('aaaa', 5, 100, acoes)
# mago1 = Mago('aaaa', 5, 100, acoes)
# mago2 = Mago('aaaa', 5, 100, acoes)
# mago3 = Mago('aaaa', 5, 100, acoes)
# mago4 = Mago('aaaa', 5, 100, acoes)
# mago5 = Mago('aaaa', 5, 100, acoes)


# # Lista de elementos
# time = [
#     Element(window, mago, 100, 200),
#     Element(window, mago4, 200, 100),
#     Element(window, mago5, 200, 300),
    
# ]

# inimigos = [
#     Element(window, mago1, 700, 200),
#     Element(window, mago2, 600, 100),
#     Element(window, mago3, 600, 300)
# ]    

            # if not attack:
            #     rand = Random()
            #     targetPos = rand.randint(0, 2)
            #     target = enemies[targetPos]
            #     x, y = char.rect.centerx - 10, char.rect.centery-10
            #     fireball = Element(window, 'fireball.png', x, y, 20, 20)
            #     team.append(fireball)
            #     attack = True
            # else:
            #     fireball.rect.x += x_speed
            #     match targetPos:
            #         case 0:
            #             pass
            #         case 1:
            #             fireball.rect.y -= x_speed/5
            #         case 2:
            #             fireball.rect.y += x_speed/5

            #     if fireball.rect.collidepoint(target.rect.center):
            #         attack = False
            #         team.remove(fireball)
            #         print("char2 -5 vida")