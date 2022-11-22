from Model.Personagem import Personagem
import random as r

# -*- coding: utf-8 -*-

class Batalha:

    def __init__(self, aliados:list[Personagem],
                 inimigos:list[Personagem]):
        self.__aliados = aliados
        self.__inimigos = inimigos

    def get_allies(self):
        return self.__aliados

    def get_enemies(self):
        return self.__inimigos

    def jogar_dados(self):
        return r.randint(1, 20)

# recebe o time que esta atacando e
# o que esta defendendo, decidindo
# quem executa a ação e quem recebe,
# aleatoriamente, executa e checa se
# a saude chegou a 0

    def turno(self, executores:list[Personagem],
                    alvos:list[Personagem]):

        atacante = r.choice(executores)
        habilidade = atacante.get_acao()
        
        troca = False
        if habilidade.tipo == 'suporte':
            executores, alvos = alvos, executores
            troca = True

        alvo = r.choice(alvos)
        habilidade.executar(alvo,
                            self.jogar_dados())

        if troca:
            return alvos, executores
        if alvo.get_saude() <= 0:
            alvos.remove(alvo)
            alvo.fim_da_batalha()
        return executores, alvos 
