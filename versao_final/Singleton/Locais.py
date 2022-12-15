from Singleton.Singleton import Singleton
from Model.Personagem import Personagem
from Model.CenarioBatalha import CenarioBatalha
from Model.CenarioModel import CenarioModel
from Singleton.habilidades import Habilidades
from Model.Habilidade import Habilidade
import random as r

class Locais(Singleton):

    __acoes = Habilidades().skills
    
    __inimigosFase = [None]*6
    classes = ['goblin_mirrored', 'troll_mirrored',
               'orc_mirrored', 'mago_mirrored']

    for i in range(6):
        __inimigosFase[i] = [None]*3
        for j in range(3):
            k = r.randint(0, 3)
            __inimigosFase[i][j] = Personagem(classes[k], i+1, [Habilidade(*l) for l in __acoes])

    __reg1 = CenarioBatalha('background.png',
                            800, 500, 400, 600,
                            1, __inimigosFase[0])
    __reg2 = CenarioBatalha('background.png',
                            800, 500, 400, 500,
                            2, __inimigosFase[1])
    __reg3 = CenarioBatalha('background.png',
                            800, 500, 300, 500,
                            3, __inimigosFase[2])
    __reg4 = CenarioBatalha('background.png',
                            800, 500, 500, 500,
                            3, __inimigosFase[3])
    __reg5 = CenarioBatalha('background.png',
                            800, 500, 500, 400,
                            4, __inimigosFase[4])
    __reg6 = CenarioBatalha('background.png',
                            800, 500, 300, 300,
                            4, __inimigosFase[5])

    __locais = [
        CenarioModel(__reg1, 58,263,64,47),
        CenarioModel(__reg2, 360,264,67,80),
        CenarioModel(__reg3, 325,135,101,73),
        CenarioModel(__reg4, 362,427,64,45),
        CenarioModel(__reg5, 652,166,113,48),
        CenarioModel(__reg6, 657,245,102,73)
    ]
    
    @property
    def locais(cls):
        return cls.__locais
