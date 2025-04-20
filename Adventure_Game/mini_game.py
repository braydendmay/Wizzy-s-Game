def mini_game_func():
    import pygame
    import random
    import sys

    pygame.init()
    WIDTH, HEIGHT = 600, 800
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Dodge the Falling Objects")
    clock = pygame.time.Clock()

    # Game variables
    player = pygame.Rect(WIDTH // 2 - 25, HEIGHT - 60, 50, 50)
    player_speed = 5
    falling_objects = []
    object_size = 30
    fall_speed = 5
    objects_to_spawn = 1
    round_over = False
    score = 0
    game_over = False
    font = pygame.font.SysFont(None, 48)

    # Colors
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)

    def spawn_objects(num):
        objs = []
        for _ in range(num):
            x = random.randint(0, WIDTH - object_size)
            y = -random.randint(40, 200)
            objs.append(pygame.Rect(x, y, object_size, object_size))
        return objs

    def draw_text(text, size, color, x, y, center=True):
        font_obj = pygame.font.SysFont(None, size)
        text_surface = font_obj.render(text, True, color)
        text_rect = text_surface.get_rect()
        if center:
            text_rect.center = (x, y)
        else:
            text_rect.topleft = (x, y)
        screen.blit(text_surface, text_rect)

    high_score = 0
    with open('score.txt', 'r') as source:
        for line in source:
            try:
                x = int(line)
                if x > high_score:
                    high_score = x
            except ValueError:
                pass
    print(WIDTH // 2 - 25)
    running = True
    while running:
        clock.tick(60)
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not game_over:
            # Player movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player.left > 0:
                player.x -= player_speed
            if keys[pygame.K_RIGHT] and player.right < WIDTH:
                player.x += player_speed

            # Update falling objects
            if not falling_objects:
                falling_objects = spawn_objects(objects_to_spawn)
                round_over = False

            for obj in falling_objects:
                obj.y += fall_speed
                pygame.draw.rect(screen, RED, obj)

                # Check collision
                if player.colliderect(obj):
                    game_over = True

            # Check if all objects are off screen
            if all(obj.top > HEIGHT for obj in falling_objects) and not round_over:
                objects_to_spawn += 1
                score += 1
                falling_objects = []
                round_over = True

            # Draw player
            pygame.draw.rect(screen, BLUE, player)

            # Draw score
            draw_text(f"Score: {score}", 36, BLACK, 10, 10, center=False)
            draw_text(f"High Score: {high_score}", 36, BLACK, 10, 30, center=False)

        else:
            draw_text("Game Over", 72, RED, WIDTH // 2, HEIGHT // 2 - 50)
            draw_text(f"Final Score: {score}", 48, BLACK, WIDTH // 2, HEIGHT // 2 + 10)
            draw_text("Press ESC to quit", 36, BLACK, WIDTH // 2, HEIGHT // 2 + 60)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                with open('score.txt', 'a') as destination:
                    try: 
                        score = str(score)
                        destination.write(score + '\n')
                    except ValueError:
                        pass
                running = False

        pygame.display.flip()

    pygame.quit()
    sys.exit()
