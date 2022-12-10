from Controller.Controller import Controller

class Loop:
    def __init__(self) -> None:
        self.__controller = Controller()

    def iniciar(self):
        run = True
        while run:
            play = self.__controller.rodaMenu()
            if play:
                pass