import pygame
class Back():
    def __init__(self,imagem, x_hit, y_hit, hit_largura, hit_altura):
        self.__clicked = False
        self.__imagem = imagem
        self.__lugar = lugar
        self.__x_hit = x_hit
        self.__y_hit = y_hit
        self.__hitbox = pygame.Rect(x_hit, y_hit, hit_largura, hit_altura)

    @property
    def clicked(self):
        return self.__clicked

    @clicked.setter
    def clicked(self, novo_clicked: bool):
        self.__clicked = novo_clicked

    @property
    def hitbox(self):
        return self.__hitbox

    @property
    def imagem(self):
        return self.__imagem

'''
back() foi isolado do resto para ser melhorado posteriormente
objetivo é ser um objeto para facilitar a inclusao em diferentes "telas"
    def back(self,click):
        #temp = os.getcwd().split(os.path.sep)
        #temp.remove("View")
        #temp = os.path.sep.join(temp)
        #caminho = os.path.join(temp, "assets")
        #imagem_back = pygame.image.load(os.path.join(caminho, 'back_buttom.png')).convert()
        #imagem_back = pygame.transform.scale(imagem_back, (50, 50))
        #back_rect = imagem_back.get_rect()
        #back_rect_center = (750, 550)
        hit_back = pygame.Rect(750, 450, 50, 50)
        #self.__tela.blit(imagem_back,back_rect_center)
        if hit_back.collidepoint(click):
            return True
        return False
'''