from Model.Acao import Acao

class Singleton:
    __instance = None
    __screenSize = (1200, 600)
    __skills = [
        Acao('fireball', -200, 'saude', 'ofensivo'),
        Acao('rasengan', -200, 'saude', 'ofensivo'),
        Acao('earthball', -200, 'saude', 'ofensivo'),
        Acao('waterball', -200, 'saude', 'ofensivo'),
        # Acao('boost', 5, 'ataque', 'suporte')
        ]

    def __new__(cls, *args):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args)
        return cls.__instance
    
    @property
    def screenSize(cls):
        return cls.__screenSize
    @screenSize.setter
    def screenSize(cls, size):
        cls.__screenSize = size

    @property
    def skills(cls):
        return cls.__skills