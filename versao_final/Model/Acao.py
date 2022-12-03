# cada acao deve ter um nome, um fator
# (quanto vai afetar, capaz de evoluir)
# efeitos, consistindo em qual atributo
# (saude ou ataque) ela vai afetar e
# o tipo (ofensivo ou suporte)

from Model.Personagem import Personagem
from View.Sprite import Sprite

class Acao:
    def __init__(self, nome:str, fator: int,
                efeito:str, tipo:str):
        self.__nome = nome
        self.__fator = fator
        self.__tipo = tipo
        self.__efeito = efeito.lower()

    def evolucao(self):
        if self.__fator > 0:
            self.__fator += 5
        else:
            self.__fator -= 5
    
    def animation(self, 
                 atacante:Sprite, 
                 alvo:Sprite, 
                 habilidade:Sprite, 
                 atacantePos: int, 
                 alvoPos: int):
        y_speed = 0
        x_speed = 5

        # print(alvoPos)

        if atacante.rect.x > alvo.rect.x:
            x_speed = -x_speed

        if atacantePos == alvoPos:
            y_speed = 0
            # print('a')
        elif atacantePos > alvoPos:
            if atacantePos - alvoPos == 2:
                y_speed = -2
                # print('b')
            else:
                y_speed = -1
                # print('c')
        else:
            if alvoPos - atacantePos == 2:
                y_speed = 2
                # print('d')
            else:
                y_speed = 1        

        habilidade.rect.x += x_speed
        habilidade.rect.y += y_speed
        
        if habilidade.rect.collidepoint(alvo.rect.center):
            return True, habilidade

        return False, habilidade
        


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
    
    @fator.setter
    def fator(self, novo:int):
        self.__fator = novo


    @property
    def efeito(self):
        return self.__efeito

    @efeito.setter
    def efeito(self, novo:str):
        self.__efeito = novo
    
    def executar(self, alvo:Personagem, dado:int):
        c = (self.__fator*(dado/20))//1
        if self.__efeito == 'saude':
            alvo.afeta_saude(c)
        elif self.__efeito == 'ataque':
            alvo.afeta_ataque(c)
        else: print('efeito invalido')