ALGORITHM: str = "MINIMAX"

LEVEL_TO_ALGORITHM = {
    "LEVEL1": "BFS",
    "LEVEL2": "Local Search",
    "LEVEL3": "Minimax"
}

# DEFINE COLOR
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
WALL_DEEP_BLUE = (25, 25, 166)
WALL_ELECTRIC_BLUE = (0, 153, 255)
WALL_PURPLE = (93, 63, 211)


FOOD_YELLOW = (255, 255, 0)        # Bright classic yellow
FOOD_WHITE = (255, 255, 255)       # Clean white dots
FOOD_ORANGE = (255, 192, 76)       #


# DEFINE MAP
SIZE_WALL: int = 40
DEFINE_WIDTH: int = 6
BLOCK_SIZE: int = SIZE_WALL // 2

# Entity
EMPTY = 0
WALL = 1
FOOD = 2
MONSTER = 3

# Setup screen
WIDTH: int = 1200
HEIGHT: int = 600
FPS: int = 500

MARGIN = {
    "TOP": 0,
    "LEFT": 0
}


# IMAGE
IMAGE_GHOST = [ "images/Inky.png","images/Clyde.png","images/Blinky.png", "images/Pinky.png"]
IMAGE_PACMAN = ["images/1.png", "images/2.png", "images/3.png", "images/4.png"]