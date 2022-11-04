import pygame
from Cenario import Cenario
from Mapa import Mapa

LARGURA = 800
ALTURA = 500
QUADROS_POR_SEGUNDO = 60

preto = pygame.Color(0, 0, 0)

pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("mapa")
clock = pygame.time.Clock()

rodando = True
in_mapa = True
in_lugar = False

sprites_jogo = pygame.sprite.Group()
mapa = Mapa({"Saffron": Cenario("Saffron.jpg",800,500,400,250,431,148,75,83)},"mapa.jpg",500,800,400,250)

while rodando:

    clock.tick(QUADROS_POR_SEGUNDO)
    if in_mapa:
        for i in sprites_jogo:
            sprites_jogo.remove(i)
        imagem_tela = mapa
        sprites_jogo.add(imagem_tela)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                posicao = pygame.mouse.get_pos()
                if event.button == 1:
                    for lugar in mapa.locais.keys():
                        if mapa.locais[lugar].hitbox.collidepoint(posicao):
                            mapa.locais[lugar].clicked = True

            for lugar in mapa.locais.keys():
                if mapa.locais[lugar].clicked:
                        in_mapa = False
                        in_lugar = True
                        mapa.locais[lugar].clicked = False
                        prox_lugar = mapa.locais[lugar]
    elif in_lugar:
        for i in sprites_jogo:
            sprites_jogo.remove(i)
        sprites_jogo.add(prox_lugar)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                in_mapa = True
                in_lugar = False







    # atualiza o estado do jogo
    sprites_jogo.update()


    # desenha
    tela.fill(preto)
    sprites_jogo.draw(tela)


    pygame.display.flip()

pygame.quit()




