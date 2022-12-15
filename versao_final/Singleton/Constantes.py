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
    def posicoesPersonagens(cls) -> tuple[int]:
        return cls.__posicoesPersonagens

    @property
    def posicoesSlots(cls) -> tuple[int]:
        return cls.__posicoesSlots

    @property
    def screenSize(cls) -> tuple[int]:
        return cls.__screenSize
    
    @property
    def defaultSize(cls) -> tuple[int]:
        return cls.__defaultSize

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

    @property
    def locais(cls) -> list:
        return cls.__locais
