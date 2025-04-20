import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Button Example")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Button class
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.font = pygame.font.Font(None, 36)

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)
        
        text_surface = self.font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False

# Create a button instance
button = Button(300, 250, 100, 50, "Click Me!", GREEN, (0, 200, 0))
button2 = Button(300, 50, 100, 50, "Click Me2!", GREEN, (0, 200, 0))
# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if button.is_clicked(event):
            print("Button clicked!")

    screen.fill(WHITE)
    button.draw(screen)
    button2.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()