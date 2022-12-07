from Singleton.Singleton import Singleton
from Model.Acao import Acao
from View.CenarioBatalha import CenarioBatalha
from Model.CenarioModel import CenarioModel

class Constantes(Singleton):
    __instance = None
    __screenSize = (1200, 600)
    __skills = [
        Acao('fireball', -50, 'saude', 'ofensivo', 'projetil'),
        Acao('rasengan', -50, 'saude', 'ofensivo', 'projetil'),
        Acao('earthball', -50, 'saude', 'ofensivo', 'projetil'),
        Acao('waterball', -50, 'saude', 'ofensivo', 'projetil'),
        Acao('melee', -500, 'saude', 'ofensivo', 'melee'),
        Acao('boost', 5, 'ataque', 'suporte', 'projetil')
        ]
    __locais = [None]*10
    for i in range(10):
        __locais[i] = CenarioModel(CenarioBatalha("Saffron.jpg",
                                            800,500,400,250, i),
                                            431,148,75,83)
    
    def __init__(self):
        pass
    
    @property
    def screenSize(cls) -> tuple(int):
        return cls.__screenSize
    @screenSize.setter
    def screenSize(cls, size):
        cls.__screenSize = size

    @property
    def skills(cls) -> Acao:
        return cls.__skills

    @property
    def locais(cls) -> list[CenarioModel]:
        return cls.__locais

    