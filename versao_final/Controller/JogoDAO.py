from DAO import DAO

class JogoDAO(DAO):
    def __init__(self, datasource='nivel'):
        super().__init__(datasource)

    def add(self, obj:int):
        c1 = isinstance(obj, int)
        if not c1:
            return None
        return super().add('nivel', obj)

    def get(self) -> int:
        return super().get('nivel')

    def remove(self, key:str):
        if isinstance(key, str):
            return super().remove(key)