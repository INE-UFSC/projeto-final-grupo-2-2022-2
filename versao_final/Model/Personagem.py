from Model.Acao import Acao
import random as r
# from Controller.PersonagemController import PersonagemController

class Personagem:
    def __init__(self, nome:str, nivel:int,
                 tecnicas:list, classe:str):
        self.__nome = nome
        self.__saude_max = (100 + 100*nivel/10)/1
        self.__ataque_max = (100 + 100*nivel/10)/1
        self.__saude_at = (100 + 100*nivel/10)/1
        self.__ataque_at = (100 + 100*nivel/10)/1
        self.__tecnicas = tecnicas
        self.__classe = classe
        self.__batalhas = []

    @property
    def nome(self) -> str:
        return self.__nome
    @nome.setter
    def nome(self, novo:str):
        self.__nome = novo

    @property
    def classe(self) -> str:
        return self.__classe
    @classe.setter
    def classe(self, novo:str):
        self.__classe = novo

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

    def get_acao(self, num=0) -> Acao:
        if len(self.__tecnicas) > num:
            return self.__tecnicas[num]
        return None

# recebem o efeito ofensivo ou de suporte

    def afeta_saude(self, efeito:int):
        self.__saude_at += efeito
    
    def afeta_ataque(self, efeito:int):
        self.__ataque_at += efeito

# expande as tecnicas

    def aprender_tecnica(self, novo: Acao):
        self.__tecnicas.append(novo)

# resetam os status e evoluem depois da batalha

    def fim_da_batalha(self, id_battle: int):
        self.__batalhas.append(id_battle)

        var = r.choice(['ataque', 'saude'])
        self.evoluir_atributo(var)

        self.__saude_at = self.__saude_max
        self.__ataque_at = self.__ataque_max

        var = r.choice(self.__tecnicas)
        self.evoluir_tecnica(var)

    
    def evoluir_tecnica(self, tecnica: Acao):
        if tecnica in self.__tecnicas:
            tecnica.evolucao()
        else: print("tecnica invalida")

    def evoluir_atributo(self, atributo: str):
        if atributo == 'ataque':
            self.__ataque_max += 5
        if atributo == 'saude':
            self.__saude_max += 5