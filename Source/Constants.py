from typing import List, Tuple

FPS: int = 8
TITLE: str = "Snake"
WIDTH: int = 1280
HEIGHT: int = 720
TILE_SIZE: int = 40
HALF_TILE_SIZE: int = TILE_SIZE // 2
HORIZONTAL_TILE_COUNT: int = WIDTH // TILE_SIZE
VERTICAL_TILE_COUNT: int = HEIGHT // TILE_SIZE
BACKGROUND_COLORS: List[Tuple[int, int, int]] = [(20, 240, 20), (20, 200, 20)]
SNAKE_COLOR: Tuple[int, int, int] = (0, 0, 255)
APPLE_COLOR: Tuple[int, int, int] = (200, 20, 20)
