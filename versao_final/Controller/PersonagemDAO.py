from DAO import DAO
from Model.Personagem import Personagem
from Model.Acao import Acao

class PersonagemDAO(DAO):
    def __init__(self, datasource='Personagem.pkl'):
        super().__init__(datasource)

    def add(self, obj:Personagem):
        c0 = isinstance(obj, Personagem)
        c1 = c0 and isinstance(obj.ataque, int)
        c2 = c1 and isinstance(obj.saude, int)
        c3 = c2 and isinstance(obj.nome, str)
        c4 = c3 and isinstance(obj.tecnicas, list)
        for i in obj.tecnicas:
            c5 = c4 and isinstance(i, Acao)
        c6 = False
        if c5:
            lista = [i.fator for i in obj.tecnicas]
            for i in lista:
                c6 = c5 and isinstance(i, int)
        if not c6:
            return None
        lista = [obj.ataque, obj.saude].extend(lista)
        return super().add(obj.nome, lista)

    def get(self, nome:str) -> list[int]:
        if isinstance(nome, str):
            return super().get(nome)

    def remove(self, key:str):
        if isinstance(key, str):
            return super().remove(key)