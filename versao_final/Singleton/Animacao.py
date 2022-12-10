from Singleton import Singleton

class Animacao(Singleton):
    __fase = 0
    __finished = True

    __atacante = None
    __alvo = None
    __index = None

    __turnoJogador = True

    def inicia(cls,
               atacante=None,
               alvo=None,
               index=None):
        cls.__atacante = atacante
        cls.__alvo = alvo
        cls.__index = index
        cls.__finished = False
        

    @property
    def fase(cls):
        return cls.__fase
    @fase.setter
    def fase(cls, new:int):
        cls.__fase = new

    @property
    def finished(cls):
        return cls.__finished
    @finished.setter
    def finished(cls, new:int):
        cls.__finished = new
        cls.__turnoJogador = not cls.__turnoJogador
    
    @property
    def info(cls):
        return [cls.__atacante, cls.__alvo, cls.__index]

    @property
    def turnoJogador(cls):
        return cls.__turnoJogador
    