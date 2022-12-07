from View.BatalhaView import BatalhaView
from View.Menu import Menu
from View.Mapa import Mapa
from Model.Batalha import Batalha
from Model.Personagem import Personagem
from Model.CenarioModel import CenarioModel
from View.CenarioBatalha import CenarioBatalha
from Singleton.Constantes import Constantes
from Controller.JogoDAO import *
from Controller.PersonagemDAO import *

import pygame

class Jogo:
    def __init__(self):
        self.__nivel = 0
        self.__save = SaveNivel
        self.save()

    def save(self):
        self.__save.add(self.__nivel)
    # Parâmetros temporários -> inimigos devem ser gerados pelo mapa e aliados provenientes
    # de serialização
    def run(self, aliados):
        inimigos = Constantes().locais[self.__nivel].cenario.inimigos
        menu = Menu()
        play = menu.main()

        if play:
            # mapa = TelaMapa()
                    # Mapa deve retornar os inimigos da fase clicada
                    # Mapa também deve retornar o cenário a ser enviado à batalha

            batalha = Batalha(aliados, inimigos)
            batalha.start()
            self.__nivel += 1
            self.save()

from Singleton.Constantes import Constantes

acoes = Constantes().skills

magos = [None]*3

for i in range(3):
    magos[i] = Personagem(nome = 'Joao' + str(i), 
                          nivel = 1,
                          tecnicas = [acoes[i-1], acoes[i]], 
                          classe = 'mago')
