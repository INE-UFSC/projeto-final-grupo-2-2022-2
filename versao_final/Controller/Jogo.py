from View.BatalhaView import BatalhaView
from Controller.Menu import Menu
from View.Mapa import Mapa
from View.tela_mapa import TelaMapa


import pygame

class Jogo:
    def __init__(self):
        pass        
    # Parâmetros temporários -> inimigos devem ser gerados pelo mapa e aliados provenientes
    # de serialização
    def run(self, aliados, inimigos):
        menu = Menu()
        play = menu.main()

        if play:
            # mapa = TelaMapa()
                    # Mapa deve retornar os inimigos da fase clicada
                    # Mapa também deve retornar o cenário a ser enviado à batalha

            batalha = BatalhaView(aliados, inimigos)
            batalha.main()
