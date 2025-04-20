import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
TILE_SIZE = 40
MAZE = [
    "##########",
    "#        #",
    "# ###### #",
    "# #    # #",
    "# # ## # #",
    "# # ## # #",
    "# #    # #",
    "# ###### #",
    "#        #",
    "########G#"
]
MAZE = [
    "###################"
    "#                 #"
    "################# #"
]
ROWS = len(MAZE)
COLS = len(MAZE[0])

WIDTH = COLS * TILE_SIZE
HEIGHT = ROWS * TILE_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)

# Setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")

# Player start position
player_pos = [1, 1]

def draw_maze():
    for y, row in enumerate(MAZE):
        for x, tile in enumerate(row):
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if tile == '#':
                pygame.draw.rect(screen, BLACK, rect)
            elif tile == 'G':
                pygame.draw.rect(screen, GREEN, rect)
            else:
                pygame.draw.rect(screen, WHITE, rect)

def draw_player():
    x, y = player_pos
    rect = pygame.Rect(x * TILE_SIZE + 5, y * TILE_SIZE + 5, TILE_SIZE - 10, TILE_SIZE - 10)
    pygame.draw.rect(screen, RED, rect)

def is_valid_move(x, y):
    return 0 <= x < COLS and 0 <= y < ROWS and MAZE[y][x] != '#'

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)
    draw_maze()
    draw_player()
    pygame.display.flip()
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    x, y = player_pos
    if keys[pygame.K_LEFT] and is_valid_move(x - 1, y):
        player_pos[0] -= 1
    if keys[pygame.K_RIGHT] and is_valid_move(x + 1, y):
        player_pos[0] += 1
    if keys[pygame.K_UP] and is_valid_move(x, y - 1):
        player_pos[1] -= 1
    if keys[pygame.K_DOWN] and is_valid_move(x, y + 1):
        player_pos[1] += 1

    # Check for goal
    if MAZE[player_pos[1]][player_pos[0]] == 'G':
        print("🎉 You reached the goal!")
        pygame.time.wait(2000)
        running = False

pygame.quit()
sys.exit()
