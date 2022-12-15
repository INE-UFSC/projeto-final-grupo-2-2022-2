from DAO.DAO import DAO

class JogoDAO(DAO):
    def __init__(self, datasource='Nivel.pkl'):
        super().__init__(datasource)

    def add(self, nivel:int):
        if isinstance(nivel, int):
            return super().add('fase', nivel)

    def get(self) -> int:
        return super().get('fase')

    def remove(self):
        return super().remove('fase')