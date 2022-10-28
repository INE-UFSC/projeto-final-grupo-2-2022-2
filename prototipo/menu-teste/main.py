import pygame
import os

WIDHT, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDHT, HEIGHT))
pygame.display.set_caption("Hello")
FPS = 60
SPEED = 3

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)



def draw_window(red, yellow):
    WIN.fill((100, 100, 100))
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a]: # LEFT
        yellow.x -= SPEED
    if keys_pressed[pygame.K_d]: # RIGHT
        yellow.x += SPEED
    if keys_pressed[pygame.K_s]: # DOWN
        yellow.y += SPEED
    if keys_pressed[pygame.K_w]: # UP
        yellow.y -= SPEED
        
def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT]: # LEFT
        red.x -= SPEED
    if keys_pressed[pygame.K_RIGHT]: # RIGHT
        red.x += SPEED
    if keys_pressed[pygame.K_DOWN]: # DOWN
        red.y += SPEED
    if keys_pressed[pygame.K_UP]: # UP
        red.y -= SPEED

def main():
    red = pygame.Rect(600, 100, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(300, 100, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        
        # if keys_pressed[pygame.K_]:
        #     yellow.x -= SPEED
        # if keys_pressed[pygame.K_a]:
        #     yellow.x -= SPEED
        # if keys_pressed[pygame.K_a]:
        #     yellow.x -= SPEED
        # if keys_pressed[pygame.K_a]:
        #     yellow.x -= SPEED
        

        draw_window(red, yellow)
    
    pygame.quit()

if __name__ == "__main__":
    main()