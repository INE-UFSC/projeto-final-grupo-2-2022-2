import random as r
from Model.Sprite import Sprite
from Model.Acao import Acao
from Model.Sprite import Sprite
#from time import sleep

class Personagem:
    def __init__(self, nome:str, nivel:int,
                 tecnicas:list, classe:str):
        self.__nome = nome
        self.__nivel = nivel
        self.__saude_max = 100 + 10*nivel
        self.__ataque_max = 100 + 10*nivel
        self.__saude_at = self.__saude_max
        self.__ataque_at = self.__ataque_max
        self.__tecnicas = tecnicas
        self.__classe = classe
        self.__sprite = Sprite(classe)
        self.__batalhas = [0]

    @property
    def nome(self) -> str:
        return self.__nome
    @nome.setter
    def nome(self, novo:str):
        self.__nome = novo

    @property
    def sprite(self) -> Sprite:
        return self.__sprite
    @sprite.setter
    def sprite(self, novo:Sprite):
        self.__sprite = novo

    @property
    def ataque(self) -> int:
        return self.__ataque_max

    @property
    def saude(self) -> int:
        return self.__saude_max

    @property
    def tecnicas(self) -> list[Acao]:
        return self.__tecnicas

    @property
    def classe(self) -> str:
        return self.__classe
    @classe.setter
    def classe(self, novo:str):
        self.__classe = novo
        self.sprite = Sprite(novo)

    @property
    def batalhas(self) -> list:
        return self.__batalhas
    @batalhas.setter
    def batalhas(self, novo):
        print('Não envie parâmetros!!!')
    
    @property
    def saude_max(self) -> int:
        return self.__saude_max

# retornam a saude e o ataque atual, em batalha

    def get_saude(self) -> int:
        return self.__saude_at
    
    def get_ataque(self) -> int:
        return self.__ataque_at

# escolhe uma tecnica 

    def get_acao(self, num=0):
        if len(self.__tecnicas) > num:
            return self.__tecnicas[num]
        return None

# recebem o efeito ofensivo ou de suporte

    def afeta_saude(self, efeito:int):
        self.__saude_at += efeito
    
    def afeta_ataque(self, efeito:int):
        self.__ataque_at += efeito

# expande as tecnicas

    def aprender_tecnica(self, novo):
        self.__tecnicas.append(novo)

# resetam os status e evoluem depois da batalha

    def fim_da_batalha(self):
        self.__nivel += 1
        self.__batalhas.append(self.__nivel)

        var = r.choice(['ataque', 'saude'])
        self.evoluir_atributo(var)

        self.__saude_at = self.__saude_max
        self.__ataque_at = self.__ataque_max

        var = r.choice(self.__tecnicas)
        self.evoluir_tecnica(var)

    
    def evoluir_tecnica(self, tecnica):
        if tecnica in self.__tecnicas:
            tecnica.evolucao()
        else: print("tecnica invalida")

    def evoluir_atributo(self, atributo: str):
        if atributo == 'ataque':
            self.__ataque_max += 5
        if atributo == 'saude':
            self.__saude_max += 5
        else:
            print('argumento invalido')

        self.__saude_max += (100*self.__nivel/10)//1
        self.__ataque_max += (100*self.__nivel/10)//1
        
