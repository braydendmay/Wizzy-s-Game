import time
import random
import os
import pygame
clear = lambda: os.system('cls')
pygame.init()
clock = pygame.time.Clock()
#Game window
screen = pygame.display.set_mode((800,600))

#Gravity Variables
y_velocity = 0
gravity = 0.5
jump_strength = -10
is_jumping = False


def key_binds():

    global falling_rect
    global y_velocity
    global jump_strength
    global is_jumping
    global mouse_pos
    global key
    key = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()

    # Horizontal movement
    if key[pygame.K_a]:
        player_rect.x -= 3
    if key[pygame.K_d]:
        player_rect.x += 3

    # Jumping
    if key[pygame.K_SPACE] and not is_jumping:
        y_velocity = jump_strength
        is_jumping = True

    # Apply gravity
    y_velocity += gravity
    player_rect.y += y_velocity
    #num.y += y_velocity

player_rect = pygame.Rect((350, 250, 50, 50))

floor_rect = pygame.Rect((0, 599, 800, 1))
class Spike(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
num = 0
def random_pos(amount):
    global num
    global falling_rect
    pos = random.randint(20, 780)
    falling_rect= pygame.Rect((pos,0, 20, 50))
        
def spawn():
    global falling_rect
    global count
    random_pos(count)
    count += 1
count = 1
random_pos(count)
run = True
while run:
    screen.fill((255,255,255))
    #screen.blit(player_rect(400, 300))
    pygame.draw.rect(screen, (0, 0, 0), player_rect)
    pygame.draw.rect(screen, (0, 0, 0), floor_rect)
    spawn()   
    pygame.draw.rect(screen, (0,0,255), (f'{falling_rect}{num}'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    key_binds()
    if player_rect.colliderect(floor_rect): 
        player_rect.bottom = floor_rect.top
        y_velocity = 0
        is_jumping = False
    #if player_rect.bottom >= 550:
    #    print('Below')
    #    player_rect.y = 550
    pygame.display.update()
    clock.tick(80)
        
