from Personagem import Personagem
from Animacao import Animacao
from Sprite import Sprite
from habilidades import Habilidades
import random as random

class BatalhaModel:
    def __init__(self) -> None:

        self.__skillsAliados = Habilidades().skillsAliados
        self.__skillsInimigos = Habilidades().skillsInimigos

        self.__personagemSelecionado = None

        self.__posicoesPersonagens = [
            (240, 180), (120, 300), (240, 420),
            (960, 180), (1080, 300), (960, 420)
        ]
        self.__posicoesSlots = [
            (400, 550), (450, 550), (500, 550), (550, 550),
            (600, 550), (650, 550), (700, 550), (750, 550)
        ]

        self.__aliados = [
            Personagem('mago', 1, self.__skillsAliados[0:2].copy(), self.__posicoesPersonagens[0]),
            Personagem('assassin', 1, self.__skillsAliados[1:3].copy(), self.__posicoesPersonagens[1]),
            Personagem('goblin', 1, self.__skillsAliados[2:4].copy(), self.__posicoesPersonagens[2])
        ]

        self.__inimigos = [
            Personagem('mago', 1, self.__skillsInimigos[0:2].copy(), self.__posicoesPersonagens[3]),
            Personagem('assassin', 1, self.__skillsInimigos[1:3].copy(), self.__posicoesPersonagens[4]),
            Personagem('goblin', 1, self.__skillsInimigos[2:4].copy(), self.__posicoesPersonagens[5])
        ]

        self.__setPosicoes()

        self.__spritesAliados = [i.sprite for i in self.__aliados]
        self.__spritesInimigos = [i.sprite for i in self.__inimigos]
        self.__habilidades: list[Sprite] = []

    def __setPosicoes(self):
        print('b')
        i = 0
        for aliado in self.__aliados:
            aliado.posicao = self.__posicoesPersonagens[i]
            i += 1
        for inimigo in self.__inimigos:
            inimigo.posicao = self.__posicoesPersonagens[i]
            i += 1
        
    def ataque(self, atacante: Personagem, alvo: Personagem, index: int):
        dano = atacante.atacar(index, alvo.sprite.posicao)
        if Animacao().fase == 2:
            alvo.defender(dano)
    
    def inimigoAtaca(self):
        atacante = self.selecionaPersonagem(self.__inimigos)
        alvo = self.selecionaPersonagem(self.__aliados)
        index = random.randint(0, len(atacante.habilidades)-1)
        Animacao().inicia(atacante, alvo, index)
        self.ataque(atacante, alvo, index)

    def checaVencedor(self):
        cont = 0
        for aliado in self.__aliados:
            if aliado.saude > 0:
                cont += 1
        if cont == 0:
            return 'enemies'
        cont = 0
        for inimigo in self.__inimigos:
            if inimigo.saude > 0:
                cont += 1
        if cont == 0:
            return 'allies'
        
        return ''


    def selecionaPersonagem(self, personagens: list[Personagem]):
        personagem = random.choice(personagens)
        while personagem.saude <= 0:
            personagem = random.choice(personagens)
        
        return personagem
    
    # controller?
    def personagemClicado(self, posicao:list[int]):
        for index, aliado in enumerate(self.__spritesAliados):
            if posicao is not None and aliado.rect.collidepoint(posicao) and self.__aliados[index].saude > 0:
                self.__personagemSelecionado = self.__aliados[index]
                print(self.__personagemSelecionado.posicao)
                habilidades = self.__aliados[index].habilidades
                habilidades = [i.projetil for i in habilidades]
                self.__habilidades = habilidades
                return habilidades
        
    # controller?
    def habilidadeClicada(self, posicao:list[int]):
        for index, sprite in enumerate(self.__habilidades):
            if posicao is not None and sprite.rect.collidepoint(posicao):
                alvo = self.selecionaPersonagem(self.__inimigos)
                if self.__personagemSelecionado.saude > 0:
                    Animacao().inicia(self.__personagemSelecionado, alvo, index)
                    self.ataque(self.__personagemSelecionado, alvo, index)


    def resetaPersonagens(self):
        self.__aliados = [
            Personagem('mago', 1, self.__skillsAliados[0:2].copy(), self.__posicoesPersonagens[0]),
            Personagem('assassin', 1, self.__skillsAliados[1:3].copy(), self.__posicoesPersonagens[1]),
            Personagem('goblin', 1, self.__skillsAliados[2:4].copy(), self.__posicoesPersonagens[2])
        ]

        self.__inimigos = [
            Personagem('mago', 1, self.__skillsInimigos[:].copy(), self.__posicoesPersonagens[3]),
            Personagem('assassin', 1, self.__skillsInimigos[:].copy(), self.__posicoesPersonagens[4]),
            Personagem('goblin', 1, self.__skillsInimigos[:].copy(), self.__posicoesPersonagens[5])
        ]

    
    @property
    def posicoesSlots(self):
        return self.__posicoesSlots
    
    @property
    def posicoesPersonagens(self):
        return self.__posicoesPersonagens
    
    @property
    def aliados(self):
        return self.__aliados
    
    @property
    def inimigos(self):
        return self.__inimigos

    @property
    def habilidades(self):
        if self.__personagemSelecionado is not None:
            skills = [i.projetil for i in self.__personagemSelecionado.habilidades]
            return skills
