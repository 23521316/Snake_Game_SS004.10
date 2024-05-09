import pygame
import random
from enum import Enum
from collections import namedtuple

pygame.init()

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

Point = namedtuple('Point', 'x, y')

BLOCK_SIZE = 20

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 110, 255)
RED = (200, 0, 0)
class Menu:
    def __init__(self, surface, options):
        self.surface = surface
        self.options = options
        self.selected_option = 0

    def draw(self):
        height = len(self.options) * font.get_height()
        y = (self.surface.get_height() - height) // 2
        for i, option in enumerate(self.options):
            text = font.render(option, True, WHITE)
            rect = text.get_rect(center=(self.surface.get_width() // 2, y + i * font.get_height()))
            if i == self.selected_option:
                pygame.draw.rect(self.surface, BLUE1, rect)
            self.surface.blit(text, rect)

    def select_next_option(self):
        self.selected_option = (self.selected_option + 1) % len(self.options)

    def select_previous_option(self):
        self.selected_option = (self.selected_option - 1) % len(self.options)

    def get_selected_option(self):
        return self.options[self.selected_option]

class SnakeGame:
    def __init__(self, w=1000, h=800):
        self.w = w
        self.h = h
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('SNAKE_GAME_23521682_23521316_23520610')
        # initialise game settings
        # direction
        self.direction = Direction.RIGHT
        # snake
        self.head = Point(self.w / 2, self.h / 2)
        self.snake = [
            self.head,
            Point(self.head.x - BLOCK_SIZE, self.head.y),
            Point(self.head.x - 2 * BLOCK_SIZE, self.head.y)
        ]
        # food
        self.food = None
        # clock
        self.clock = pygame.time.Clock()
        # score
        self.score=0;
    def _place_food(self):
        x = random.randint(0, (self.w - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (self.h - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.snake:
            self._place_food()

if __name__ == '__main__':
    game = SnakeGame()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
