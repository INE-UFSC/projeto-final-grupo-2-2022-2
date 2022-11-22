from Controller.DAO import DAO
from View.PersonagemView import PersonagemView

class JogoDAO(DAO):
    def __init__(self, datasource=''):
        super().__init__(datasource)

    def add(self, obj:PersonagemView):
        c1 = isinstance(obj, PersonagemView)
        c2 = c1 and isinstance(obj.nome, str)
        if not c2:
            return None
        return super().add(obj.nome, obj)

    def get(self, nome:str) -> PersonagemView:
        if isinstance(nome, str):
            return super().get(nome)

    def remove(self, key:str):
        if isinstance(key, str):
            return super().remove(key)