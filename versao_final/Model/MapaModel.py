from View.Tela import Tela
from View.Mapa import Mapa
from Model.CenarioModel import CenarioModel

class MapaModel:
    def __init__(self) -> None:
        # self.__tela = Tela()
        self.__mapa = Mapa()
        self.__cenarios: list[CenarioModel] = []

    def inicia(self):
        pass