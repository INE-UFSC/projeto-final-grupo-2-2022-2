from DAO.DAO import DAO
from Model.Personagem import Personagem
from Model.Habilidade import Habilidade
from copy import deepcopy

class PersonagemDAO(DAO):
    def __init__(self, datasource='Personagem.pkl'):
        super().__init__(datasource)

    def add(self, char:Personagem):
        cond = isinstance(char, Personagem)
        cond = cond and isinstance(char.nome, str)
        cond = cond and isinstance(char.classe, str)
        cond = cond and isinstance(char.nivel, int)
        cond = cond and isinstance(char.ataque_max, int)
        cond = cond and isinstance(char.saude_max, int)
        cond = cond and isinstance(char.tecnicas, list)
        tecnicas = {}
        while cond:
            for i in char.tecnicas:
                cond = cond and isinstance(i, Habilidade)
                cond = cond and isinstance(i.nome, str)
                cond = cond and isinstance(i.fator, int)
                tecnicas[i.nome] = [i.nome,
                                 i.fator,
                                 i.efeito,
                                 i.tipo,
                                 i.modo]
            valor = [char.ataque_max,
                    char.saude_max,
                    char.nivel,
                    char.classe,
                    tecnicas]
            super().add(char.nome, valor)

    def get(self, nome:str) -> Personagem:
        j = deepcopy(self.__temp_get(nome))
        tecnicas = self.__get_tecnicas(nome)
        personagem = Personagem(nome, j[2], tecnicas, j[3])
        personagem.save_ataque_max(j[0], 'pode usar')
        personagem.save_saude_max(j[1], 'pode usar')
        return personagem

    def remove(self, key:str):
        if isinstance(key, str):
            return super().remove(key)
        self.get_tecnicas
    
    def get_all(self) -> list[Personagem]:
        temp_dicio = deepcopy(super().get_all())
        personagens = [None]*len(temp_dicio)
        j = 0
        for i in temp_dicio.keys():
            personagens[j] = self.get(i)
            j += 1
        return personagens

    def __temp_get(self, nome:str) -> list[int, dict]:
        if isinstance(nome, str):
            return super().get(nome)
        print('erro de endereçamento')

# transforma os atributos de tecnicas salvas em Habilidade

    def __get_tecnicas(self, nome:str) -> list[Habilidade]:
        char = deepcopy(self.__temp_get(nome))
        temp_tecnicas = deepcopy(char[4])
        tecnicas = ['']*len(temp_tecnicas)
        j = 0
        for i in temp_tecnicas.values():
            tecnicas[j] = Habilidade(i[0], i[1], i[2], i[3], i[4])
            j += 1
        return tecnicas