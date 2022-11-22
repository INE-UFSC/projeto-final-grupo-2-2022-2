from View.PersonagemView import PersonagemView

class PersonagemController:
    def __init__(self, view: PersonagemView):
        self.__view = view

    @property
    def view(self) -> PersonagemView:
        return self.__view

    @view.setter
    def view(self, novo):
        self.__view = novo

    def set_health(self, health:int):
        self.__view.set_health(health)

    def set_image(self, classe:str):
        self.__view.set_image(classe)