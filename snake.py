import pygame

pygame.init()

FPS = 8
WIDTH = 1280
HEIGHT = 720
TITLE = "Snake"
TILE_SIZE = 40
BACKGROUND_COLORS = [(20, 240, 20), (20, 200, 20)]
SNAKE_COLOR = (0, 0, 255)
APPLE_COLOR = (200, 20, 20)

class Snake:
    def __init__(self) -> None:
        self.reset()
    
    def reset(self) -> None:
        self.body = [(1, 1), (2, 1), (3, 1)]
        self.direction = (1, 0)

    def change_direction(self, direction) -> None:
        if direction == "UP" and self.direction != (0, 1):
            self.direction = (0, -1)
        elif direction == "DOWN" and self.direction != (0, -1):
            self.direction = (0, 1)
        elif direction == "LEFT" and self.direction != (1, 0):
            self.direction = (-1, 0)
        elif direction == "RIGHT" and self.direction != (-1, 0):
            self.direction = (1, 0)

    def move(self) -> None:
        head = self.body[-1]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.body.pop(0)
        self.body.append(new_head)

    def grow(self) -> None:
        head = self.body[-1]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.body.append(new_head)
    
    def check_collision(self) -> bool:
        head = self.body[-1]
        for x, y in self.body[:-1]:
            if head == (x, y):
                return True

        return False

    def check_boundaries(self) -> bool:
        head = self.body[-1]
        if head[0] < 0 or head[0] >= WIDTH // TILE_SIZE or head[1] < 0 or head[1] >= HEIGHT // TILE_SIZE:
            return True

        return False

    def check_apple(self, apple) -> bool:
        head = self.body[-1]
        return head == apple.position

    def get_score(self) -> int:
        return len(self.body) - 3

    def draw(self, screen) -> None:
        for i, (x, y) in enumerate(self.body):
            color = tuple(map(lambda x: x * i // len(self.body), SNAKE_COLOR))
            pygame.draw.rect(screen, color, (x * TILE_SIZE + TILE_SIZE // 4, y * TILE_SIZE + TILE_SIZE // 4, TILE_SIZE // 2, TILE_SIZE // 2))

class Apple:
    def __init__(self):
        self.reset()

    def reset(self):
        self.position = (pygame.time.get_ticks() % (WIDTH // TILE_SIZE), pygame.time.get_ticks() % (HEIGHT // TILE_SIZE))

    def draw(self, screen):
        pygame.draw.circle(screen, APPLE_COLOR, (self.position[0] * TILE_SIZE + TILE_SIZE // 2, self.position[1] * TILE_SIZE + TILE_SIZE // 2), TILE_SIZE // 2)

snake = Snake()
apple = Apple()

pygame.display.set_caption(TITLE)
screen = pygame.display.set_mode([1280, 720], pygame.RESIZABLE, 32, 0, 0)
game_over = False
totalDelta = 0

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
