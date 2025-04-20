import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Draw X with Rectangles")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)

# Function to draw an X
def draw_x(surface, color, x, y, size):
    thickness = 10  # Thickness of the rectangles
    pygame.draw.rect(surface, color, (x, y, thickness, size))
    pygame.draw.rect(surface, color, (x, y, size, thickness))
    pygame.draw.rect(surface, color, (x + size - thickness, y, thickness, size))
    pygame.draw.rect(surface, color, (x, y + size - thickness, size, thickness))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill(white)

    # Draw the X
    draw_x(screen, black, 350, 250, 100)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
