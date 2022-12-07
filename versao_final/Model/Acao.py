# cada acao deve ter um nome, um fator
# (quanto vai afetar, capaz de evoluir)
# efeitos, consistindo em qual atributo
# (saude ou ataque) ela vai afetar e
# o tipo (ofensivo ou suporte)

import random as r
class Acao:
    def __init__(self, nome:str, fator: int,
                efeito:str, tipo:str, modo: str):
        self.__nome = nome
        self.__fator = fator
        self.__tipo = tipo
        self.__efeito = efeito.lower()
        self.__modo = modo

    def evolucao(self):
        if self.__fator > 0:
            self.__fator += 5
        else:
            self.__fator -= 5

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, novo:str):
        self.__nome = novo


    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self, novo:str):
        self.__tipo = novo


    @property
    def fator(self):
        return self.__fator


    @property
    def efeito(self):
        return self.__efeito
    @efeito.setter
    def efeito(self, novo:str):
        self.__efeito = novo

    @property
    def modo(self):
        return self.__modo
    @modo.setter
    def modo(self, novo:str):
        self.__modo = novo
    
    def executar(self, alvo):
        dado = r.randint(1, 20)
        c = (self.__fator*(dado/20))//1
        if self.__efeito == 'saude':
            alvo.afeta_saude(c)
        elif self.__efeito == 'ataque':
            alvo.afeta_ataque(c)
        else: print('efeito invalido')