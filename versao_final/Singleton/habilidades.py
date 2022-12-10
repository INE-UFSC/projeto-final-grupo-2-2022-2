from Singleton.Singleton import Singleton

class Habilidades(Singleton):
    __skills = [
        ['fireball', 5, 'saude', 'ofensivo'],
        ['rasengan', 5, 'saude', 'ofensivo'],
        ['earthball', 5, 'saude', 'ofensivo'],
        ['waterball', 5, 'saude', 'ofensivo'],
        ['boost', 5, 'ataque', 'suporte']
        ]
    __classesEHabilidades = {
        'mago': ['fireball', 'rasengan', 'waterball'],
        'orc': ['earthball', 'melee'],
        'goblin': ['melee'],
        'troll': ['melee'],
        
    }
    
    @property
    def skills(cls):
        return cls.__skills
    
    