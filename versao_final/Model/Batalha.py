from Model.Personagem import Personagem

# from Controller.BatalhaController import BatalhaController

from View.BatalhaView import BatalhaView

import random as r

# -*- coding: utf-8 -*-

class Batalha:
    def __init__(self, aliados:list[Personagem],
                 inimigos:list[Personagem]):
        self.__aliados = aliados
        self.__inimigos = inimigos
        # self.__controller = BatalhaController(aliados, inimigos)
        self.__view = BatalhaView(aliados, inimigos)

    def get_allies(self):
        return self.__aliados

    def get_enemies(self):
        return self.__inimigos

    def jogar_dados(self):
        return r.randint(1, 20)

# recebe o time que esta atacando e
# o que esta defendendo, decidindo
# quem executa a ação e quem recebe,
# aleatoriamente, executa e checa se
# a saude chegou a 0

    def start(self):
        self.__view.main()
