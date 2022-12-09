from Menu import Menu
from Model.MapaModel import MapaModel
from Model.BatalhaModel import BatalhaModel
from DAO.JogoDAO import JogoDAO
from DAO.PersonagemDAO import PersonagemDAO
from View.BatalhaView import BatalhaView
from Tela import Tela
from InputHandler import InputHandler
from Animacao import Animacao
import pygame

class Controller:
    def __init__(self) -> None:
        self.__tela = Tela()
        self.__saveJogo = JogoDAO()
        self.__savePersonagens = PersonagemDAO()
        
        self.__batalhaModel = BatalhaModel()

        self.__spritesAliados = pygame.sprite.Group([i.sprite for i in self.__batalhaModel.aliados])
        self.__spritesInimigos = pygame.sprite.Group([i.sprite for i in self.__batalhaModel.inimigos])

        posicoes = self.__batalhaModel.posicoesSlots

        self.__batalhaView = BatalhaView(self.__spritesAliados, self.__spritesInimigos, posicoes)


    def rodaMenu(self):
        menu = Menu()
        menu.inicia()
    
    def rodaMapa(self):
        mapa = MapaModel()
        mapa.inicia()
    
    def rodaBatalha(self):
        vencedor = self.__batalhaModel.checaVencedor()
        if self.__batalhaModel.checaVencedor() != '':
            self.__batalhaView.mostraResultado(self.__tela.display, vencedor)

        inputHandler = InputHandler(self.__tela.display)
        run = inputHandler.handleScreenEvents()


        if Animacao().turnoJogador:
            posicaoMouse = inputHandler.handleClick()

            if not self.animacaoRodando():
                self.checaClique(posicaoMouse)

        elif not self.animacaoRodando():
            self.__batalhaModel.inimigoAtaca()


        self.__batalhaView.draw(self.__tela.display, self.__batalhaModel.aliados, self.__batalhaModel.inimigos)
        if self.__batalhaModel.habilidades is not None:
            self.__batalhaView.mostraHabilidades(self.__batalhaModel.habilidades)

        return run

    # Função do model batalha
    def checaClique(self, posicao:tuple[int]):
        habilidades = self.__batalhaModel.personagemClicado(posicao)
        if habilidades is not None:
            self.__batalhaView.mostraHabilidades(habilidades)
            return
        else:
            self.__batalhaModel.habilidadeClicada(posicao)
        
    def animacaoRodando(self):
        if not Animacao().finished:
            info = Animacao().info
            self.__batalhaModel.ataque(*info)
            # self.__batalhaModel.resetaPersonagens()
            return True
