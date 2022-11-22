from DAO import DAO
from Model.Personagem import Personagem

class JogoDAO(DAO):
    def __init__(self, datasource='Personagem'):
        super().__init__(datasource)

    def add(self, obj:Personagem):
        c1 = isinstance(obj, Personagem)
        c2 = c1 and isinstance(obj.nome, str)
        if not c2:
            return None
        return super().add(obj.nome, obj)

    def get(self, nome:str) -> Personagem:
        if isinstance(nome, str):
            return super().get(nome)

    def remove(self, key:str):
        if isinstance(key, str):
            return super().remove(key)