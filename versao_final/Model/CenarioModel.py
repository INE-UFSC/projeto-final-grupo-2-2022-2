from View.Cenario import Cenario

class CenarioModel():
    def __init__(self, lugar:Cenario, x_hit, y_hit, hit_largura,hit_altura):
        self.__clicked = False
        self.__lugar = lugar
        self.__x_hit = x_hit
        self.__y_hit = y_hit
        self.__hitbox = pygame.Rect(x_hit, y_hit,hit_largura, hit_altura)

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
    def cenario(self):
        return self.__lugar