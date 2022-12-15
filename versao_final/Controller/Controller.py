from View.Menu import Menu
from Model.BatalhaModel import BatalhaModel
from DAO.JogoDAO import JogoDAO
from DAO.PersonagemDAO import PersonagemDAO
from View.BatalhaView import BatalhaView
from View.Tela import Tela
from Model.Mapa import Mapa
from Model.InputHandler import InputHandler
from Singleton.Animacao import Animacao
import pygame

class Controller:
    def __init__(self) -> None:
        self.__tela = Tela()
        self.__menu = Menu(self.__tela)
        self.__mapa = Mapa(self.__tela)
        self.__saveJogo = JogoDAO()
        self.__savePersonagens = PersonagemDAO()
        
    def savePersonagens(self):
        aliados = self.__batalhaModel.aliados

        for personagem in aliados:
            self.__savePersonagens.add(personagem)

    def setBatalha(self):
        self.__batalhaModel = BatalhaModel(self.__tela, self.__inimigos)
        self.__spritesAliados = pygame.sprite.Group([i.sprite for i in self.__batalhaModel.aliados])
        self.__spritesInimigos = pygame.sprite.Group([i.sprite for i in self.__batalhaModel.inimigos])
        self.__batalhaView = BatalhaView(self.__spritesAliados, 
                                         self.__spritesInimigos, 
                                         self.__batalhaModel.posicoesSlots,
                                         self.__tela)

    def rodaMenu(self):
        return self.__menu.run()
    
    def rodaMapa(self):
        self.__inimigos, self.__nivel, run = self.__mapa.inicia()
        if len(self.__inimigos) > 0:
            self.setBatalha()
            return run, True
        return run, False
    
    def rodaBatalha(self):
        inputHandler = InputHandler(self.__tela)
        run = inputHandler.handleScreenEvents()

        vencedor = self.__batalhaModel.checaVencedor()
        if vencedor != '':
            self.__batalhaView.mostraResultado(self.__tela.display, vencedor)
            self.__batalhaModel.reset()
            if vencedor == 'allies':
                self.__batalhaModel.evoluiAliados(self.__nivel + 1)
                self.__savePersonagens.add()
                self.__saveJogo.add(self.__nivel + 1)
            return run, True
        else:
            if Animacao().turnoJogador:
                posicaoMouse = inputHandler.handleClick()

                if not self.animacaoRodando():
                    self.checaClique(posicaoMouse)

            elif not self.animacaoRodando():
                skill = self.__batalhaModel.inimigoAtaca()
                self.__batalhaView.projetilInimigo = skill


            self.__batalhaView.draw(self.__batalhaModel.aliados, self.__batalhaModel.inimigos)
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
