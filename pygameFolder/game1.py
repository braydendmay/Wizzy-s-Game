import pygame
import time
from Adventure_Game.Adventure_Text import *
clock = pygame.time.Clock()
pygame.init()
font = pygame.font.SysFont('Comic Sans MS', 15)
# Game window
screen = pygame.display.set_mode((800,600))

enemy = pygame.Rect((0, 450, 50, 50))

player_surf = pygame.image.load('blue-slime2-small.png').convert_alpha()
player = player_surf.get_rect(midbottom = (50,475))
player = pygame.Rect((0, 450, 50, 50))

floor = pygame.Rect((0, 500, 820, 100))

setting_surf = pygame.image.load('setting_cog_small.png').convert_alpha()
setting_surf = pygame.transform.scale(setting_surf, (50,50))
setting_rect = setting_surf.get_rect(midbottom = (770,50))

store_surf = pygame.Rect((100,400,100,100))
#store_rect = pygame.image.load(' image goes here ').convert()

blacksmith_surf = pygame.Rect((220,400,100,100))
#blacksmith_rect = pygame.image.load(' image goes here ').convert()

# Jump and gravity variables
y_velocity = 0
gravity = 0.5
jump_strength = -10
is_jumping = False

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

walls = pygame.sprite.Group()
wall1 = Wall(400, 300, 50, 50)
#wall2 = Wall(300, 200, 50, 50)
#walls.add(wall1)
#walls.add(wall2)


weapon1 = pygame.Rect((300, 400, 50, 50))
health_potion = pygame.Rect((380, 400, 50, 50))

def display_stats():
    font = pygame.font.SysFont('Comic Sans MS', 20)
    show_health = font.render(f'Health: {health}', True, (255,255,255))
    font = pygame.font.SysFont('Comic Sans MS', 15)
    show_level_xp = font.render(f'Player Level: {player_level} Next level: {player_exp}/{exp_progress}', True, (255,255,255))
    show_perks = font.render(f'Available Perks: {perk_count}', True, (255,255,255))
    show_gold = font.render(f'Gold: {gold}g', True, (255,255,255))
    screen.blit(show_health, (355,0))
    screen.blit(show_level_xp, (4,0))
    screen.blit(show_perks, (4,20))
    screen.blit(show_gold, (4,40))
    screen.blit(player_surf,player)
    screen.blit(setting_surf, setting_rect)

def key_binds():

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
        player.x -= 3
    if key[pygame.K_d]:
        player.x += 3

    # Jumping
    if key[pygame.K_SPACE] and not is_jumping:
        y_velocity = jump_strength
        is_jumping = True

    # Apply gravity
    y_velocity += gravity
    player.y += y_velocity

enemy_chance = random.randint(1,16)

new_scene = 0
run = True
while run:
    #health = font.render(f'Health: {health}', True, (255,255,255))
    screen.fill((0, 0, 0))
    if new_scene == 1:
        pygame.draw.rect(screen, (255, 255, 255), floor)
        pygame.draw.rect(screen, (0,255,0), store_surf)
        pygame.draw.rect(screen, (0,255,0), weapon1)
        pygame.draw.rect(screen, (255,0,0), health_potion)

    elif new_scene == 0:
        pygame.draw.rect(screen,(0,0,255), store_surf)
        pygame.draw.rect(screen,(255,0,0), blacksmith_surf) 
        #pygame.draw.rect(screen,(255,0,0), setting_surf) 
        pygame.draw.rect(screen, (255, 255, 255), floor)
        walls.draw(screen)
    elif new_scene == 2:
        pygame.draw.rect(screen, (255, 255, 255), floor)
        
        print(enemy_chance)
        #if enemy_chance >= 0 and enemy_chance <=3:
        walls.draw(screen)

    display_stats()
    
    
    key_binds()
    

    # Collision with the floor
    if player.colliderect(floor):
        player.bottom = floor.top
        y_velocity = 0
        is_jumping = False

    # Enter store
    if player.colliderect(store_surf) and key[pygame.K_RETURN]:
        test()
        if new_scene == 1:
            new_scene = 0
        elif new_scene == 0:
            new_scene = 1
        time.sleep(.3) 
    #Buy Weapon 
    if weapon1.collidepoint(mouse_pos):
        if event.type == pygame.MOUSEBUTTONUP:
            inner_test()
            print(print_weapon)
            time.sleep(1)
    if health_potion.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONUP:
            give_potion()
            time.sleep(.3) 
    
    if player.x >= 780:
        player.x = 780
        if new_scene != 2:
            new_scene = 2
            player.x -= 760
            print(player.x)
            print('mines')
            
    if player.x <= 0:
        player.x = 0
        #if key[pygame.K_RETURN] and player.x <= 10:
        if new_scene == 2:
            new_scene = 0
            player.x = 780
            
            

    if setting_rect.collidepoint(mouse_pos):
        if event.type == pygame.MOUSEBUTTONUP:
            screen.fill((103,84,77))
            display_stats() 
    
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #if event.type == pygame.MOUSEMOTION:
        #    print(event.pos)
        

    pygame.display.update()
    clock.tick(60)

pygame.quit()
