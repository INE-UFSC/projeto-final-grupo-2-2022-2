from Jogo import Jogo

# cada item deve ter um nome, um fator
# (quanto vai afetar o que deseja)
# e qual atributo vai afetar

Items = [
    ['Paracetamol', 5, 'saude', 1]
]

class Item:
    def __init__(self, nome: str, fator:int, 
                efeito:str):
        self.__nome = nome
        self.__fator = fator
        self.__efeito = efeito