from View.Cenario import Cenario

#esta aqui apenas para indicar que vai existir essa classe,
# mas no momento, nao tem nada implementado

class CenarioLoja(Cenario):
    def __init__(self,identificador:str, largura:int, altura:int,
                 eixo_x:int, eixo_y:int,itens: dict):
        super().__init__(identificador,largura,altura,eixo_x,eixo_y)
        self.__itens = itens
    @property
    def itens(self):
        return self.__itens

    def compra_item(self,item_pego):
        return self.__itens.pop(item_pego)

    def get_item(self,item_pego):
        return self.__itens[item_pego]