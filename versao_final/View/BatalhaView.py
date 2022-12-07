import pygame
from Model.Personagem import Personagem
from Model.Sprite import Sprite
from Model.Acao import Acao
from Controller.Controller import Controller
from Singleton.Singleton import Singleton
from Model.SkillSlot import SkillSlot
import time

class BatalhaView():
    def __init__(self, aliados: list[Personagem],
                 inimigos: list[Personagem]):
        self.__screenSize = Singleton().screenSize
        self.__larguraTela, self.__alturaTela = self.__screenSize
        self.__window = pygame.display.set_mode(self.__screenSize, pygame.RESIZABLE)

        self.__aliadosPersonagens = aliados
        self.__inimigosPersonagens = inimigos

        self.__spritesAliados = pygame.sprite.Group()
        self.__spritesInimigos = pygame.sprite.Group()
        self.__spritesSlots = pygame.sprite.Group()
        
        self.__personagemSelecionado = None

        self.__playerTurn = True
        self.__winner = -1

        self.fillSprites()

        self.__controller = Controller()

    '''
    createSprites é responsável por instanciar todos os sprites que serão mostrados na tela
    @params None
    @return None
    '''

    def fillSprites(self):
        for i in self.__aliadosPersonagens:
            self.__spritesAliados.add(i.sprite)
        self.__spritesInimigos.add([i.sprite for i in self.__inimigosPersonagens])
        self.__spritesSlots.add([SkillSlot() for i in range (8)])
        for i in self.__spritesSlots:
            print(i.rect)

    def obterPosicoes(self, atacante:Sprite, alvo:Sprite):
        posicaoAlvo = alvo.coord
        posicaoAtacante = atacante.coord
        return posicaoAtacante, posicaoAlvo

    '''
    animacao é responsável pelas animações da tela, tanto dos personagens quanto das habilidades
    @params atacante: Personagem => o personagem que executa a ação
    @params alvo: Personagem => o personagem atacado
    @params habilidade: Acao => a habilidade utilizada
    @return None
    '''
    def animacao(self, atacante:Personagem, alvo:Personagem, acao: Acao):

        atacante.animacao(0)
        acao.animacao(atacante.sprite, alvo.sprite)
        alvo.animacao(1)
        
    
    '''
    turn é responsável por executar um turno (ataque)
    @params atacante: Personagem => o personagem que executa a ação
    @params alvos: list[Personagem] => a lista de alvos disponíveis
    @return None
    '''
    def turno(self, 
              atacante: Personagem,
              atacantes: list[Personagem],
              alvos:list[Personagem],
              habilidade: Acao):
        
        if habilidade.tipo == 'suporte':
            alvo = self.__controller.selecionaPersonagem(atacantes)
        else:
            alvo = self.__controller.selecionaPersonagem(alvos)
        self.animacao(atacante, alvo, habilidade)


        self.__playerTurn = not self.__playerTurn
        self.__winner = self.__controller.checkForWinner(self.__aliadosPersonagens, self.__inimigosPersonagens)

        self.desenha()
        if self.__winner != -1:
            self.mostraResultado()

    '''
    drawHealthBars é a função que desenha a barra de vida dos personagens
    @params None
    @return None
    '''
    def desenhaBarrasDeVida(self):
        for i, (aliado, inimigo) in enumerate(zip(self.__spritesAliados, self.__spritesInimigos)):
            w = 60
            h = 15

            personagens = self.__aliadosPersonagens
            x, y = aliado.rect.centerx, aliado.rect.centery - 50

            for j in range (2):
                saude = personagens[i].get_saude()
                if saude > 0:
                    outerRect = pygame.Rect(x, y, w, h)
                    outerRect.center = (x, y)
                    pygame.draw.rect(self.__window, (0, 0, 0), outerRect, 1)
                    progresso = saude / personagens[i].saude_max

                    innerPosition = (outerRect.x+3, outerRect.y+3)
                    innerSize = ((w-6)*progresso, h-6)

                    innerRect = pygame.Rect(*innerPosition, *innerSize)

                    pygame.draw.rect(self.__window, (0, 255, 0), innerRect)
                
                personagens = self.__inimigosPersonagens
                x, y = inimigo.rect.centerx, inimigo.rect.centery - 50

    '''
    draw é a função que desenha todas as sprites na tela
    @params None
    @return None
    '''
    def desenha(self):
        self.__window.fill((255, 255, 255))
        self.__spritesAliados.draw(self.__window)
        self.__spritesInimigos.draw(self.__window)
        self.__spritesSlots.draw(self.__window)
        
        self.desenhaBarrasDeVida()
        pygame.display.flip()
    
    '''
    showResult é responsável por mostrar o resultado na tela
    @params none
    @return None
    '''
    def mostraResultado(self):
        winner = ''
        if self.__winner == 0:
            winner = 'enemies'
        else:
            winner = 'allies'

        resultado = Sprite(winner, self.__larguraTela/2, self.__alturaTela/2, self.__larguraTela/4, self.__alturaTela/4)
        resultado.draw(self.__window)

    '''
    main é a função principal da classe, que executa o loop
    que mantém a tela rodando
    @params None
    @return bool => utilizada posteriormente em Jogo para mudar o estado
    '''

    def setTamanhoTela(self):
        if isinstance(self.__window, pygame.Surface):
            self.__screenSize = self.__window.get_size()
            Singleton().screenSize = self.__screenSize

    def handleScreenEvents(self, event:pygame.event.Event):
            if event.type == pygame.VIDEORESIZE:
                self.__window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                self.setTamanhoTela()
                pygame.display.update()
                self.desenha()
                        
            if event.type == pygame.QUIT:
                return False
            
            return True

    def handleInteractions(self, event:pygame.event.Event):
        if self.__playerTurn:
            for i, sprite in enumerate(self.__spritesAliados):
                if event.type == pygame.MOUSEBUTTONDOWN and sprite.rect.collidepoint(pygame.mouse.get_pos()):
                    self.__personagemSelecionado = self.__aliadosPersonagens[i]
                    self.__personagemSelecionado.mostraHabilidadesDisponives(self.__window)
            self.desenha()

            if self.__personagemSelecionado is not None and self.__personagemSelecionado.get_saude() > 0:
                for i, sprite in enumerate(self.__spritesSlots):
                    if event.type == pygame.MOUSEBUTTONDOWN and sprite.rect.collidepoint(pygame.mouse.get_pos()):
                        self.turno(atacante = self.__personagemSelecionado, 
                                   atacantes = self.__aliadosPersonagens,
                                   alvos = self.__inimigosPersonagens,
                                   habilidade = self.__personagemSelecionado.get_acao(i))
        else:
            atacante = self.__controller.selecionaPersonagem(self.__inimigosPersonagens)
            habilidade = self.__controller.selecionaHabilidade(atacante)

            alvos = self.__aliadosPersonagens
            time.sleep(0.5)
            self.turno(atacante, self.__inimigosPersonagens, alvos, habilidade)

    def loop(self):
        fps = 30
        clock = pygame.time.Clock()
        run = True
        
        while run:
            clock.tick(fps)
            self.setTamanhoTela()

            for event in pygame.event.get():
                
                run = self.handleScreenEvents(event)

                if self.__winner == -1:
                    self.handleInteractions(event)

            if not self.__winner != -1:
                # self.criaSprites()
                self.desenha()

