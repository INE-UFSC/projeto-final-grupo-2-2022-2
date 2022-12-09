from View.BatalhaView import BatalhaView
from View.Menu import Menu
from View.Mapa import Mapa
from Model.Batalha import Batalha
from Model.Personagem import Personagem
from Model.CenarioModel import CenarioModel
from View.CenarioBatalha import CenarioBatalha
from Singleton.Constantes import Constantes
from Controller.Loop import Loop
from Controller.JogoDAO import JogoDAO
from Controller.PersonagemDAO import PersonagemDAO

class Jogo:
    def __init__(self):
        self.__save_nivel = JogoDAO()
        self.__nivel = self.__save_nivel.get()
        self.__save_aliados = PersonagemDAO()
        self.__aliados = self.__save_aliados.get_all()
        self.save()

    def save(self):
        self.__save_nivel.add(self.__nivel)
        for i in self.__aliados:
            i.fim_da_batalha(self.__nivel)
            self.__save_aliados.add(i)

    # Parâmetros temporários -> inimigos devem ser
    # gerados pelo mapa e aliados provenientes
    # de serialização

    def run(self):
        menu = Menu()
        play = menu.main()

        if play:
            # Mapa deve retornar os inimigos da fase clicada
            # Mapa também deve retornar o cenário a ser enviado à batalha

            # 

            loop = Loop()
            # enviando a lista de aliados
            # como argumento para o loop,
            # que já instancia a batalha
            fim = loop.main(self.__aliados)
            if fim == 1:
                self.__nivel += 1
                self.save()
            elif fim == 0:
                self.save()
