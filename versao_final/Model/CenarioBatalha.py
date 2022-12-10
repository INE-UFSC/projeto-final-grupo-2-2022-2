from Model.Cenario import Cenario
from DAO.PersonagemDAO import inimigos as Inimigos
from Model.Personagem import Personagem

class CenarioBatalha(Cenario):
    def __init__(self,
                 identificador:str, 
                 largura:int,
                 altura:int, 
                 eixo_x:int, 
                 eixo_y:int,
                 nivel:int):
        super().__init__(identificador, largura,
                         altura, eixo_x, eixo_y)
        self.__inimigos = Inimigos[nivel]

    @property
    def inimigos(self) -> list[Personagem]:
        return self.__inimigos