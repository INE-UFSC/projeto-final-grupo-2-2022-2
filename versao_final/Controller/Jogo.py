from Model.Personagem import Personagem
import os
from Controller.BatalhaController import BatalhaController
from Controller.PersonagemController import PersonagemController
from View.PersonagemView import PersonagemView


from Model.Batalha import Batalha
from Controller.Menu import Menu
from View.Mapa import Mapa
from View.tela_mapa import TelaMapa


import pygame

class Jogo:
    def __init__(self):
        pygame.init()
        
    # Parâmetros temporários -> inimigos devem ser gerados pelo mapa e aliados provenientes
    # de serialização
    def run(self, aliados, inimigos):
        menu = Menu()
        play = menu.runMenu()

        if play:
            # mapa = TelaMapa()
                    # Mapa deve retornar os inimigos da fase clicada
                    # Mapa também deve retornar o cenário a ser enviado à batalha

            batalha = Batalha(aliados, inimigos)
            batalha.start()
