import pygame
class Botao():
    def __init__(self,texto,centro_largura,centro_altura):
        self.__clicked = False
        self.__cor_fundo = (138, 8, 8) #vermelho
        self.__cor_texto = (0,0,0) #preto
        self.__font = pygame.font.Font('freesansbold.ttf', 32)
        self.__texto = self.__font.render(texto, False, self.__cor_texto)
        self.__rect_texto = self.__texto.get_rect()
        self.__rect_texto.center = (centro_largura,centro_altura)
        self.__rect = pygame.Rect(0, 0,200,50)
        self.__rect.center = (centro_largura,centro_altura)

    @property
    def clicked(self) -> bool:
        return self.__clicked

    @clicked.setter
    def clicked(self, novo_clicked: bool):
        self.__clicked = novo_clicked

    @property
    def rect(self):
        return self.__rect

    @property
    def cor_fundo(self):
        return self.__cor_fundo

    @property
    def texto(self):
        return self.__texto

    @property
    def rect_texto(self):
        return self.__rect_texto

