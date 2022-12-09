from Model.Personagem import Personagem
from View.BatalhaView import BatalhaView

import random as r

# -*- coding: utf-8 -*-

class Batalha:
    def __init__(self, aliados:list[Personagem],
                 inimigos:list[Personagem]):
        self.__aliados = aliados
        self.__inimigos = inimigos
        self.__view = BatalhaView(aliados,
                                  inimigos)

    def get_allies(self):
        return self.__aliados

    def get_enemies(self):
        return self.__inimigos

    def jogar_dados(self):
        return r.randint(1, 20)

    def start(self):
        return self.__view.loop()