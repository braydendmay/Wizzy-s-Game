import time
import random
import os
import pygame
clear = lambda: os.system('cls')
pygame.init()
clock = pygame.time.Clock()
#Game window
screen = pygame.display.set_mode((800,600))

grid_line_vert_1 = pygame.Rect((305,100, 15, 300))
grid_line_vert_2 = pygame.Rect((455,100, 15, 300))
grid_line_horz_1 = pygame.Rect((240, 300, 300, 15))
grid_line_horz_2 = pygame.Rect((240, 168, 300, 15))

grid_outer_left_top = pygame.Rect((190, 56, 100, 100))
grid_outer_left_middle = pygame.Rect((190, 190, 100, 100))
grid_outer_left_bottom = pygame.Rect((190, 325, 100, 100))

grid_center_top = pygame.Rect((335, 56, 100,100))
grid_center_middle = pygame.Rect((335, 190, 100,100))
grid_center_bottom = pygame.Rect((335, 325, 100,100))

grid_outer_right_top = pygame.Rect((480, 56, 100,100))
grid_outer_right_middle = pygame.Rect((480, 190, 100,100))
grid_outer_right_bottom = pygame.Rect((480, 325, 100,100))
run = True
while run:
    mouse_pos = pygame.mouse.get_pos()
    screen.fill((255,255,255))
    pygame.draw.rect(screen, (0,0,0), grid_line_vert_1)
    pygame.draw.rect(screen, (0,0,0), grid_line_vert_2)
    pygame.draw.rect(screen, (0,0,0), grid_line_horz_1)
    pygame.draw.rect(screen, (0,0,0), grid_line_horz_2)

    pygame.draw.rect(screen, (255,0,0), grid_outer_left_top)
    pygame.draw.rect(screen, (255,0,0), grid_outer_left_middle)
    pygame.draw.rect(screen, (255,0,0), grid_outer_left_bottom)

    pygame.draw.rect(screen, (255,0,0), grid_center_top)
    pygame.draw.rect(screen, (255,0,0), grid_center_middle)
    pygame.draw.rect(screen, (255,0,0), grid_center_bottom)

    pygame.draw.rect(screen, (255,0,0), grid_outer_right_top)
    pygame.draw.rect(screen, (255,0,0), grid_outer_right_middle)
    pygame.draw.rect(screen, (255,0,0), grid_outer_right_bottom)

    if grid_outer_right_top.colliderect(mouse_pos):
        if event.type == pygame.MOUSEBUTTONUP:
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEMOTION:
            print(mouse_pos)
    pygame.display.update()
    clock.tick(80)