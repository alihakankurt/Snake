import pygame
from Constants import APPLE_COLOR, HALF_TILE_SIZE, TILE_SIZE, WIDTH, HEIGHT

class Apple:
    def __init__(self):
        self.reset()

    def reset(self):
        x: int = pygame.time.get_ticks() % (WIDTH // TILE_SIZE)
        y: int = pygame.time.get_ticks() % (HEIGHT // TILE_SIZE)
        self.position = (x, y)

    def draw(self, screen):
        x: int = self.position[0] * TILE_SIZE + HALF_TILE_SIZE
        y: int = self.position[1] * TILE_SIZE + HALF_TILE_SIZE
        pygame.draw.circle(screen, APPLE_COLOR, (x, y), HALF_TILE_SIZE)
