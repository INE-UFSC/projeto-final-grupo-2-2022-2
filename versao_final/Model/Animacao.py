from Model.Sprite import Sprite

class Animacao:
    def __init__(self) -> None:
        self.__progresso = 0
        self.__colidiu = False
        pass
    
    def executa(self, atacante:Sprite, alvo: Sprite, habilidade: Sprite):
        finished = False

        if not self.__colidiu:
            if self.__progresso < 10:
                atacante.rect.x += 2
                # print('a')

            if self.__progresso >= 10:
                self.__colidiu = habilidade.move(atacante.position, alvo.position, alvo.rect)
                # print('b')

            if self.__progresso >= 10 and self.__progresso < 20:
                atacante.rect.x -= 2
                # print('c')

            if self.__colidiu: 
                self.__progresso = 0
                habilidade.kill()
                # print('d')

        else:
            if self.__progresso == 1:
                alvo.rect.x += 4
                alvo.rect.y += 4
                # print('e')

            if self.__progresso == 2:
                alvo.rect.x -= 4
                alvo.rect.y -= 4
                # print('f')

                finished = True
                self.__colidiu = False
                self.__progresso = 0
        
        self.__progresso += 1
        return finished