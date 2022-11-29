import PySimpleGUI as sg

class Menu():
    def __init__(self) -> None:
        self.__container = []
        self.__window = None
    
    def draw(self):
        self.__container.append([sg.VPush()])
        
        comandos = ['play', 'options', 'quit']

        for i in comandos:
            self.__container.append(
                [sg.Button(
                    button_text = i.upper(),
                    key = i,
                    size = (30, 1.2),
                    use_ttk_buttons= True,
                    pad = 30
                )
            ])

        self.__container.append([sg.VPush()])
        
        self.__window = sg.Window(
            title = "Menu Principal", 
            layout = self.__container, 
            font = ("Helvetica", 14),
            size = (1000, 500),
            element_justification='c',
            resizable=True
        )


    def main(self) -> bool:
        self.draw()
        run = True
        while run:
            event, values = self.__window.read()
            if event == sg.WIN_CLOSED or event == 'quit':
                run = False
            
            if event == 'play':
                self.__window.close()
                return True
    