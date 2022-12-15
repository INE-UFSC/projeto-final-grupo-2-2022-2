from Singleton.Singleton import Singleton

class Constantes(Singleton):
    __screenSize = (1200, 600)
    __defaultSize = (80, 80)

    __posicoesPersonagens = [
        (240, 180), (120, 300), (240, 420),
        (960, 180), (1080, 300), (960, 420)
    ]
    __posicoesSlots = [
        (400, 550), (450, 550), (500, 550), (550, 550),
        (600, 550), (650, 550), (700, 550), (750, 550)
    ]

    @property
    def posicoesPersonagens(cls) -> tuple:
        return cls.__posicoesPersonagens

    @property
    def posicoesSlots(cls) -> tuple:
        return cls.__posicoesSlots

    @property
    def screenSize(cls) -> tuple:
        return cls.__screenSize
    
    @property
    def defaultSize(cls) -> tuple:
        return cls.__defaultSize

    @property
    def locais(cls) -> list:
        return cls.__locais
