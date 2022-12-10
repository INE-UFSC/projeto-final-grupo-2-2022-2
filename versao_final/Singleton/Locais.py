from Singleton.Singleton import Singleton
from Model.Personagem import Personagem
from DAO.PersonagemDAO import inimigos
from Model.CenarioBatalha import CenarioBatalha
from Model.CenarioModel import CenarioModel

class Locais(Singleton):
    __reg1 = CenarioBatalha('background.png',
                            800, 500, 400, 600,
                            1, inimigos[0])
    __reg2 = CenarioBatalha('background.png',
                            800, 500, 400, 500,
                            2, inimigos[1])
    __reg3 = CenarioBatalha('background.png',
                            800, 500, 300, 500,
                            3, inimigos[2])
    __reg4 = CenarioBatalha('background.png',
                            800, 500, 500, 500,
                            3, inimigos[3])
    __reg5 = CenarioBatalha('background.png',
                            800, 500, 500, 400,
                            4, inimigos[4])
    __reg6 = CenarioBatalha('background.png',
                            800, 500, 300, 300,
                            4, inimigos[5])

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