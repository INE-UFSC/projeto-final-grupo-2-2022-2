
class InventarioPersonagem():
    def __init__(self,itens:list,
                 tipo_aceito):
        self.__itens = itens
        self.__tipo_aceito = tipo_aceito

    @property
    def itens(self):
        return self.__itens

#terminar
#criar interface para essas coisas todas (eu nao aguento mais o pygame ;-; )
