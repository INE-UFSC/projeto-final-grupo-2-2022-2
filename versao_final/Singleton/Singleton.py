from abc import ABC

class Singleton(ABC):
    __instance = None

    def __new__(cls, *args):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls,
                                            *args)
        return cls.__instance
