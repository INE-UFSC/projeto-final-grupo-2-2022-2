from View.Sprite import Sprite

class PersonagemController:
    def __init__(self, view: Sprite):
        self.__view = view

    @property
    def view(self) -> Sprite:
        return self.__view

    @view.setter
    def view(self, novo):
        self.__view = novo

    def set_health(self, health:int):
        self.__view.set_health(health)

    def set_image(self, classe:str):
        self.__view.set_image(classe)