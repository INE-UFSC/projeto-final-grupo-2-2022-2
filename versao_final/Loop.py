from Controller.Controller import Controller
import pygame
class Loop:
    def __init__(self) -> None:
        self.__controller = Controller()
        self.__fps = 60
        self.__clock = pygame.time.Clock()

    def iniciar(self):
        run = True
        play = False
        while run:
            self.__clock.tick(self.__fps)

            if not play:
                run, play = self.__controller.rodaMenu()
                print(play)
            if play:
                run = self.__controller.rodaMapa()
                # run, end = self.__controller.rodaBatalha()
                