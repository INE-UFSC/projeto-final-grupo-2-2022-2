from abc import ABC, abstractmethod
import pickle

class DAO(ABC):
    def __init__(self, datasource=''):
        self.__datasource = datasource
        self.__cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))

    def __load(self):
        self.__cache = pickle.load(open(self.__datasource, 'rb'))

    @abstractmethod
    def add(self, key, obj):
        if key in self.__cache.keys():
            print('Já adicionado!!!')
            return None
        self.__cache[key] = obj
        self.__dump()

    @abstractmethod
    def get(self, key):
        try:
            return self.__cache[key]
        except KeyError:
            return None

    @abstractmethod
    def remove(self, key):
        try:
            self.__cache.pop(key)
            self.__dump()
        except KeyError:
            return None

    def get_all(self):
        return self.__cache.values()