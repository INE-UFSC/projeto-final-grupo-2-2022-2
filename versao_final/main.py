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
    Acao('fireball', -5, 'saude', 'ofensivo')
]

mago0 = Personagem('aaaa', 5, 100, acoes, 'mago.png', (70, 80))
mago1 = Personagem('aaaa', 5, 100, acoes, 'mago.png', (70, 80))
mago2 = Personagem('aaaa', 5, 100, acoes, 'mago.png', (70, 80))
mago3 = Personagem('aaaa', 5, 100, acoes, 'mago.png', (70, 80))
mago4 = Personagem('aaaa', 5, 100, acoes, 'mago.png', (70, 80))
mago5 = Personagem('aaaa', 5, 100, acoes, 'mago.png', (70, 80))
retangulo = pygame.transform.scale(
    pygame.image.load(os.path.join('assets', 'retangulo.png')),
    (50, 50))
retangulo2 = pygame.transform.scale(
    pygame.image.load(os.path.join('assets', 'retangulo.png')),
    (50, 50))
retangulo3 = pygame.transform.scale(
    pygame.image.load(os.path.join('assets', 'retangulo.png')),
    (50, 50))
retangulo4 = pygame.transform.scale(
    pygame.image.load(os.path.join('assets', 'retangulo.png')),
    (50, 50))
retangulo5 = pygame.transform.scale(
    pygame.image.load(os.path.join('assets', 'retangulo.png')),
    (50, 50))
retangulo6 = pygame.transform.scale(
    pygame.image.load(os.path.join('assets', 'retangulo.png')),
    (50, 50))
retangulo7 = pygame.transform.scale(
    pygame.image.load(os.path.join('assets', 'retangulo.png')),
    (50, 50))



# Lista de Elementos
time = [
    PersonagemView(window, mago0, 100, 200),
    PersonagemView(window, mago4, 200, 100),
    PersonagemView(window, mago5, 200, 300)
]

inimigos = [
    PersonagemView(window, mago1, 700, 200),
    PersonagemView(window, mago2, 600, 100),
    PersonagemView(window, mago3, 600, 300)
]

elements = [
    retangulo,
    retangulo2,
    retangulo3,
    retangulo4,
    retangulo5,
    retangulo6,
    retangulo7,
]

resultado = [

]

jogo = BatalhaController(time, inimigos)

def update_window(window:pygame.Surface):
    window.fill((255, 255, 255))
    for PersonagemView in time:
        PersonagemView.draw()
    for PersonagemView in inimigos:
        PersonagemView.draw()
    cont = 7
    for i, elemento in enumerate(elements):
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
