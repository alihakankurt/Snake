import pygame
from Constants import WIDTH, HEIGHT, TILE_SIZE, HALF_TILE_SIZE, HORIZONTAL_TILE_COUNT, VERTICAL_TILE_COUNT, SNAKE_COLOR

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

    def is_eaten_by_itself(self) -> bool:
        head = self.body[-1]
        for x, y in self.body[:-1]:
            if head == (x, y):
                return True

        return False

    def is_out_of_board(self) -> bool:
        head = self.body[-1]
        if head[0] < 0 or head[0] >= HORIZONTAL_TILE_COUNT or head[1] < 0 or head[1] >= VERTICAL_TILE_COUNT:
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
            pygame.draw.rect(screen, color, (x * TILE_SIZE + TILE_SIZE // 4, y * TILE_SIZE + TILE_SIZE // 4, HALF_TILE_SIZE, HALF_TILE_SIZE))
