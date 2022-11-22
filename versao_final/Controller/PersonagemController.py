from Model.Personagem import Personagem
from View.PersonagemView import PersonagemView

class PersonagemController:
    def __init__(self, view: PersonagemView):
        self.__view = view

    def set_health(self, health:int):
        self.__view.set_health(health)

    def set_image(self, classe:str):
        self.__view.set_image(classe)