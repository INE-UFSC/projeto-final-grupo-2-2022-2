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
        cond = cond and isinstance(char.ataque, int)
        cond = cond and isinstance(char.saude_max, int)
        cond = cond and isinstance(char.habilidades, list)
        tecnicas = {}
        while cond:
            for i in char.habilidades:
                cond = cond and isinstance(i, Habilidade)
                cond = cond and isinstance(i.nome, str)
                cond = cond and isinstance(i.fator, int)
                cond = cond and isinstance(i.efeito, int)
                cond = cond and isinstance(i.tipo, str)
                tecnicas[i.nome] = [i.nome,
                                 i.fator,
                                 i.efeito,
                                 i.tipo]
            valor = [char.ataque,
                    char.saude_max,
                    char.nivel,
                    char.classe,
                    char.posicao,
                    tecnicas]
            super().add(char.nome, valor)

    def get(self, nome:str) -> Personagem:
        j = deepcopy(self.__temp_get(nome))
        tecnicas = self.__get_tecnicas(nome)
        personagem = Personagem(j[3], j[2], tecnicas, j[4], nome)
        personagem.save_ataque(j[0], 'ataque_autorizado')
        personagem.save_saude_max(j[1], 'vida_autorizada')
        return personagem

    def remove(self, key:str):
        if isinstance(key, str):
            return super().remove(key)
        self.__get_tecnicas
    
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

# transforma os atributos de tecnicas salvas em Acao

    def __get_tecnicas(self, nome:str) -> list[Habilidade]:
        char = deepcopy(self.__temp_get(nome))
        temp_tecnicas = deepcopy(char[5])
        tecnicas = ['']*len(temp_tecnicas)
        j = 0
        for i in temp_tecnicas.values():
            tecnicas[j] = Habilidade(i[0], i[1], i[2], i[3])
            j += 1
        return tecnicas



