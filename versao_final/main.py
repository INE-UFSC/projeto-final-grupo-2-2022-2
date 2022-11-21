from Controller.Jogo import Jogo

jogo = Jogo()

'''
from Model.Personagem import Personagem
from Model.Batalha import Batalha
from Model.Acao import Acao
import os
from Controller.BatalhaController import BatalhaController
from View.PersonagemView import PersonagemView
import pygame

pygame.init()
window = pygame.display.set_mode((900, 500), pygame.RESIZABLE)
winw, winh = window.get_size()

# Elementos a serem mostrados na tela
acoes = [
    Acao('fireball', -5, 'saude', 'ofensivo'),
    Acao('boost', 5, 'ataque', 'suporte')
]

elements = ['']*7
for i in range(7):
    elements[i] = pygame.transform.scale(
    pygame.image.load(os.path.join('assets', 'retangulo.png')),
    (50, 50))

magos = ['']*6
for i in range(6):
   magos[i] = Personagem('Joao', 5, 100, acoes, 'mago', (70, 80))

time = ['']*3
inimigos = ['']*3
for i in range(3):
    time[i] = PersonagemView(window, magos[0], 100, 200)
    #PersonagemView(window, magos[4], 200, 100),
    #PersonagemView(window, magos[5], 200, 300)
    inimigos[i] =  PersonagemView(window, magos[1], 700, 200)
    #PersonagemView(window, magos[2], 600, 100),
    #PersonagemView(window, magos[3], 600, 300)

resultado = []

jogo = BatalhaController(time, inimigos)

def update_window(window:pygame.Surface):
    window.fill((255, 255, 255))
    for PersonagemView in time:
        PersonagemView.draw()
    for PersonagemView in inimigos:
        PersonagemView.draw()
    cont = 7
    for elemento in elements:
        window.blit(elemento, (winw/22*cont, winh-50))
        cont += 1
    for i in resultado:
        window.blit(i, (winw/4, winh/4))
    pygame.display.update()
    

def main(window: pygame.Surface):
    fps = 60
    clock = pygame.time.Clock()


    run = True
    finished = False
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            finished = jogo.watch(event, finished)
            if event.type == pygame.QUIT:
                return False
            if finished:
                result = pygame.transform.scale(
                    pygame.image.load(os.path.join('assets', f'allies.png')),
                    (winw/2, winh/2))
                resultado.append(result)
                

        update_window(window)

if __name__ == "__main__":
    main(window)
'''