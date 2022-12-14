from Singleton.Singleton import Singleton
from Model.Personagem import Personagem
from Model.CenarioBatalha import CenarioBatalha
from Model.CenarioModel import CenarioModel
from Singleton.habilidades import Habilidades
from Model.Habilidade import Habilidade


# classes = ['mago', 'assassin', 'goblin']
# classes_I = ['mago_mirrored',
#              'orc_mirrored',
#              'goblin_mirrored',
#              'troll_mirrored']

# save_aliados = PersonagemDAO('Aliados.pkl')
# aliados = [None]*3
# inimigos = [None]*6

# for i in range(3):
#     aliados[i] = Personagem(classes[i], 1,
#                 [Habilidade(*i) for i in Habilidades().skills[0:2]],
#                 Constantes().posicoesPersonagens[i],
#                 'Joao' + str(i))
#     save_aliados.add(aliados[i])

#     for nivel in range(6):
#         inimigos[nivel] = [None]*3
#         inimigos[nivel][i] = Personagem(classes_I[i], nivel,
#                     [Habilidade(*i) for i in Habilidades(
#                         ).skills[0:2]],
#                     Constantes().posicoesPersonagens[i+3],
#                     'Inimigo' + str(nivel) + str(i))

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
        Personagem('troll_mirrored', 3, [Habilidade(*i) for i in __acoes]),
        Personagem('goblin_mirrored', 3, [Habilidade(*i) for i in __acoes]),
        Personagem('orc_mirrored', 3, [Habilidade(*i) for i in __acoes])
    ]

    __inimigosFase4 = [
        Personagem('troll_mirrored', 3, [Habilidade(*i) for i in __acoes]),
        Personagem('orc_mirrored', 3, [Habilidade(*i) for i in __acoes]),
        Personagem('troll_mirrored', 3, [Habilidade(*i) for i in __acoes])
    ]

    __inimigosFase5 = [
        Personagem('orc_mirrored', 3, [Habilidade(*i) for i in __acoes]),
        Personagem('orc_mirrored', 3, [Habilidade(*i) for i in __acoes]),
        Personagem('orc_mirrored', 3, [Habilidade(*i) for i in __acoes])
    ]

    __inimigosFase6 = [
        Personagem('orc_mirrored', 3, [Habilidade(*i) for i in __acoes]),
        Personagem('mago_mirrored', 3, [Habilidade(*i) for i in __acoes]),
        Personagem('orc_mirrored', 3, [Habilidade(*i) for i in __acoes]),
    ]

    __reg1 = CenarioBatalha('background.png',
                            800, 500, 400, 600,
                            1, __inimigosFase1)
    __reg2 = CenarioBatalha('background.png',
                            800, 500, 400, 500,
                            2, __inimigosFase2)
    __reg3 = CenarioBatalha('background.png',
                            800, 500, 300, 500,
                            3, __inimigosFase3)
    __reg4 = CenarioBatalha('background.png',
                            800, 500, 500, 500,
                            3, __inimigosFase4)
    __reg5 = CenarioBatalha('background.png',
                            800, 500, 500, 400,
                            4, __inimigosFase5)
    __reg6 = CenarioBatalha('background.png',
                            800, 500, 300, 300,
                            4, __inimigosFase6)

    __locais = [
        CenarioModel(__reg1, 40,200,65,60),
        CenarioModel(__reg2, 348,200,69,100),
        CenarioModel(__reg3, 312,48,104,89),
        CenarioModel(__reg4, 349,399,67,57),
        CenarioModel(__reg5, 349,533,64,57),
        CenarioModel(__reg6, 643,85,113,59)
    ]
    
    @property
    def locais(cls):
        return cls.__locais