from Singleton import Singleton
from Habilidade import Habilidade

class Habilidades(Singleton):
    __skillsAliados = [
        Habilidade('fireball', 5, 'saude', 'ofensivo'),
        Habilidade('rasengan', 5, 'saude', 'ofensivo'),
        Habilidade('earthball', 5, 'saude', 'ofensivo'),
        Habilidade('waterball', 5, 'saude', 'ofensivo'),
        Habilidade('melee', 50, 'saude', 'ofensivo'),
        Habilidade('boost', 5, 'ataque', 'suporte')
        ]
    __skillsInimigos = [
        Habilidade('fireball', 5, 'saude', 'ofensivo'),
        Habilidade('rasengan', 5, 'saude', 'ofensivo'),
        Habilidade('earthball', 5, 'saude', 'ofensivo'),
        Habilidade('waterball', 5, 'saude', 'ofensivo'),
        Habilidade('melee', 50, 'saude', 'ofensivo'),
        Habilidade('boost', 5, 'ataque', 'suporte')
        ]
    
    @property
    def skillsAliados(cls):
        return cls.__skillsAliados
    
    @property
    def skillsInimigos(cls):
        return cls.__skillsInimigos
    
    