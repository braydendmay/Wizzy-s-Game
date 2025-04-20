import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jumping with Gravity")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Player settings
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - player_size
player_velocity_y = 0
jump_strength = -15
gravity = 1
ground_level = HEIGHT - player_size

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if key[pygame.K_d] == True:
            player_x += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_y == ground_level:
                player_velocity_y = jump_strength

    # Apply gravity
    player_velocity_y += gravity
    player_y += player_velocity_y

    # Check for collision with the ground
    if player_y >= ground_level:
        player_y = ground_level
        player_velocity_y = 0

    # Clear screen
    screen.fill(WHITE)

    # Draw player
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
