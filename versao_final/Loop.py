from Controller.Controller import Controller
import pygame
class Loop:
    def __init__(self) -> None:
        self.__controller = Controller()
        self.__fps = 60
        self.__clock = pygame.time.Clock()

    def iniciar(self):
        run = True
        mapa = False
        menu = True
        batalha = False
        while run:
            self.__clock.tick(self.__fps)

            if menu:
                run, mapa = self.__controller.rodaMenu()
            if mapa:
                menu = False
                run, batalha = self.__controller.rodaMapa()
            if batalha:
                mapa = False
                run, mapa = self.__controller.rodaBatalha()
                