from Jogo import Jogo

# cada acao deve ter um nome, um fator
# (quanto vai afetar, capaz de evoluir)
# e os efeitos, consistindo em qual
# atributo ela vai afetar, e quantos alvos


class Acao:
    def __init__(self, nome:str, fator: int,
                efeito:str, n_de_alvos:int):
        self.__nome = nome
        self.__fator = fator
        self.__efeito = efeito
        self.__n_de_alvos = n_de_alvos

    def evolucao(self):
        if self.__fator > 0:
            self.__fator += 5
        else:
            self.__fator -= 5
    
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome:str):
        self.__nome = nome


acoes = [
    Acao('fireball', -5, 'saude', 1)
]