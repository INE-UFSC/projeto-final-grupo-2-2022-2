from View.Cenario import Cenario
from Model.Personagem import Personagem
from Singleton.Constantes import Constantes

class CenarioBatalha(Cenario):
    def __init__(self,identificador:str, largura:int,
                 altura:int, eixo_x:int, eixo_y:int,
                 nivel:int=1):
        super().__init__(identificador, largura,
                         altura, eixo_x, eixo_y)
        self.__inimigos = [None]*3
        for i in range(3):
            nome = 'Inimigo' + str(nivel) + str(i)
            self.__inimigos[i] = Personagem(nome, 
                                nivel = nivel,
                                tecnicas = Constantes().skills,
                                classe = 'troll')

    @property
    def inimigos(self) -> list[Personagem]:
        return self.__inimigos