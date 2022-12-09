from Controller.DAO import DAO
from Model.Personagem import Personagem
from Model.Acao import Acao
from copy import deepcopy

class PersonagemDAO(DAO):
    def __init__(self, datasource='Personagem.pkl'):
        super().__init__(datasource)

    def add(self, char:Personagem):
        cond = isinstance(char, Personagem)
        cond = cond and isinstance(char.nome, str)
        cond = cond and isinstance(char.ataque_max, int)
        cond = cond and isinstance(char.saude_max, int)
        cond = cond and isinstance(char.tecnicas, list)
        tecnicas = [i for i in char.tecnicas]
        dicio = {}
        while cond:
            for i in tecnicas:
                cond = cond and isinstance(i, Acao)
                cond = cond and isinstance(i.nome, str)
                cond = cond and isinstance(i.fator, int)
                dicio[i.nome] = [i.nome,
                                 i.fator,
                                 i.efeito,
                                 i.tipo,
                                 i.modo]
            valor = [char.ataque_max,
                    char.saude_max,
                    dicio]
            super().add(char.nome, valor)

    def get(self, nome:str) -> list[dict]:
        if isinstance(nome, str):
            return super().get(nome)
        print('erro de endereçamento')

    def remove(self, key:str):
        if isinstance(key, str):
            return super().remove(key)
        self.get_tecnicas

    def get_ataque(self, nome:str) -> int:
        char = self.get(nome)
        return char[0]

    def get_saude(self, nome:str) -> int:
        char = self.get(nome)
        return char[1]

# transforma os atributos de tecnicas salvas em Acao

    def __get_temp_tecnicas(self, nome:str) -> dict[list]:
        char = deepcopy(self.get(nome))
        return deepcopy(char[2])

    def get_tecnicas(self, nome:str) -> dict(Acao):
        temp_tecnicas = self.__get_temp_tecnicas(nome)
        tecnicas = {}
        for i in temp_tecnicas.values():
            tecnicas[i[0]] = Acao(i[0], i[1], i[2], i[3], i[4])
        return tecnicas