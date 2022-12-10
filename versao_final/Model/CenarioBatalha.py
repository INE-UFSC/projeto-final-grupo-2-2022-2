from View.Cenario import Cenario

class CenarioBatalha(Cenario):
    def __init__(self, identificador:str, largura:int,
                 altura:int, eixo_x:int, eixo_y:int,
                 nivel:int, inimigos:list):
        super().__init__(identificador, largura,
                         altura, eixo_x, eixo_y)
        self.__inimigos = inimigos
        self.__nivel = nivel

    @property
    def nivel(self) -> list:
        return self.__nivel

    @property
    def inimigos(self) -> list:
        return self.__inimigos