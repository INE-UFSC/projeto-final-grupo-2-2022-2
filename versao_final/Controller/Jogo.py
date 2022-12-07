from View.BatalhaView import BatalhaView
from View.Menu import Menu
from View.Mapa import Mapa
from View.tela_mapa import TelaMapa
from Model.Batalha import Batalha

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

            batalha = Batalha(aliados, inimigos)
            batalha.start()
