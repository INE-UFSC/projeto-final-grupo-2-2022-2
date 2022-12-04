import pygame
from Model.Personagem import Personagem
from View.Sprite import Sprite
from Model.Acao import Acao
from Controller.Controller import Controller
from Singleton.Singleton import Singleton
import os
import time
import random as r

class BatalhaView():
    def __init__(self, aliados: list[Personagem],
                 inimigos: list[Personagem]):
        self.__screenSize = Singleton().screenSize
        self.__window = pygame.display.set_mode(self.__screenSize, pygame.RESIZABLE)

        self.__aliadosPersonagens = aliados
        self.__inimigosPersonagens = inimigos

        self.__spritesAliados = pygame.sprite.Group()
        self.__spritesInimigos = pygame.sprite.Group()
        self.__spritesElementos = pygame.sprite.Group()
        self.__spritesHabilidades = pygame.sprite.Group()

        self.__playerTurn = True
        self.__winner = -1

        self.__controller = Controller(aliados, inimigos)

        self.createSprites()

    '''
    createSprites é responsável por instanciar todos os sprites que serão mostrados na tela
    @params None
    @return None
    '''
    def createSprites(self):

        # Esvazia todos os grupos de sprites
        self.__spritesAliados.empty()
        self.__spritesInimigos.empty()
        self.__spritesElementos.empty()
        self.__spritesHabilidades.empty()

        larguraTela, alturaTela = self.__window.get_size()

        # Instancia os 3 personagens de cada lado
        for i in range (3):

            # Shift serve para deslocar a posição do personagem do meio
            mover = 0
            if i == 1:
                mover = larguraTela/10
            

            # Renderiza todos os personagens na tela
            grupo = self.__spritesAliados
            personagem = self.__aliadosPersonagens[i]
            x = larguraTela/5 - mover
            y = alturaTela/5 * (i+1)

            for j in range (2):
                default_width = 60
                default_height = 80

                '''
                Caso o personagem não tenha mais vida, ele não terá tamanho,
                logo não aparecerá na tela, mas permanecerá na lista de personagens
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
                x = larguraTela - (larguraTela/5 - mover + 60)
        

        # Renderiza os slots de habilidade
        cont = 7
        for i in range (7):
            ret = Sprite(filename = 'retangulo', 
                         width = 50, 
                         height = 50, 
                         x = larguraTela/22*cont, 
                         y = alturaTela-50)
            self.__spritesElementos.add(ret)

            habilidade = Sprite(filename = 'fireball', 
                           width = 46, 
                           height = 46, 
                           x = larguraTela/22*cont + 2, 
                           y = alturaTela-48)
            self.__spritesHabilidades.add(habilidade)

            cont += 1
    
    def animaAtacante(self, atacante:Sprite, alvo:Sprite):
        for i in range (10):
            if atacante.rect.x > alvo.rect.x:
                atacante.rect.x -= 2
            else:
                atacante.rect.x += 2
            self.draw()
    
    def animaAlvo(self, alvo:Sprite):
        for i in range (10):
            if i%2 == 0:
                alvo.rect.x += 4
                alvo.rect.y += 4
            else:
                alvo.rect.x -= 4
                alvo.rect.y -= 4

            self.draw()

    def obterPosicoes(self, atacante:Sprite, alvo:Sprite):
        if atacante in self.__spritesAliados:    
            posicaoAtacante = self.__spritesAliados.sprites().index(atacante)
            posicaoAlvo = self.__spritesInimigos.sprites().index(alvo)
        else:
            posicaoAtacante = self.__spritesInimigos.sprites().index(atacante)
            posicaoAlvo = self.__spritesAliados.sprites().index(alvo)
        return posicaoAtacante, posicaoAlvo

    def animaHabilidade(self, 
                       habilidade:Acao,
                       habilidadeSprite: Sprite, 
                       atacante: Sprite, 
                       alvo: Sprite,
                       posicaoAtacante: int,
                       posicaoAlvo: int):
        hit = False

        while not hit:
            hit, habilidadeSprite = habilidade.animation(atacante, 
                                                         alvo, 
                                                         habilidadeSprite,
                                                         posicaoAtacante,
                                                         posicaoAlvo)
            self.__spritesHabilidades.add(habilidadeSprite)
            self.draw()

        habilidadeSprite.kill()    
        atacante.rect.x = atacante.defaultSize[0]

    '''
    animacao é responsável pelas animações da tela, tanto dos personagens quanto das habilidades
    @params atacante: Personagem => o personagem que executa a ação
    @params alvo: Personagem => o personagem atacado
    @params habilidade: Acao => a habilidade utilizada
    @return None
    '''
    def animacao(self, atacante:Personagem, alvo:Personagem, habilidade:Acao):
        
        default_width, default_height = 60, 80
        atacanteSprite = atacante.sprite
        alvoSprite = alvo.sprite

        self.animaAtacante(atacanteSprite, alvoSprite)
            
        time.sleep(0.5)
        multiplicador = r.randint(1, 20)

        habilidadeSprite = Sprite(filename = habilidade.nome, 
                                  width = default_width,
                                  height = default_height,
                                  x = atacante.sprite.rect.x,
                                  y = atacante.sprite.rect.y)

        posicaoAtacante, posicaoAlvo = self.obterPosicoes(atacanteSprite, alvoSprite)

        self.animaHabilidade(habilidade = habilidade,
                            habilidadeSprite = habilidadeSprite,
                            atacante = atacanteSprite,
                            alvo = alvoSprite,
                            posicaoAtacante = posicaoAtacante,
                            posicaoAlvo = posicaoAlvo)

        habilidade.executar(alvo, multiplicador)

        self.animaAlvo(alvoSprite)
        
    
    '''
    turn é responsável por executar um turno (ataque)
    @params atacante: Personagem => o personagem que executa a ação
    @params alvos: list[Personagem] => a lista de alvos disponíveis
    @return None
    '''
    def turno(self, atacante: Personagem, alvos:list[Personagem]):

        alvo, habilidade = self.__controller.selecionaAlvoEHabilidade(atacante, alvos)

        self.animacao(atacante, alvo, habilidade)

        self.__playerTurn = not self.__playerTurn
        self.__winner = self.__controller.checkForWinner(self.__aliadosPersonagens, self.__inimigosPersonagens)

        self.createSprites()
        self.draw()
        if self.__winner != -1:
            self.showResult()

    '''
    drawHealthBars é a função que desenha a barra de vida dos personagens
    @params None
    @return None
    '''
    def drawHealthBars(self):
        for i, (aliado, inimigo) in enumerate(zip(self.__spritesAliados, self.__spritesInimigos)):
            w = 60
            h = 15

            personagens = self.__aliadosPersonagens
            x, y = aliado.rect.x, aliado.rect.y - 20

            for j in range (2):
                saude = personagens[i].get_saude()
                if saude > 0:
                    pygame.draw.rect(self.__window, (0, 0, 0), pygame.Rect(x, y, w, h), 1)
                    progresso = saude / personagens[i].saude_max

                    innerPosition = (x+3, y+3)
                    innerSize = ((w-6)*progresso, h-6)

                    pygame.draw.rect(self.__window, (0, 255, 0), pygame.Rect(*innerPosition, *innerSize))
                
                personagens = self.__inimigosPersonagens
                x, y = inimigo.rect.x, inimigo.rect.y - 20

    '''
    draw é a função que desenha todas as sprites na tela
    @params None
    @return None
    '''
    def draw(self):
        self.__window.fill((255, 255, 255))
        self.__spritesAliados.draw(self.__window)
        self.__spritesInimigos.draw(self.__window)
        self.__spritesElementos.draw(self.__window)
        self.__spritesHabilidades.draw(self.__window)
        self.drawHealthBars()
        pygame.display.flip()
    
    '''
    showResult é responsável por mostrar o resultado na tela
    @params winner: str => time vencedor, usado para carregar a imagem
    @return None
    '''
    def showResult(self):
        larguraJanela, alturaJanela = self.__window.get_size()
        winner = ''
        if self.__winner == 0:
            winner = 'enemies'
        else:
            winner = 'allies'

        resultado = Sprite(winner, larguraJanela/2, alturaJanela/2, larguraJanela/4, alturaJanela/4)
        resultado.draw(self.__window)

    '''
    main é a função principal da classe, que executa o loop
    que mantém a tela rodando
    @params None
    @return bool => utilizada posteriormente em Jogo para mudar o estado
    '''

    def setScreenSize(self):
        if isinstance(self.__window, pygame.Surface):
            self.__screenSize = self.__window.get_size()
            Singleton().screenSize = self.__screenSize

    def handleScreenEvents(self, event:pygame.event.Event):
            if event.type == pygame.VIDEORESIZE:
                self.__window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                pygame.display.update()
                self.createSprites()
                self.draw()
                
            if event.type == pygame.QUIT:
                return False
            
            return True

    def handleAttacks(self, event:pygame.event.Event):
        if self.__playerTurn:
            atacantes, sprites = self.__aliadosPersonagens, self.__spritesAliados
            alvos = self.__inimigosPersonagens

            for i, sprite in enumerate(sprites):
                if event.type == pygame.MOUSEBUTTONDOWN and sprite.rect.collidepoint(pygame.mouse.get_pos()):
                    self.turno(atacantes[i], alvos)
        else:
            atacante = r.choice(self.__inimigosPersonagens)
            while atacante.get_saude() <= 0:
                atacante = r.choice(self.__inimigosPersonagens)

            alvos = self.__aliadosPersonagens
            time.sleep(0.5)
            self.turno(atacante, alvos)

    def loop(self):
        fps = 30
        clock = pygame.time.Clock()
        run = True
        self.draw()
        
        while run:
            clock.tick(fps)
            self.setScreenSize()

            for event in pygame.event.get():
                
                run = self.handleScreenEvents(event)

                if self.__winner == -1:
                    self.handleAttacks(event)

            if not self.__winner != -1:
                self.createSprites()
                self.draw()

