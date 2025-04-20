import pygame
import sys
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))

sky_surface = pygame.image.load("sky-background.jpg")
path_surface = pygame.image.load('stone_path.jpg')
sky_surface = pygame.transform.scale(sky_surface, (800,600))
path_surface = pygame.transform.scale(path_surface, (800,100))

slime = pygame.image.load('blue-slime.png')
slime = pygame.transform.scale(slime, (100,100))
slime_x_pos = 800

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #screen.blit(sky_surface,(0,-100))
    #screen.blit(path_surface,(0,500))
    slime_x_pos -= 4
    if slime_x_pos < -100: slime_x_pos = 800
    screen.blit(slime, (slime_x_pos,450))

    pygame.display.update()
    clock.tick(60)