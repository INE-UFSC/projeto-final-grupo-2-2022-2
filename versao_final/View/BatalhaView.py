import pygame
from Model.Personagem import Personagem
from Model.Sprite import Sprite
from Model.Acao import Acao
from Controller.Controller import Controller
from Singleton.Constantes import Constantes
import time

class BatalhaView():
    def __init__(self, aliados: list[Personagem],
                 inimigos: list[Personagem]):

        self.__screenSize = Constantes().screenSize
        self.__larguraTela, self.__alturaTela = self.__screenSize
        self.__window = pygame.display.set_mode(self.__screenSize,
                                                pygame.RESIZABLE)
        self.__defaultWidth, self.__defaultHeight = Constantes().defaultSize

        self.__aliadosPersonagens = aliados
        self.__inimigosPersonagens = inimigos

        self.__spritesAliados = pygame.sprite.Group()
        self.__spritesInimigos = pygame.sprite.Group()
        self.__spritesElementos = pygame.sprite.Group()
        self.__spritesHabilidades = pygame.sprite.Group()

        self.__personagemSelecionado = None

        self.__playerTurn = True
        self.__winner = -1

        self.__controller = Controller()

    def loop(self):
        fps = 30
        clock = pygame.time.Clock()
        run = True
        self.desenha()
        
        while run:
            clock.tick(fps)
            self.setTamanhoTela()

            for event in pygame.event.get():
                
                run = self.handleScreenEvents(event)

                if self.__winner == -1:
                    self.handleInteractions(event)

            if not self.__winner != -1:
                self.criaSprites()
                self.desenha()
            else:
                return self.__winner
    
    '''
    turno é responsável por executar um turno (ataque)
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
        self.__winner = self.__controller.checkForWinner(self.__aliadosPersonagens,
                                                         self.__inimigosPersonagens)

        self.criaSprites()
        self.desenha()
        if self.__winner != -1:
            self.mostraResultado()
            for i in self.__aliadosPersonagens

    def handleInteractions(self, event:pygame.event.Event):
        if self.__playerTurn:
            for i, sprite in enumerate(self.__spritesAliados):
                c = event.type == pygame.MOUSEBUTTONDOWN
                c = c and sprite.rect.collidepoint(pygame.mouse.get_pos()) 
                if c:
                    self.mostraHabilidadesDoPersonagem(i)
            self.desenha()

            c0 = self.__personagemSelecionado is not None
            c0 = c0 and self.__personagemSelecionado.get_saude() > 0
            if c0:
                for i, sprite in enumerate(self.__spritesHabilidades):
                    c1 = event.type == pygame.MOUSEBUTTONDOWN
                    c1 = c1 and sprite.rect.collidepoint(pygame.mouse.get_pos())
                    if c1:
                        self.turno(atacante = self.__personagemSelecionado, 
                                   atacantes = self.__aliadosPersonagens,
                                   alvos = self.__inimigosPersonagens,
                        habilidade = self.__personagemSelecionado.get_acao(i))
        else:
            atacante = self.__controller.selecionaPersonagem(
                self.__inimigosPersonagens)
            habilidade = self.__controller.selecionaHabilidade(atacante)

            alvos = self.__aliadosPersonagens
            time.sleep(0.5)
            self.turno(atacante,
                       self.__inimigosPersonagens,
                       alvos, habilidade)

    '''
    createSprites é responsável por instanciar
    todos os sprites que serão mostrados na tela
    @params None
    @return None
    '''
    def criaSprites(self):

        # Esvazia todos os grupos de sprites
        self.__spritesAliados.empty()
        self.__spritesInimigos.empty()
        self.__spritesElementos.empty()
        self.__spritesHabilidades.empty()

        self.__larguraTela, self.__alturaTela = self.__window.get_size()

        # Instancia os 3 personagens de cada lado
        for i in range (3):

            # Shift serve para deslocar a posição do personagem do meio
            mover = 0
            if i == 1:
                mover = self.__larguraTela/10
            

            # Renderiza todos os personagens na tela
            grupo = self.__spritesAliados
            personagem = self.__aliadosPersonagens[i]
            x = self.__larguraTela/5 - mover
            y = self.__alturaTela/5 * (i+1)

            for j in range (2):
                default_width = self.__defaultWidth
                default_height = self.__defaultHeight

                '''
                Caso o personagem não tenha mais vida,
                ele não terá tamanho,
                logo não aparecerá na tela,
                mas permanecerá na lista de personagens
                '''
                if personagem.get_saude() <= 0:
                    default_width, default_height = 0, 0

                personagemSprite = Sprite(filename = personagem.classe, 
                                          width = default_width, 
                                          height = default_height, 
                                          x = x, 
                                          y = y)
                personagem.sprite = personagemSprite
                grupo.add(personagemSprite)

                grupo = self.__spritesInimigos
                personagem = self.__inimigosPersonagens[i]
                x = self.__larguraTela - (self.__larguraTela/5 - mover + 60)
        

        # Renderiza os slots de habilidade
        cont = 7
        for i in range (7):
            ret = Sprite(filename = 'retangulo', 
                         width = 50, 
                         height = 50, 
                         x = self.__larguraTela/22*cont, 
                         y = self.__alturaTela-50)
            self.__spritesElementos.add(ret)

            cont += 1
        if self.__personagemSelecionado is not None:
            self.mostraHabilidadesDoPersonagem(
                self.__aliadosPersonagens.index(
                    self.__personagemSelecionado))
    
    def mostraHabilidadesDoPersonagem(self, index:int):
        cont = 7

        self.__spritesHabilidades.empty()
        self.__personagemSelecionado = self.__aliadosPersonagens[index]

        if len(self.__aliadosPersonagens) > index:
            skills = self.__personagemSelecionado.tecnicas 

            for acao in skills:
                self.__spritesHabilidades.add(
                    Sprite(filename = acao.nome,
                            width = 45,
                            height = 45,
                            x = self.__larguraTela/22*cont + 2, 
                            y = self.__alturaTela-48)
                    )
                cont += 1

    def animaAtacante(self, atacante:Sprite,
                      alvo:Sprite):
        for i in range (10):
            if atacante.rect.x > alvo.rect.x:
                atacante.rect.x -= 2
            else:
                atacante.rect.x += 2
            self.desenha()
    
    def animaAlvo(self, alvo:Sprite):
        alvo.rect.x += 4
        alvo.rect.y += 4
        self.desenha()
        alvo.rect.x -= 4
        alvo.rect.y -= 4

    def obterPosicoes(self, atacante:Sprite,
                      alvo:Sprite):
        posicaoAlvo = alvo.coord
        posicaoAtacante = atacante.coord
        return posicaoAtacante, posicaoAlvo

    def animaAtaque(self, 
                    movedSprite: Sprite, 
                    atacante: Sprite, 
                    alvo: Sprite):

        atacantePosicao, alvoPosicao = self.obterPosicoes(atacante,
                                                          alvo)
        hit = False

        self.__spritesHabilidades.add(movedSprite)
        while not hit:
            hit = movedSprite.move(atacantePosicao,
                                   alvoPosicao,
                                   alvo.rect)
            self.desenha()
        
        if movedSprite == atacante:
            time.sleep(0.5)

        movedSprite.kill()
        # Volta para posição original
        atacante.rect.x = atacante.defaultSize[0]

    '''
    animacao é responsável pelas animações da tela,
    tanto dos personagens quanto das habilidades
    @params atacante: Personagem => o personagem que executa a ação
    @params alvo: Personagem => o personagem atacado
    @params habilidade: Acao => a habilidade utilizada
    @return None
    '''
    def animacao(self, atacante:Personagem,
                 alvo:Personagem, acao: Acao):
        atacanteSprite = atacante.sprite
        alvoSprite = alvo.sprite

        self.animaAtacante(atacanteSprite, alvoSprite)
            
        time.sleep(0.5)
        if acao.modo == 'projetil':
            movedSprite = Sprite(filename = acao.nome, 
                                    width = self.__defaultWidth,
                                    height = self.__defaultHeight,
                                    x = atacante.sprite.rect.x,
                                    y = atacante.sprite.rect.y)
        else:
            movedSprite = atacanteSprite

        self.animaAtaque(movedSprite, atacanteSprite, alvoSprite)

        acao.executar(alvo)

        self.animaAlvo(alvoSprite)

    '''
    drawHealthBars é a função que desenha a barra de vida dos personagens
    @params None
    @return None
    '''
    def desenhaBarrasDeVida(self):
        for i, (aliado, inimigo) in enumerate(zip(self.__spritesAliados,
                                                  self.__spritesInimigos)):
            w = 60
            h = 15

            personagens = self.__aliadosPersonagens
            x, y = aliado.rect.centerx, aliado.rect.centery - 50

            for j in range (2):
                saude = personagens[i].get_saude()
                if saude > 0:
                    outerRect = pygame.Rect(x, y, w, h)
                    outerRect.center = (x, y)
                    pygame.draw.rect(self.__window,
                                     (0, 0, 0), outerRect, 1)
                    progresso = saude / personagens[i].saude_max

                    innerPosition = (outerRect.x+3,
                                     outerRect.y+3)
                    innerSize = ((w-6)*progresso, h-6)

                    innerRect = pygame.Rect(*innerPosition,
                                            *innerSize)

                    pygame.draw.rect(self.__window,
                                     (0, 255, 0),
                                     innerRect)
                
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
        self.__spritesElementos.draw(self.__window)
        self.__spritesHabilidades.draw(self.__window)
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

        resultado = Sprite(winner, self.__larguraTela/2,
                           self.__alturaTela/2,
                           self.__larguraTela/4,
                           self.__alturaTela/4)
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
            Constantes().screenSize = self.__screenSize

    def handleScreenEvents(self, event:pygame.event.Event):
            if event.type == pygame.VIDEORESIZE:
                self.__window = pygame.display.set_mode((event.w, event.h),
                                                        pygame.RESIZABLE)
                pygame.display.update()
                self.criaSprites()
                self.desenha()
                        
            if event.type == pygame.QUIT:
                return False
            
            return True
