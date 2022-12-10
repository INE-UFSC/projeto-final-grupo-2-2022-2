from Model.Cenario import Cenario
from Model.Personagem import Personagem
from Singleton.habilidades import Habilidades

class CenarioBatalha(Cenario):
    def __init__(self,
                 identificador:str, 
                 largura:int,
                 altura:int, 
                 eixo_x:int, 
                 eixo_y:int,
                 nivel:int,
                 inimigos: list[Personagem]):
        super().__init__(identificador, largura,
                         altura, eixo_x, eixo_y)
        self.__inimigos = inimigos

        # for i in range(3):
        #     nome = 'Inimigo' + str(nivel) + str(i)
        #     self.__inimigos[i] = Personagem(nome, 
        #                         nivel = nivel,
        #                         habilidades = Habilidades().skills,
        #                         classe = 'troll')

    @property
    def inimigos(self) -> list[Personagem]:
        return self.__inimigos