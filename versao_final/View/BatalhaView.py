import pygame
from Model.Personagem import Personagem
from View.Sprite import Sprite
from Model.Acao import Acao
import os
import time
import random as r

class BatalhaView():
    def __init__(self, aliados: list[Personagem],
                 inimigos: list[Personagem]):
        self.__window = pygame.display.set_mode((1000, 500), pygame.RESIZABLE)

        self.__aliadosPersonagens = aliados
        self.__inimigosPersonagens = inimigos

        self.__timeAliado = pygame.sprite.Group()
        self.__timeInimigo = pygame.sprite.Group()
        self.__elements = pygame.sprite.Group()
        self.__skills = pygame.sprite.Group()

        self.__playerTurn = True
        self.__finished = False
        self.__winner = -1

        self.createSprites()

    '''
    createSprites é responsável por instanciar todos os sprites que serão mostrados na tela
    @params None
    @return None
    '''
    def createSprites(self):

        # Esvazia todos os grupos de sprites
        self.__timeAliado.empty()
        self.__timeInimigo.empty()
        self.__elements.empty()
        self.__skills.empty()

        winw, winh = self.__window.get_size()

        # Instancia os 3 personagens de cada lado
        for i in range (3):

            # Shift serve para deslocar a posição do personagem do meio
            shift = 0
            if i == 1:
                shift = winw/10
            

            # Renderiza todos os personagens na tela
            grupo = self.__timeAliado
            personagem = self.__aliadosPersonagens[i]
            x = winw/5 - shift
            y = winh/5 * (i+1)

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

                grupo = self.__timeInimigo
                personagem = self.__inimigosPersonagens[i]
                x = winw - (winw/5 - shift + 60)
        

        # Renderiza os slots de habilidade
        cont = 7
        for i in range (7):
            ret = Sprite(filename = 'retangulo', 
                         width = 50, 
                         height = 50, 
                         x = winw/22*cont, 
                         y = winh-50)
            self.__elements.add(ret)

            skill = Sprite(filename = 'fireball', 
                           width = 46, 
                           height = 46, 
                           x = winw/22*cont + 2, 
                           y = winh-48)
            self.__skills.add(skill)

            cont += 1
    
    '''
    animation é responsável pelas animações da tela, tanto dos personagens quanto das habilidades
    @params atacante: Personagem => o personagem que executa a ação
    @params alvo: Personagem => o personagem atacado
    @params habilidade: Acao => a habilidade utilizada
    @return None
    '''
    def animation(self, atacante:Personagem, alvo:Personagem, habilidade:Acao):
        atacanteSprite = atacante.sprite
        alvoSprite = alvo.sprite

        '''
        O personagem se desloca para frente antes de atacar
        '''
        for i in range (10):
            if atacanteSprite.rect.x > alvoSprite.rect.x:
                atacanteSprite.rect.x -= 2
            else:
                atacanteSprite.rect.x += 2
            self.draw()
            
        time.sleep(0.5)
        multiplicador = r.randint(1, 20)

        
        '''
        Renderiza o sprite da habilidade
        '''

        default_width, default_height = 60, 80

        habilidadeSprite = Sprite(filename = habilidade.nome, 
                                  width = default_width,
                                  height = default_height,
                                  x = atacante.sprite.rect.x,
                                  y = atacante.sprite.rect.y)

        '''
        Registra a posição da tela do atacante e do alvo
        '''
        if atacanteSprite in self.__timeAliado:    
            atacantePos = self.__timeAliado.sprites().index(atacanteSprite)
            alvoPos = self.__timeInimigo.sprites().index(alvoSprite)
        else:
            atacantePos = self.__timeInimigo.sprites().index(atacanteSprite)
            alvoPos = self.__timeAliado.sprites().index(alvoSprite)
        
        '''
        Move a habilidade até ela atingir o alvo
        '''
        hit = False
        while not hit:
            hit, habilidadeSprite = habilidade.animation(atacanteSprite, alvoSprite, habilidadeSprite, atacantePos, alvoPos)
            self.__skills.add(habilidadeSprite)
            self.draw()
        habilidadeSprite.kill()

        '''
        Registra o dano da habilidade
        '''
        habilidade.executar(alvo, multiplicador)

        '''
        O alvo treme quando é atingido pela habilidade
        '''
        for i in range (10):
            if i%2 == 0:
                alvoSprite.rect.x += 4
                alvoSprite.rect.y += 4
            else:
                alvoSprite.rect.x -= 4
                alvoSprite.rect.y -= 4

            self.draw()

    '''
    checkForWinner verifica se existe alguma equipe cujos personagens estão todos sem vida
    @params None
    @return None
    '''
    def checkForWinner(self):
        cont = 0
        for i in self.__aliadosPersonagens:
            if i.get_saude() >= 0:
                cont += 1
        if cont == 0:
            self.__finished = True
            self.__winner = 0
            return
        cont = 0
        for i in self.__inimigosPersonagens:
            if i.get_saude() >= 0:
                cont += 1
        if cont == 0:
            self.__finished = True
            self.__winner = 1
            return
    
    '''
    turn é responsável por executar um turno (ataque)
    @params atacante: Personagem => o personagem que executa a ação
    @params alvos: list[Personagem] => a lista de alvos disponíveis
    @return None
    '''
    def turn(self, atacante: Personagem, alvos:list[Personagem]):

        habilidade = atacante.get_acao()
        
        # Caso o alvo escolhido não tenha vida restante, tenta selecionar outro
        alvo = r.choice(alvos)
        while alvo.get_saude() <= 0:
            alvo = r.choice(alvos)

        # TODO: habilidades do tipo suporte
        if habilidade.tipo == 'suporte':
            pass

        self.animation(atacante, alvo, habilidade)

        self.__playerTurn = not self.__playerTurn
        self.checkForWinner()

    '''
    drawHealthBars é a função que desenha a barra de vida dos personagens
    @params None
    @return None
    '''
    def drawHealthBars(self):
        for i, (aliado, inimigo) in enumerate(zip(self.__timeAliado, self.__timeInimigo)):
            w = 60
            h = 15

            personagens = self.__aliadosPersonagens
            x, y = aliado.rect.x, aliado.rect.y - 20

            for j in range (2):
                saude = personagens[i].get_saude()
                if saude >= 0:
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
        self.__timeAliado.draw(self.__window)
        self.__timeInimigo.draw(self.__window)
        self.__elements.draw(self.__window)
        self.__skills.draw(self.__window)
        self.drawHealthBars()
        pygame.display.flip()
    
    '''
    showResult é responsável por mostrar o resultado na tela
    @params winner: str => time vencedor, usado para carregar a imagem
    @return None
    '''
    def showResult(self, winner:str):
        winw, winh = self.__window.get_size()
        result = pygame.image.load(os.path.join('versao_final/assets', f'{winner}.png'))
        result = pygame.transform.scale(result, (winw/2, winh/2))
        self.__window.blit(result, (winw/4, winh/4))
        pygame.display.update()

    '''
    main é a função principal da classe, que executa o loop
    que mantém a tela rodando
    @params None
    @return bool => utilizada posteriormente em Jogo para mudar o estado
    '''
    def main(self):
        fps = 30
        clock = pygame.time.Clock()
        run = True
        
        while run:
            clock.tick(fps)

            for event in pygame.event.get():
                if event.type == pygame.VIDEORESIZE:
                    window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    pygame.display.update()
                
                if self.__finished:
                    if self.__winner == 0:
                        self.showResult('enemies')
                    else:
                        self.showResult('allies')
                else:
                    if self.__playerTurn:
                        atacantes, sprites = self.__aliadosPersonagens, self.__timeAliado
                        alvos = self.__inimigosPersonagens

                        for i, sprite in enumerate(sprites):
                            if event.type == pygame.MOUSEBUTTONDOWN and sprite.rect.collidepoint(pygame.mouse.get_pos()):
                                self.turn(atacantes[i], alvos)
                    else:
                        atacante = r.choice(self.__inimigosPersonagens)
                        while atacante.get_saude() <= 0:
                            atacante = r.choice(self.__inimigosPersonagens)

                        alvos = self.__aliadosPersonagens
                        time.sleep(0.5)
                        self.turn(atacante, alvos)

                    self.createSprites()
                    self.draw()

                if event.type == pygame.QUIT:
                    return False
