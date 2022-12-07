from Model.Acao import Acao
from Model.Personagem import Personagem

from Controller.Jogo import Jogo

from Singleton.Singleton import Singleton

magos = ['']*3
orcs = ['']*3
time = ['']*3
inimigos = ['']*3
acoes = []

for i in Singleton().skills:
    acoes.append(Acao(*i))

for i in range(3):
    shift = 0
    if i == 1:
        shift = 100
    
    orcs[i] = Personagem(nome = 'Mateus' + str(i), 
                         nivel = 1,
                         tecnicas = acoes, 
                         classe = 'troll')


    magos[i] = Personagem(nome = 'Joao' + str(i), 
                          nivel = 10,
                          tecnicas = [acoes[i-1], acoes[i]], 
                          classe = 'mago')
                          
    # save.add(magos[i])


jogo = Jogo()

# !!!!! Parâmetros são temporários 
# Time deve ser armazenado em serialização
# Inimigos devem vir do mapa
jogo.run(magos, orcs)