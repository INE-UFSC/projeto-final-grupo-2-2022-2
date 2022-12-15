from Model.Personagem import Personagem
from Model.Habilidade import Habilidade
from Singleton.habilidades import Habilidades
from DAO.PersonagemDAO import PersonagemDAO

aliados = [
    Personagem('mago', 1, [Habilidade(*i) for i in Habilidades().skills[0:2]], nome='Pedro'),
    Personagem('assassin', 1, [Habilidade(*i) for i in Habilidades().skills[1:3]], nome='Matias'),
    Personagem('healer', 1, [Habilidade(*i) for i in Habilidades().skills[2:4]], nome='Hugo')
]

dao = PersonagemDAO()
for i in aliados:
    dao.add(i)

import pickle as pkl

objects = []
with (open("Nivel.pkl", "rb")) as openfile:
    while True:
        try:
            objects.append(pkl.load(openfile))
        except EOFError:
            break

from DAO.JogoDAO import JogoDAO
dao = JogoDAO()
dao.add(1)

print(objects)