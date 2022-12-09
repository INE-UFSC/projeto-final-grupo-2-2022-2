class Inventario():
    def __init__(self,inventarios_personagens: list,itens: list,dinheiro:int):
        self.__itens = itens
        self.__dinheiro = dinheiro
        self.__invetarios_personagens = inventarios_personagens

    @property
    def itens(self):
        return self.__itens

    @property
    def inventarios_personagens(self):
        return self.__invetarios_personagens

    def equipa_item(self,item_equipado,item_antigo,inventario_alvo):
        if item_equipado.tipo() == inventario_alvo.tipo():
            if item_equipado.equipado == False:
                item_equipado.set_equipado(True)
                item_antigo.set_equipado(False)
                return self.__itens[item_equipado]
            else:
                return "esse item ja ta equipado"
        else:
            return "esse item nao pode ser equipado neste personagem"

    def add_item(self,novo_item):
        self.__itens.append(novo_item)

    @property
    def dinheiro(self):
        return self.__dinheiro

    def add_dinheiro(self,dinheiro_add):
        self.__dinheiro += dinheiro_add

    def remove_dinheiro(self,dinheiro_removido):
        self.__dinheiro -= dinheiro_removido


class InventarioPersonagem():
    def __init__(self,itens:list,tipo_aceito):
        self.__itens = itens
        self.__tipo_aceito = tipo_aceito

    @property
    def itens(self):
        return self.__itens

class Item():
    def __init__(self,nome:str,descricao:str,multiplicador:float):
        self.__nome = nome
        self.__

#terminar
#criar interface para essas coisas todas (eu nao aguento mais o pygame ;-; )

