from Model.Personagem import Personagem

import random as r

class Controller():
    def __init__(self) -> None:
        pass

    def checkForWinner(self,
                       aliados: list[Personagem],
                       inimigos: list[Personagem]) -> int:
        cont = 0
        for i in aliados:
            if i.get_saude() >= 0:
                cont += 1
        if cont == 0:
            return 0
        cont = 0
        for i in inimigos:
            if i.get_saude() >= 0:
                cont += 1
        if cont == 0:
            return 1
        
        return -1

    def selecionaPersonagem(self, alvos:list[Personagem]):
        alvo = r.choice(alvos)
        # Caso o alvo escolhido não tenha vida restante, tenta selecionar outro
        while alvo.get_saude() <= 0:
            alvo = r.choice(alvos)

        return alvo
    
    def selecionaHabilidade(self, personagem: Personagem):
        index = r.randint(0, len(personagem.tecnicas)-1)
        habilidade = personagem.get_acao(index)
        return habilidade
