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

mapa = Mapa({"direita": Cenario("lado_direito",500,400,400,125,400,0),
         "esquerda": Cenario("lado_esquerdo",500,400,400,375,0,0)},"mapa",500,800,400,250)

while rodando:

    clock.tick(QUADROS_POR_SEGUNDO)
    imagem_tela = mapa
    sprites_jogo.add(imagem_tela)
    if in_mapa:
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
                        prox_lugar = mapa.locais[lugar]
    elif in_lugar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
        sprites_jogo.remove(imagem_tela)
        sprites_jogo.add(prox_lugar)






    # atualiza o estado do jogo
    sprites_jogo.update()


    # desenha
    tela.fill(preto)
    sprites_jogo.draw(tela)


    pygame.display.flip()

pygame.quit()



