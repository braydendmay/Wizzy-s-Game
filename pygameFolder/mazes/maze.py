import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 640, 480
TILE_SIZE = 40
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE  = (0, 0, 255)
GREEN = (0, 255, 0)

# Maze layout (1 = wall, 0 = path, G = goal)
maze = [
    "111111111111",
    "1P0000000001",
    "111011111101",
    "100010000001",
    "101110111101",
    "1000001000G1",
    "111111111111"
]

# Player starting position
player_x, player_y = 1, 1

clock = pygame.time.Clock()

def draw_maze():
    for y, row in enumerate(maze):
        for x, tile in enumerate(row):
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if tile == "1":
                pygame.draw.rect(screen, BLACK, rect)
            elif tile == "G":
                pygame.draw.rect(screen, GREEN, rect)
            elif tile == "P":
                continue  # We'll draw the player separately

def move_player(dx, dy):
    global player_x, player_y
    new_x = player_x + dx
    new_y = player_y + dy
    if maze[new_y][new_x] != "1":
        player_x, player_y = new_x, new_y

# Main game loop
running = True
while running:
    screen.fill(WHITE)
    draw_maze()

    # Draw player
    player_rect = pygame.Rect(player_x * TILE_SIZE, player_y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
    pygame.draw.rect(screen, BLUE, player_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        move_player(-1, 0)
    if keys[pygame.K_RIGHT]:
        move_player(1, 0)
    if keys[pygame.K_UP]:
        move_player(0, -1)
    if keys[pygame.K_DOWN]:
        move_player(0, 1)

    # Check win condition
    if maze[player_y][player_x] == "G":
        print("You reached the goal! 🎉")
        pygame.time.wait(2000)
        running = False

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
sys.exit()
