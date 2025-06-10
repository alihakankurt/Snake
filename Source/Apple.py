import pygame
from Constants import WIDTH, HEIGHT, TILE_SIZE, HALF_TILE_SIZE, HORIZONTAL_TILE_COUNT, VERTICAL_TILE_COUNT, APPLE_COLOR

class Apple:
    def __init__(self):
        self.reset()

    def reset(self):
        x: int = pygame.time.get_ticks() % HORIZONTAL_TILE_COUNT
        y: int = pygame.time.get_ticks() % VERTICAL_TILE_COUNT
        self.position = (x, y)

    def draw(self, screen):
        x: int = self.position[0] * TILE_SIZE + HALF_TILE_SIZE
        y: int = self.position[1] * TILE_SIZE + HALF_TILE_SIZE
        pygame.draw.circle(screen, APPLE_COLOR, (x, y), HALF_TILE_SIZE)
