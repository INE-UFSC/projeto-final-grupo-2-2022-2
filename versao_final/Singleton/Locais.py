from Singleton.Singleton import Singleton
from Model.Personagem import Personagem
from Singleton.habilidades import Habilidades
from Model.CenarioBatalha import CenarioBatalha
from Model.CenarioModel import CenarioModel

class Locais(Singleton):
    __acoes = Habilidades().skills
    __inimigosFase1 = [
        Personagem('goblin_mirrored', 1, __acoes),
        Personagem('goblin_mirrored', 1, __acoes),
        Personagem('goblin_mirrored', 1, __acoes)
    ]

    __inimigosFase2 = [
        Personagem('goblin_mirrored', 2, __acoes),
        Personagem('troll_mirrored', 2, __acoes),
        Personagem('goblin_mirrored', 2, __acoes)
    ]

    __inimigosFase3 = [
        Personagem('troll_mirrored', 3, __acoes),
        Personagem('goblin_mirrored', 3, __acoes),
        Personagem('orc_mirrored', 3, __acoes)
    ]

    __inimigosFase4 = [
        Personagem('troll_mirrored', 3, __acoes),
        Personagem('orc_mirrored', 3, __acoes),
        Personagem('troll_mirrored', 3, __acoes)
    ]

    __inimigosFase5 = [
        Personagem('orc_mirrored', 3, __acoes),
        Personagem('orc_mirrored', 3, __acoes),
        Personagem('orc_mirrored', 3, __acoes)
    ]

    __inimigosFase6 = [
        Personagem('orc_mirrored', 3, __acoes),
        Personagem('mago_mirrored', 3, __acoes),
        Personagem('orc_mirrored', 3, __acoes),
    ]

    __reg1 = CenarioBatalha('background.png', 800, 500, 400, 600, 1, __inimigosFase1)
    __reg2 = CenarioBatalha('background.png', 800, 500, 400, 500, 2, __inimigosFase2)
    __reg3 = CenarioBatalha('background.png', 800, 500, 300, 500, 3, __inimigosFase3)
    __reg4 = CenarioBatalha('background.png', 800, 500, 500, 500, 3, __inimigosFase4)
    __reg5 = CenarioBatalha('background.png', 800, 500, 500, 400, 4, __inimigosFase5)
    __reg6 = CenarioBatalha('background.png', 800, 500, 300, 300, 4, __inimigosFase6)

    __locais = [
        CenarioModel(__reg1, 431,148,75,83),
        CenarioModel(__reg2, 431,148,75,83),
        CenarioModel(__reg3, 431,148,75,83),
        CenarioModel(__reg4, 431,148,75,83),
        CenarioModel(__reg5, 431,148,75,83),
        CenarioModel(__reg6, 431,148,75,83)
    ]
    
    @property
    def locais(cls):
        return cls.__locais