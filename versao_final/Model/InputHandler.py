import pygame
from View.Tela import Tela

class InputHandler:
    def __init__(self, tela:Tela) -> None:
        self.__events = pygame.event.get()
        self.__tela = tela

    def handleClick(self):
        for event in self.__events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                return pygame.mouse.get_pos()
    
    def handleScreenEvents(self):
        for event in self.__events:
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.VIDEORESIZE:
                self.__tela.display = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                self.__tela.display.fill((255, 255, 255))
                
        return True