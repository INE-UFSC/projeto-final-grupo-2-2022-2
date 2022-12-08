from Singleton.Singleton import Singleton
from Model.Acao import Acao
from Model.Personagem import Personagem
from View.CenarioBatalha import CenarioBatalha
from Model.CenarioModel import CenarioModel

class Constantes(Singleton):
    __instance = None
    __screenSize = (1200, 600)
    __defaultSize = (80, 80)
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
        id = "Saffron" + str(i) + ".jpg"
        __locais[i] = CenarioModel(CenarioBatalha(id, 800,500,
                                                  400,250, i),
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
    def defaultSize(cls) -> tuple(int):
        return cls.__defaultSize
    @defaultSize.setter
    def screenSize(cls, size):
        cls.__defaultSize = size

    @property
    def skills(cls) -> Acao:
        return cls.__skills

    @property
    def locais(cls) -> list[CenarioModel]:
        return cls.__locais



acoes = Constantes().skills

aliados = [None]*3

for i in range(3):
    aliados[i] = Personagem(nome = 'Joao' + str(i), 
                          nivel = 1,
                          tecnicas = [acoes[i-1], acoes[i]], 
                          classe = 'mago')
    