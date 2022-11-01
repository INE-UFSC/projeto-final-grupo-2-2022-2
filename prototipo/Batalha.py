from Jogo import Jogo
from Acao import Acao
from Cenario import Cenario
from Jogador import Jogador
from Personagem import Personagem
import random as r

class Batalha:

    def __init__(self, aliados:list(Personagem), inimigos:list(Personagem)):
        self.__aliados = aliados
        self.__inimigos = inimigos
        self.__L = len(aliados)
        i = 0
        while self.__L > len(self.__inimigos):
            h = inimigos[i]
            self.__inimigos.append(h)
            i += 1

    def jogar_dados(self):
        return r.randint(1, 20)

    def turno(self, i:int, executor:list(Personagem), alvo:list(Personagem)):
        a = r.choice(executor)
        c = a.get_acao()
        troca = False
        if c.tipo == 'suporte':
            executor, alvo = alvo, executor
            troca = True
        b = r.choice(alvo)
        c.executar(b)
        if troca:
            return alvo, executor
        else:
            if b.get_saude() <= 0:
                alvo.remove(b)
            return executor, alvo 
    
    def batalhar(self):
        x = True
        y = True
        origem_a = self.__aliados
        origem_b = self.__inimigos
        while x and y:
            self.__aliados, self.__inimigos = self.turno(self.__aliados,
                                                         self.__inimigos)
            self.__inimigos, self.__aliados = self.turno(self.__inimigos,
                                                         self.__aliados)
            x = len(self.__aliados) > 0
            y = len(self.__inimigos) > 0

        if x:
            print('Vitoria!!!')
        else: print('Hoje Não')

        for i in range(self.__L):
            origem_a[i].fim_da_batalha()
            origem_b[i].fim_da_batalha()