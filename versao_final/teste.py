from View.CenarioBatalha import CenarioBatalha
from Model.CenarioModel import CenarioModel
from Model.Personagem import Personagem
from Singleton.Constantes import Constantes
import random as r

classes = ['mago', 'orc', 'assassin', 'barbarian', 'goblin', 'knight']
inimigos = [None]*6
acoes = Constantes().skills

# --------------------------------------------------
# As imagens estão com _mirrored pra aparecerem viradas pros aliados
# --------------------------------------------------

inimigosFase1 = [
    Personagem('a', 1, acoes, 'goblin_mirrored'),
    Personagem('a', 1, acoes, 'goblin_mirrored'),
    Personagem('a', 1, acoes, 'goblin_mirrored')
]

inimigosFase2 = [
    Personagem('b', 2, acoes, 'goblin_mirrored'),
    Personagem('b', 2, acoes, 'troll_mirrored'),
    Personagem('b', 2, acoes, 'goblin_mirrored')
]

inimigosFase3 = [
    Personagem('b', 3, acoes, 'troll_mirrored'),
    Personagem('b', 3, acoes, 'goblin_mirrored'),
    Personagem('b', 3, acoes, 'orc_mirrored')
]

inimigosFase4 = [
    Personagem('b', 3, acoes, 'troll_mirrored'),
    Personagem('b', 3, acoes, 'orc_mirrored'),
    Personagem('b', 3, acoes, 'troll_mirrored')
]

inimigosFase5 = [
    Personagem('b', 4, acoes, 'orc_mirrored'),
    Personagem('b', 4, acoes, 'orc_mirrored'),
    Personagem('b', 4, acoes, 'orc_mirrored')
]

inimigosFase6 = [
    Personagem('b', 4, acoes, 'orc_mirrored'),
    Personagem('b', 4, acoes, 'mago_mirrored'),
    Personagem('b', 4, acoes, 'orc_mirrored')
]

reg1 = CenarioBatalha('regiao_1', 800, 500, 400, 600, 1, inimigosFase1)
reg2 = CenarioBatalha('regiao_2', 800, 500, 400, 500, 2, inimigosFase2)
reg3 = CenarioBatalha('regiao_3', 800, 500, 300, 500, 3, inimigosFase3)
reg4 = CenarioBatalha('regiao_4', 800, 500, 500, 500, 3, inimigosFase4)
reg5 = CenarioBatalha('regiao_5', 800, 500, 500, 400, 4, inimigosFase5)
reg6 = CenarioBatalha('regiao_6', 800, 500, 300, 300, 4, inimigosFase6)

cenario1 = CenarioModel(reg1, 431,148,75,83)
cenario1 = CenarioModel(reg2, 431,148,75,83)
cenario1 = CenarioModel(reg3, 431,148,75,83)
cenario1 = CenarioModel(reg4, 431,148,75,83)
cenario1 = CenarioModel(reg5, 431,148,75,83)
cenario1 = CenarioModel(reg6, 431,148,75,83)