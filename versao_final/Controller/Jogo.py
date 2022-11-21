from Model.Personagem import Personagem
from Model.Batalha import Batalha
from Model.Acao import Acao
import os
from BatalhaController import BatalhaController
from View.PersonagemView import PersonagemView
import pygame

class Jogo:
    def __init__(self):
        pygame.init()
        self.__window = pygame.display.set_mode((900, 500),
                                              pygame.RESIZABLE)
        self.__winw, self.__winh = self.__window.get_size()

        # Elementos a serem mostrados na tela
        self.__acoes = [
            Acao('fireball', -5, 'saude', 'ofensivo'),
            Acao('boost', 5, 'ataque', 'suporte')
        ]

        self.__elements = ['']*7
        for i in range(7):
            self.__elements[i] = pygame.transform.scale(pygame.image.load(
                                                      os.path.join('assets',
                                                      'retangulo.png')),
                                                      (50, 50))

        self.__magos = ['']*3
        self.__orcs = ['']*3
        self.__time = ['']*3
        self.__inimigos = ['']*3
        for i in range(3):
            self.__magos[i] = Personagem('Joao' + str(i), 10,
                                       100, self.__acoes, 'mago')
            self.__orcs[i] = Personagem('Mateus' + str(i), 10,
                                       100, self.__acoes, 'orc')
            self.__time[i] = PersonagemView(self.__window,
                                          self.__magos[i],
                                          200, 100 + i*100,
                                          70, 80)
            self.__inimigos[i] = PersonagemView(self.__window,
                                          self.__orcs[i],
                                          600, 100 + i*100,
                                          70, 80)
        self.__resultado = []

        self.__jogo = BatalhaController(self.__time,
                                      self.__inimigos)
        #if __name__ == "__main__":
        #    self.__main()

    def update_window(self):
        self.__window.fill((255, 255, 255))
        for PersonagemView in self.__time:
            PersonagemView.draw()
        for PersonagemView in self.__inimigos:
            PersonagemView.draw()
        cont = 7
        for elemento in self.__elements:
            self.__window.blit(elemento, (self.__winw/22*cont,
                                        self.__winh-50))
            cont += 1
        for i in self.__resultado:
            self.__window.blit(i, (self.__winw/4, self.__winh/4))
        pygame.display.update()
        

    def main(self):
        fps = 60
        clock = pygame.time.Clock()


        run = True
        finished = False
        while run:
            clock.tick(fps)
            for event in pygame.event.get():
                finished = self.__jogo.watch(event, finished)
                if event.type == pygame.QUIT:
                    return False
                if finished:
                    result = pygame.transform.scale(
                        pygame.image.load(os.path.join('assets',
                                                       f'allies.png')),
                        (self.__winw/2, self.__winh/2))
                    self.__resultado.append(result)

            self.update_window()
