from Singleton.Singleton import Singleton
from Model.Acao import Acao
from Model.Personagem import Personagem
from View.CenarioBatalha import CenarioBatalha
from Model.CenarioModel import CenarioModel
from Controller.PersonagemDAO import PersonagemDAO
from Controller.JogoDAO import JogoDAO

class Constantes(Singleton):
    __screenSize = (1200, 600)
    __defaultSize = (80, 80)
    __slotCounter = 0
    __charCounter = 0
    __SaveNivel = JogoDAO('Nivel.pkl')
    __SavePersonagens = JogoDAO('Nivel.pkl')
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
    def slotCounter(cls) -> int:
        a = cls.__slotCounter
        cls.__slotCounter += 1
        if cls.__slotCounter >= 8:
            cls.__slotCounter = 0
        return a
    @slotCounter.setter
    def slotCounter(cls, count: int):
        cls.__slotCounter = count

    @property
    def charCounter(cls) -> int:
        a = cls.__charCounter
        cls.__charCounter += 1
        if cls.__charCounter > 5:
            cls.__charCounter = 0
        return a
    @charCounter.setter
    def charCounter(cls, count:int):
        cls.__charCounter = count

    @property
    def skills(cls) -> Acao:
        return cls.__skills

    @property
    def SaveNivel(cls) -> JogoDAO:
        return cls.__SaveNivel

    @property
    def SavePersonagens(cls) -> PersonagemDAO:
        return cls.__SavePersonagens

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
    Constantes().SavePersonagens.add(aliados[i])