from Singleton.Singleton import Singleton
from Model.Acao import Acao

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
    
    def __init__(self):
        pass
    
    @property
    def screenSize(cls):
        return cls.__screenSize
    @screenSize.setter
    def screenSize(cls, size):
        cls.__screenSize = size

    @property
    def skills(cls):
        return cls.__skills

    