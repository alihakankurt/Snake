import pygame
from Snake import Snake
from Apple import Apple
from Constants import FPS, WIDTH, HEIGHT, TITLE, TILE_SIZE, BACKGROUND_COLORS

if __name__ == "__main__":
    pygame.init()

    pygame.display.set_caption(TITLE)
    screen = pygame.display.set_mode([1280, 720], pygame.RESIZABLE, 32, 0, 0)
    game_over = False
    totalDelta = 0

    snake = Snake()
    apple = Apple()

    running = True
    while running:
    start = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        snake.change_direction("UP")
    elif keys[pygame.K_DOWN]:
        snake.change_direction("DOWN")
    elif keys[pygame.K_LEFT]:
        snake.change_direction("LEFT")
    elif keys[pygame.K_RIGHT]:
        snake.change_direction("RIGHT")
    elif game_over:
        continue

    game_over = False
    end = pygame.time.get_ticks()
    delta = end - start
    if totalDelta + delta < 1000 / FPS:
        totalDelta += delta
        continue

    totalDelta = 0

    snake.move()
    if snake.check_collision() or snake.check_boundaries():
        score = snake.get_score()
        snake.reset()

        font = pygame.font.Font(None, 74)
        text = font.render(f"Game Over! Score: {score}", True, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()
        game_over = True
        continue

    if snake.check_apple(apple):
        snake.grow()
        apple.reset()

    screen.fill((0, 0, 0))
    for x in range(0, WIDTH, TILE_SIZE):
        for y in range(0, HEIGHT, TILE_SIZE):
            color = BACKGROUND_COLORS[(x + y) // TILE_SIZE % 2]
            pygame.draw.rect(screen, color, (x, y, TILE_SIZE, TILE_SIZE))

    apple.draw(screen)
    snake.draw(screen)

    pygame.display.flip()

    pygame.quit()
