from combatClasses.mago import Mago


from Batalha import Batalha
from Acao import Acao, acoes
from BatalhaController import BatalhaController
import pygame
from personagem_view import PersonagemView

pygame.init()
window = pygame.display.set_mode((900, 500), pygame.RESIZABLE)

# PersonagemViewos a serem mostrados na tela
mago = Mago('aaaa', 5, 100, acoes)
mago1 = Mago('aaaa', 5, 100, acoes)
mago2 = Mago('aaaa', 5, 100, acoes)
mago3 = Mago('aaaa', 5, 100, acoes)
mago4 = Mago('aaaa', 5, 100, acoes)
mago5 = Mago('aaaa', 5, 100, acoes)


# Lista de PersonagemViewos
time = [
    PersonagemView(window, mago, 100, 200),
    PersonagemView(window, mago4, 200, 100),
    PersonagemView(window, mago5, 200, 300)
]

inimigos = [
    PersonagemView(window, mago1, 700, 200),
    PersonagemView(window, mago2, 600, 100),
    PersonagemView(window, mago3, 600, 300)
]

jogo = BatalhaController(time, inimigos, window)


def update_window(window):
    window.fill((255, 255, 255))
    for PersonagemView in time:
        PersonagemView.draw()
    for PersonagemView in inimigos:
        PersonagemView.draw()
    pygame.display.update()
    

def main(window):
    fps = 60
    clock = pygame.time.Clock()
    allies, enemies = [i.char for i in time], [i.char for i in inimigos]
    battle = Batalha(allies, enemies)
    

    run = True
    finished = False
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            finished = jogo.watch(battle, event, finished)
            if event.type == pygame.QUIT:
                return False

        update_window(window)

            # if not attack:
            #     rand = Random()
            #     targetPos = rand.randint(0, 2)
            #     target = enemies[targetPos]
            #     x, y = char.rect.centerx - 10, char.rect.centery-10
            #     fireball = PersonagemView(window, 'fireball.png', x, y, 20, 20)
            #     team.append(fireball)
            #     attack = True
            # else:
            #     fireball.rect.x += x_speed
            #     match targetPos:
            #         case 0:
            #             pass
            #         case 1:
            #             fireball.rect.y -= x_speed/5
            #         case 2:
            #             fireball.rect.y += x_speed/5

            #     if fireball.rect.collidepoint(target.rect.center):
            #         attack = False
            #         team.remove(fireball)
            #         print("char2 -5 vida")
            



if __name__ == "__main__":
    main(window)