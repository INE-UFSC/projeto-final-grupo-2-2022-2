from Model.Sprite import Sprite

class Animacao:
    def __init__(self) -> None:
        self.__progresso = 0
        self.__colidiu = False
        pass
    
    def executa(self, atacante:Sprite, alvo: Sprite, habilidade: Sprite):
        finished = False

        if not self.__colidiu :
            if self.__progresso < 10:
                atacante.rect.x += 2   

        if self.__progresso >= 10 and not self.__colidiu:
            self.__colidiu = habilidade.move(atacante.position, alvo.position, alvo.rect)

            if self.__progresso >= 10 and self.__progresso < 20:
                atacante.rect.x -= 2

            if self.__colidiu: 
                self.__progresso = 0
                habilidade.kill()

        if self.__colidiu:
            if self.__progresso == 0:
                alvo.rect.x += 4
                alvo.rect.y += 4
            if self.__progresso == 1:
                alvo.rect.x -= 4
                alvo.rect.y -= 4
                finished = True
                self.__colidiu = False
        
        self.__progresso += 1
        return finished

