import pygame

class InputHandler:
    def __init__(self, display:pygame.Surface) -> None:
        self.__events = pygame.event.get()
        self.__display = display

    def handleClick(self):
        for event in self.__events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                return pygame.mouse.get_pos()
    
    def handleScreenEvents(self):
        for event in self.__events:
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.VIDEORESIZE:
                self.__display = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                self.__display.fill((255, 255, 255))
                
        return True