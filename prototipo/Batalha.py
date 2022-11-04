from Personagem import Personagem
import random as r

# -*- coding: utf-8 -*-

class Batalha:

    def __init__(self, aliados:list[Personagem],
                 inimigos:list[Personagem]):
        self.__aliados = aliados
        self.__inimigos = inimigos

# para garantir que os dois times
# sempre tenham o mesmo tamanho
        while len(aliados) < len(self.__inimigos):
            self.__inimigos.pop()
        while len(aliados) > len(self.__inimigos):
            self.__inimigos.append(inimigos[0])

    def jogar_dados(self):
        return r.randint(1, 20)

# recebe o time que esta atacando e
# o que esta defendendo, decidindo 
# quem executa a ação e quem recebe,
# aleatoriamente, executa e checa se
# a saude chegou a 0 
    # def turno(self, executores:list[Personagem], alvos:list[Personagem]):
    #     atacante:Personagem = r.choice(executores)
    #     habilidade = atacante.get_acao()
    #     troca = False

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
    
    def batalhar(self):
        x = True
        y = True

        # enquanto os times mantém seus
        # integrantes com saude > 0,
        # turnos são alternados

        while x > 0 and y > 0:
            a = self.turno(self.__aliados,
                           self.__inimigos)
            self.__aliados, self.__inimigos = a

            a = self.turno(self.__inimigos,
                           self.__aliados)
            self.__inimigos, self.__aliados = a
    
            x = len(self.__aliados)
            y = len(self.__inimigos)

        if x:
            for i in self.__aliados:
                i.fim_da_batalha()
            return 'Vitoria!!!'
        # inimigos sobreviventes
        # não são recuperados
        return 'Hoje Não'