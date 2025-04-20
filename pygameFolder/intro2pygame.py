import pygame
import time
clock = pygame.time.Clock()
pygame.init()

# Game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
# but you can just do this --> screen = pygame.display.set_mode((800,600))
player = pygame.Rect((0,450, 50, 50)) #(location x, location y, sized width, size hieght)

object = pygame.Rect((400,300, 20, 100))
floor = pygame.Rect((0,500,800,100))

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 255, 255))  # White color for the wall
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Create a group to hold wall sprites
walls = pygame.sprite.Group()

# Create wall instances
wall1 = Wall(100, 100, 200, 20)
wall2 = Wall(300, 200, 20, 200)

# Add walls to the group
walls.add(wall1)
walls.add(wall2)




run = True
while run: #game loop

    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 0, 0), player)
    pygame.draw.rect(screen, (255,255,255),object)
    pygame.draw.rect(screen, (255,255,255),floor)

    key = pygame.key.get_pressed()
    walls.draw(screen)
    if key[pygame.K_a] == True:
        player.move_ip(-1,0)
    elif key[pygame.K_d] == True:
        player.move_ip(1,0)
    elif key[pygame.K_w] == True:
        player.move_ip(0,-1)
    elif key[pygame.K_s] == True:
        player.move_ip(0,1)

    if player.colliderect(wall1):
            player.y += 1
    if player.colliderect(floor):
            player.y -= 1
    if player.colliderect(wall2):
        player.x -= 1
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update() #<---refreshes the screen for any screen changes
    clock.tick(200)
pygame.quit()