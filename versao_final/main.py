from Model.Personagem import magos, orcs

from Controller.Jogo import Jogo



jogo = Jogo()

# !!!!! Parâmetros são temporários 
# Time deve ser armazenado em serialização
# Inimigos devem vir do mapa
jogo.run(magos, orcs)