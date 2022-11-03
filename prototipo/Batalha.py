from Jogo import Jogo
from Acao import Acao
from Cenario import Cenario
from Jogador import Jogador
from Personagem import Personagem
import random as r

class Batalha:

    def __init__(self, aliados:list[Personagem], inimigos:list[Personagem]):
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

    def turno(self):#, executores:list[Personagem], alvos:list[Personagem]):
        atacante:Personagem = r.choice(self.__aliados)
        habilidade = atacante.get_acao()
        troca = False

        if habilidade.tipo == 'suporte':
            self.__aliados, self.__inimigos = self.__inimigos, self.__aliados
            troca = True

        alvo = r.choice(self.__inimigos)
        habilidade.executar(alvo)
        if troca:
            return self.__inimigos, self.__aliados
        else:
            if alvo.get_saude() <= 0:
                self.__inimigos.remove(alvo)
            return self.__aliados, self.__inimigos 
    
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

        if x and not y:
            print('Vitoria!!!')
        else: 
            print('Hoje Não')

        for i in range(len(origem_a)):
            origem_a[i].fim_da_batalha()
        for i in range(len(origem_b)):
            origem_b[i].fim_da_batalha()