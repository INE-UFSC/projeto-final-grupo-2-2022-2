class Singleton:
    __instance = None
    __screenSize = (1200, 600)
    __slotCounter = 0
    __charCounter = 0
    __skills = [
        ['fireball', -50, 'saude', 'ofensivo', 'projetil'],
        ['rasengan', -50, 'saude', 'ofensivo', 'projetil'],
        ['earthball', -50, 'saude', 'ofensivo', 'projetil'],
        ['waterball', -50, 'saude', 'ofensivo', 'projetil'],
        ['melee', -500, 'saude', 'ofensivo', 'melee'],
        ['boost', 5, 'ataque', 'suporte', 'projetil'],
        ]

    def __new__(cls, *args):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args)
        return cls.__instance
    
    @property
    def screenSize(cls):
        return cls.__screenSize
    @screenSize.setter
    def screenSize(cls, size):
        cls.__screenSize = size

    @property
    def slotCounter(cls):
        a = cls.__slotCounter
        cls.__slotCounter += 1
        if cls.__slotCounter >= 8:
            cls.__slotCounter = 0
        return a
    @slotCounter.setter
    def slotCounter(cls, count):
        cls.__slotCounter = count

    @property
    def charCounter(cls):
        a = cls.__charCounter
        cls.__charCounter += 1
        if cls.__charCounter > 5:
            cls.__charCounter = 0
        return a
    @charCounter.setter
    def charCounter(cls, count):
        cls.__charCounter = count

    @property
    def skills(cls):
        return cls.__skills