import pygame
from Snake import Snake
from Apple import Apple
from Constants import FPS, TITLE, WIDTH, HEIGHT, TILE_SIZE, BACKGROUND_COLORS

class Game:
    def __init__(self):
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT], pygame.RESIZABLE, 32, 0, 0)
        self.game_over_font = pygame.font.Font(None, 74)
        self.snake = Snake()
        self.apple = Apple()
        self.frame_time = 0
        self.running = True
        self.game_over = False


    def _poll_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.game_over = False
                if event.scancode == pygame.KSCAN_ESCAPE:
                    self.running = False
                elif event.scancode == pygame.KSCAN_UP:
                    self.snake.change_direction("UP")
                elif event.scancode == pygame.KSCAN_DOWN:
                    self.snake.change_direction("DOWN")
                elif event.scancode == pygame.KSCAN_LEFT:
                    self.snake.change_direction("LEFT")
                elif event.scancode == pygame.KSCAN_RIGHT:
                    self.snake.change_direction("RIGHT")


    def _check_is_game_over(self) -> None:
        if not self.snake.is_eaten_by_itself() and not self.snake.is_out_of_board():
            return

        score = self.snake.get_score()
        self.snake.reset()

        game_over_text = self.game_over_font.render(f"Game Over! Score: {score}", True, (255, 255, 255))
        game_over_text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.blit(game_over_text, game_over_text_rect)
        pygame.display.flip()
        self.game_over = True


    def _render_frame(self) -> None:
        self.screen.fill((0, 0, 0))
        for x in range(0, WIDTH, TILE_SIZE):
            for y in range(0, HEIGHT, TILE_SIZE):
                color = BACKGROUND_COLORS[(x + y) // TILE_SIZE % 2]
                pygame.draw.rect(self.screen, color, (x, y, TILE_SIZE, TILE_SIZE))

        self.apple.draw(self.screen)
        self.snake.draw(self.screen)


    def run(self) -> None:
        while self.running:
            start_time = pygame.time.get_ticks()

            self._poll_events()
            if self.game_over:
                continue

            end_time = pygame.time.get_ticks()
            delta_time = end_time - start_time
            self.frame_time += delta_time

            if self.frame_time < (1000 // FPS):
                continue

            self.frame_time = 0

            self.snake.move()
            self._check_is_game_over()
            if self.game_over:
                continue

            if self.snake.check_apple(self.apple):
                self.snake.grow()
                self.apple.reset()

            self._render_frame()
            pygame.display.flip()
