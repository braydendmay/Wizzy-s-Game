import pygame
import random

# Constants
TILE_SIZE = 20
GRID_WIDTH = 31  # Must be odd
GRID_HEIGHT = 21  # Must be odd

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)

# Setup display
pygame.init()
WIDTH = GRID_WIDTH * TILE_SIZE
HEIGHT = GRID_HEIGHT * TILE_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Random Maze Generator")

# Maze grid: 1 = wall, 0 = path
maze = [[1 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

def carve_maze(x, y):
    dirs = [(0, -2), (2, 0), (0, 2), (-2, 0)]
    random.shuffle(dirs)
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 < nx < GRID_WIDTH and 0 < ny < GRID_HEIGHT and maze[ny][nx] == 1:
            maze[ny][nx] = 0
            maze[y + dy // 2][x + dx // 2] = 0
            carve_maze(nx, ny)

def generate_maze():
    maze[1][1] = 0
    carve_maze(1, 1)
    maze[GRID_HEIGHT - 2][GRID_WIDTH - 2] = 0  # Goal

def draw_maze():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if maze[y][x] == 1:
                pygame.draw.rect(screen, BLACK, rect)
            else:
                pygame.draw.rect(screen, WHITE, rect)
    # Draw player and goal
    pygame.draw.rect(screen, RED, (1 * TILE_SIZE + 5, 1 * TILE_SIZE + 5, TILE_SIZE - 10, TILE_SIZE - 10))
    pygame.draw.rect(screen, GREEN, ((GRID_WIDTH - 2) * TILE_SIZE + 5, (GRID_HEIGHT - 2) * TILE_SIZE + 5, TILE_SIZE - 10, TILE_SIZE - 10))

# Generate and draw
generate_maze()
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)
    draw_maze()
    pygame.display.flip()
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
