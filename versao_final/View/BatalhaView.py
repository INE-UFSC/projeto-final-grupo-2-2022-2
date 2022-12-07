import pygame
from Model.Personagem import Personagem
from Model.Sprite import Sprite
from Controller.Controller import Controller
from Singleton.Singleton import Singleton
from Model.SkillSlot import SkillSlot
from Model.Animacao import Animacao

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
        self.__spritesHabilidades = pygame.sprite.Group()
        
        self.__personagemSelecionado = None
        self.__animacao = Animacao()
        self.__animacaoFinalizada = True
        self.__animacaoSprites = []

        self.__playerTurn = True
        self.__winner = -1

        self.fillSprites()

        self.__controller = Controller()

    def fillSprites(self):
        for i in self.__aliadosPersonagens:
            self.__spritesAliados.add(i.sprite)
        self.__spritesInimigos.add([i.sprite for i in self.__inimigosPersonagens])
        self.__spritesSlots.add([SkillSlot() for i in range (8)])

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
    def animacao(self):
        self.__animacaoFinalizada = self.__animacao.executa(*self.__animacaoSprites)
        
    
    '''
    turno é responsável por executar um turno (ataque)
    @params atacante: Personagem => o personagem que executa a ação
    @params alvos: list[Personagem] => a lista de alvos disponíveis
    @return None
    '''
    def turno(self):
        self.animacao()

        self.__playerTurn = not self.__playerTurn
        self.__winner = self.__controller.checkForWinner(self.__aliadosPersonagens, self.__inimigosPersonagens)

    '''
    desenha é a função que desenha todas as sprites na tela
    @params None
    @return None
    '''
    def desenha(self):
        self.__window.fill((255, 255, 255))
        self.__spritesAliados.draw(self.__window)
        self.__spritesInimigos.draw(self.__window)
        self.__spritesSlots.draw(self.__window)
        self.__spritesHabilidades.draw(self.__window)
        for i, j in zip(self.__aliadosPersonagens, self.__inimigosPersonagens):
            i.desenhaBarraDeVida(self.__window)
            j.desenhaBarraDeVida(self.__window)
        # self.desenhaBarrasDeVida()
        pygame.display.flip()
    
    '''
    mostraResultado é responsável por mostrar o resultado na tela
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
    
    def mostraHabilidades(self, index:int):
        self.__personagemSelecionado = self.__aliadosPersonagens[index]
        acoes = self.__personagemSelecionado.getHabilidades()
        for slot, acao in zip(self.__spritesSlots, acoes):
            slot.skill = acao
            self.__spritesHabilidades.add(slot.skill)

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
                    self.mostraHabilidades(i)

            if self.__personagemSelecionado is not None and self.__personagemSelecionado.get_saude() > 0:
                for i, sprite in enumerate(self.__spritesSlots):
                    if event.type == pygame.MOUSEBUTTONDOWN and sprite.rect.collidepoint(pygame.mouse.get_pos()):
                        self.__animacaoSprites = [
                            self.__personagemSelecionado.sprite,
                            self.__controller.selecionaPersonagem(self.__inimigosPersonagens).sprite,
                            self.__personagemSelecionado.get_acao(i).sprite
                        ]
                        self.turno()
                        break
        else:
            atacante = self.__controller.selecionaPersonagem(self.__inimigosPersonagens)
            self.__animacaoSprites = [
                atacante.sprite,
                self.__controller.selecionaPersonagem(self.__aliadosPersonagens).sprite,
                self.__controller.selecionaHabilidade(atacante).sprite
            ]
            self.turno()
    
    '''
    main é a função principal da classe, que executa o loop
    que mantém a tela rodando
    @params None
    @return bool => utilizada posteriormente em Jogo para mudar o estado
    '''
    def loop(self):
        fps = 120
        clock = pygame.time.Clock()
        run = True
        
        while run:
            clock.tick(fps)
            self.setTamanhoTela()

            if not self.__animacaoFinalizada:
                self.animacao()

            for event in pygame.event.get():
                
                run = self.handleScreenEvents(event)

                if self.__winner == -1:
                    self.handleInteractions(event)

            if not self.__winner != -1:
                self.desenha()
            else:
                self.mostraResultado()

