import PySimpleGUI as sg
from Singleton.Constantes import Constantes

class Menu():
    def __init__(self) -> None:
        self.__container = []
        self.__screenSize = Constantes().screenSize
    
    def draw(self, comandos:list):
        self.__container = []
        self.__container.append([sg.VPush()])

        for i in comandos:
            self.__container.append(
                [sg.Button(
                    button_text = i.upper(),
                    key = i,
                    size = (30, 1.2),
                    use_ttk_buttons= True,
                    pad = 30,
                )
            ])

        self.__container.append([sg.VPush()])
        
        self.__window = sg.Window(
            title = "Menu", 
            layout = self.__container, 
            font = ("Helvetica", 14),
            size = self.__screenSize,
            element_justification='c',
            resizable = True,
            finalize = True
        )

    def setScreenSize(self):
        if isinstance(self.__window, sg.Window):
            self.__screenSize = self.__window.size
            Constantes().screenSize = self.__screenSize
            print(self.__screenSize, Constantes().screenSize)

    def main(self) -> bool:
        self.draw(['Play', 'Options', 'Quit'])
        run = True
        while run:
            event, values = self.__window.read()
            self.setScreenSize()

            if event == sg.WIN_CLOSED or event == 'Quit':
                run = False
            
            if event == 'Options':
                self.__window.close()
                self.draw(['Vídeo', 'Áudio', 'Teclado e Mouse', 'Voltar'])

            if event == 'Play':
                self.__window.close()
                return True
            
            if event == 'Voltar':
                self.__window.close()
                self.draw(['Play', 'Options', 'Quit'])

    