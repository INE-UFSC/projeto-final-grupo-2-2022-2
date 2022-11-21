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
        self.window = pygame.display.set_mode((900, 500), pygame.RESIZABLE)
        self.winw, self.winh = self.window.get_size()

        # Elementos a serem mostrados na tela
        self.acoes = [
            Acao('fireball', -5, 'saude', 'ofensivo'),
            Acao('boost', 5, 'ataque', 'suporte')
        ]

        self.elements = ['']*7
        for i in range(7):
            self.elements[i] = pygame.transform.scale(
            pygame.image.load(os.path.join('assets',
                                           'retangulo.png')),
            (50, 50))

        self.magos = ['']*6
        for i in range(6):
            self.magos[i] = Personagem('Joao', 5,
                                       100, self.acoes,
                                       'mago', (70,
                                                80))

        self.time = ['']*3
        self.inimigos = ['']*3
        for i in range(3):
            self.time[i] = PersonagemView(self.window,
                                          self.magos[i],
                                          100, 200)
            #PersonagemView(window, magos[4], 200, 100),
            #PersonagemView(window, magos[5], 200, 300)
            self.inimigos[i] =  PersonagemView(self.window,
                                               self.magos[i+3],
                                               700, 200)
            #PersonagemView(window, magos[2], 600, 100),
            #PersonagemView(window, magos[3], 600, 300)

        self.resultado = []

        self.jogo = BatalhaController(self.time,
                                      self.inimigos)
        if __name__ == "__main__":
            self.main()

    def update_window(self):
        self.window.fill((255, 255, 255))
        for PersonagemView in self.time:
            PersonagemView.draw()
        for PersonagemView in self.inimigos:
            PersonagemView.draw()
        cont = 7
        for elemento in self.elements:
            self.window.blit(elemento, (self.winw/22*cont, self.winh-50))
            cont += 1
        for i in self.resultado:
            self.window.blit(i, (self.winw/4, self.winh/4))
        pygame.display.update()
        

    def main(self):
        fps = 60
        clock = pygame.time.Clock()


        run = True
        finished = False
        while run:
            clock.tick(fps)
            for event in pygame.event.get():
                finished = self.jogo.watch(event, finished)
                if event.type == pygame.QUIT:
                    return False
                if finished:
                    result = pygame.transform.scale(
                        pygame.image.load(os.path.join('assets', f'allies.png')),
                        (self.winw/2, self.winh/2))
                    self.resultado.append(result)

            self.update_window()
