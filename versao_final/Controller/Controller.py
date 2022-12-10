from View.Menu import Menu
from Model.BatalhaModel import BatalhaModel
from DAO.JogoDAO import JogoDAO
from DAO.PersonagemDAO import PersonagemDAO
from View.BatalhaView import BatalhaView
from Model.Tela import Tela
from Model.Mapa import Mapa
from Model.InputHandler import InputHandler
from Singleton.Animacao import Animacao
import pygame

class Controller:
    def __init__(self) -> None:
        self.__tela = Tela()
        self.__saveJogo = JogoDAO()
        self.__savePersonagens = PersonagemDAO()
        self.__menu = Menu()

        self.__batalhaModel = BatalhaModel(self.__tela.display)
        # self.__aliados = self.__savePersonagens.get_all()
        self.__aliados = self.__batalhaModel.aliados
        self.__inimigos = self.__batalhaModel.inimigos

        self.__spritesAliados = pygame.sprite.Group([i.sprite for i in self.__batalhaModel.aliados])
        self.__spritesInimigos = pygame.sprite.Group([i.sprite for i in self.__batalhaModel.inimigos])

        self.__batalhaView = BatalhaView(self.__spritesAliados, self.__spritesInimigos, self.__batalhaModel.posicoesSlots)
        
    def savePersonagens(self):
        aliados = self.__batalhaModel.aliados

        for personagem in aliados:
            self.__savePersonagens.add(personagem)

    def setBatalha(self):
        self.__batalhaModel = BatalhaModel(self.__aliados, self.__inimigos)
        self.__spritesAliados = pygame.sprite.Group([i.sprite for i in self.__batalhaModel.aliados])
        self.__spritesInimigos = pygame.sprite.Group([i.sprite for i in self.__batalhaModel.inimigos])
        self.__batalhaView = BatalhaView(self.__spritesAliados, self.__spritesInimigos, self.__tela.display)

    def rodaMenu(self):
        return self.__menu.run(self.__tela.display)
    
    def rodaMapa(self):
        mapa = Mapa(self.__tela.display)
        self.__inimigos, self.__nivel, run = mapa.inicia()
        # if self.__nivel != 0:
        #     self.setBatalha()
        return run
    
    def rodaBatalha(self):
        inputHandler = InputHandler(self.__tela.display)
        run = inputHandler.handleScreenEvents()

        vencedor = self.__batalhaModel.checaVencedor()
        if vencedor != '':
            self.__batalhaView.mostraResultado(self.__tela.display, vencedor)
            # if vencedor == 'allies':
            #     self.__saveJogo.add()
            return run, True
        else:
            if Animacao().turnoJogador:
                posicaoMouse = inputHandler.handleClick()

                if not self.animacaoRodando():
                    self.checaClique(posicaoMouse)

            elif not self.animacaoRodando():
                skill = self.__batalhaModel.inimigoAtaca()
                self.__batalhaView.projetilInimigo = skill


            self.__batalhaView.draw(self.__tela.display, self.__batalhaModel.aliados, self.__batalhaModel.inimigos)
            if self.__batalhaModel.habilidades is not None:
                self.__batalhaView.mostraHabilidades(self.__batalhaModel.habilidades)

            return run, False

    # Função do model batalha
    def checaClique(self, posicaoMouse:tuple[int]):
        habilidades = self.__batalhaModel.personagemClicado(posicaoMouse)
        if habilidades is not None:
            self.__batalhaView.mostraHabilidades(habilidades)
            return
        else:
            self.__batalhaModel.habilidadeClicada(posicaoMouse)
        
    def animacaoRodando(self):
        if not Animacao().finished:
            info = Animacao().info
            self.__batalhaModel.ataque(*info)
            return True
