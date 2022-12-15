from Singleton.Singleton import Singleton
from Model.Personagem import Personagem
from Model.CenarioBatalha import CenarioBatalha
from Model.CenarioModel import CenarioModel
from Singleton.habilidades import Habilidades
from Model.Habilidade import Habilidade


class Locais(Singleton):

    __acoes = Habilidades().skills
    __inimigosFase1 = [
        Personagem('goblin_mirrored', 1, [Habilidade(*i) for i in __acoes]),
        Personagem('goblin_mirrored', 1, [Habilidade(*i) for i in __acoes]),
        Personagem('goblin_mirrored', 1, [Habilidade(*i) for i in __acoes])
    ]

    __inimigosFase2 = [
        Personagem('goblin_mirrored', 2, [Habilidade(*i) for i in __acoes]),
        Personagem('troll_mirrored', 2, [Habilidade(*i) for i in __acoes]),
        Personagem('goblin_mirrored', 2, [Habilidade(*i) for i in __acoes])
    ]

    __inimigosFase3 = [
        Personagem('troll_mirrored', 4, [Habilidade(*i) for i in __acoes]),
        Personagem('goblin_mirrored', 4, [Habilidade(*i) for i in __acoes]),
        Personagem('orc_mirrored', 4, [Habilidade(*i) for i in __acoes])
    ]

    __inimigosFase4 = [
        Personagem('troll_mirrored', 6, [Habilidade(*i) for i in __acoes]),
        Personagem('orc_mirrored', 6, [Habilidade(*i) for i in __acoes]),
        Personagem('troll_mirrored', 6, [Habilidade(*i) for i in __acoes])
    ]

    __inimigosFase5 = [
        Personagem('orc_mirrored', 9, [Habilidade(*i) for i in __acoes]),
        Personagem('orc_mirrored', 9, [Habilidade(*i) for i in __acoes]),
        Personagem('orc_mirrored', 9, [Habilidade(*i) for i in __acoes])
    ]

    __inimigosFase6 = [
        Personagem('orc_mirrored', 12, [Habilidade(*i) for i in __acoes]),
        Personagem('mago_mirrored', 12, [Habilidade(*i) for i in __acoes]),
        Personagem('orc_mirrored', 12, [Habilidade(*i) for i in __acoes]),
    ]

    __reg1 = CenarioBatalha('background.png',
                            800, 500, 400, 600,
                            1, __inimigosFase1)
    __reg2 = CenarioBatalha('background.png',
                            800, 500, 400, 500,
                            2, __inimigosFase2)
    __reg3 = CenarioBatalha('background.png',
                            800, 500, 300, 500,
                            5, __inimigosFase3)
    __reg4 = CenarioBatalha('background.png',
                            800, 500, 500, 500,
                            5, __inimigosFase4)
    __reg5 = CenarioBatalha('background.png',
                            800, 500, 500, 400,
                            8, __inimigosFase5)
    __reg6 = CenarioBatalha('background.png',
                            800, 500, 300, 300,
                            12, __inimigosFase6)

    __locais = [
        CenarioModel(__reg1, 76,393,88,73),
        CenarioModel(__reg2, 479,395,93,124),
        CenarioModel(__reg3, 432,203,138,111),
        CenarioModel(__reg4, 481,638,89,74),
        CenarioModel(__reg5, 869,248,152,74),
        CenarioModel(__reg6, 874,366,140,113)
    ]
    
    @property
    def locais(cls):
        return cls.__locais