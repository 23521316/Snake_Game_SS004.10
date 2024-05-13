import pygame
import random
from enum import Enum
from collections import namedtuple

pygame.init()
pygame.mixer.init()
menuchoice=pygame.mixer.Sound(r"Sound\_menuchoice_sound.mp3")
entergame=pygame.mixer.Sound(r"Sound\_entergame_sound.mp3")
eatfood=pygame.mixer.Sound(r"Sound\_eat_food_sound.mp3")
specialfood=pygame.mixer.Sound(r"Sound\_special_food_sound.mp3")
gameover=pygame.mixer.Sound(r"Sound\_gameover_sound.mp3")
pygame.mixer.music.load(r"Sound\_theme_song.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1,)
class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

Point = namedtuple('Point', 'x, y')
font = pygame.font.Font('Roboto-Medium.ttf', 25)
BLOCK_SIZE = 20
SPECIAL_FOOD_SIZE = 30  

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 110, 255)
RED = (200, 0, 0)
YELLOW = (255, 255, 0) 
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
        menuchoice.play()
        self.selected_option = (self.selected_option + 1) % len(self.options)

    def select_previous_option(self):
        menuchoice.play()
        self.selected_option = (self.selected_option - 1) % len(self.options)

    def get_selected_option(self):
        entergame.play()
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
        self.food_counter = 0 
        # score
        self.score=0;
        self._place_food()
        self.menu = Menu(self.display, ["Easy", "Medium", "Hard"])
        self.game_started = False
        self.frame_rate = 10  # Default frame rate
        self.special_food = None
        self.special_food_timer = 0
        self.special_food_score = 0
        self.food_counter = 0  # Counter for eaten food
        
    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if not self.game_started:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        difficulty = self.menu.get_selected_option()
                        self.start_game(difficulty)
                    elif event.key == pygame.K_UP:
                        self.menu.select_previous_option()
                    elif event.key == pygame.K_DOWN:
                        self.menu.select_next_option()
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and self.direction != Direction.LEFT:
                        self.direction = Direction.RIGHT
                    elif event.key == pygame.K_LEFT and self.direction != Direction.RIGHT:
                        self.direction = Direction.LEFT
                    elif event.key == pygame.K_UP and self.direction != Direction.DOWN:
                        self.direction = Direction.UP
                    elif event.key == pygame.K_DOWN and self.direction != Direction.UP:
                        self.direction = Direction.DOWN
    def start_game(self, difficulty):
        # Initialize game settings based on difficulty
        if difficulty == "Easy":
            self.frame_rate = 5
        elif difficulty == "Medium":
            self.frame_rate = 10
        elif difficulty == "Hard":
            self.frame_rate = 15
        # Reset game state
        self.game_started = True
        self.head = Point(self.w / 2, self.h / 2)
        self.snake = [
            self.head,
            Point(self.head.x - BLOCK_SIZE, self.head.y),
            Point(self.head.x - 2 * BLOCK_SIZE, self.head.y)
        ]
        self.direction = Direction.RIGHT
        self.score = 0
        self._place_food()
        self.food_counter = 0  # Reset food counter when game starts

    def play_step(self):
        self._handle_input()
        if not self.game_started:
            self.display.fill(BLACK)
            self.menu.draw()
        else:
            self._move_snake()
            self._check_collision()
            self._update_ui()
        pygame.display.flip()
        self.clock.tick(self.frame_rate)  # Limit the frame rate here

        if self.score % 5 == 0 and self.score > 0 and not self.special_food and self.food_counter >= 5:
            self._place_special_food()
            self.special_food_timer = self.h
            #change timer
            self.special_food_score = 50
            self.food_counter = 0  # Reset food counter after placing special food
        if self.special_food:
            self.special_food_score -= 1
            self.special_food_timer -= self.w*0.02
            if self.special_food_timer <= 0:
                self.special_food = None
                self.special_food_score = 0
                
    def _place_food(self):
        x = random.randint(0, (self.w - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (self.h - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.snake:
            self._place_food()
        else:
            self.food_counter += 1  # Increment food counter when new food is placed
            
    def _place_special_food(self):
        x = random.randint(0, (self.w - SPECIAL_FOOD_SIZE) // SPECIAL_FOOD_SIZE) * SPECIAL_FOOD_SIZE
        y = random.randint(0, (self.h - SPECIAL_FOOD_SIZE) // SPECIAL_FOOD_SIZE) * SPECIAL_FOOD_SIZE
        self.special_food = Point(x, y)
        if self.special_food in self.snake or self.special_food == self.food:
            self._place_special_food()
        else:
            specialfood.play()
    def _move_snake(self):
        new_head = self.head
        if self.direction == Direction.RIGHT:
            new_head = Point(self.head.x + BLOCK_SIZE, self.head.y)
        elif self.direction == Direction.LEFT:
            new_head = Point(self.head.x - BLOCK_SIZE, self.head.y)
        elif self.direction == Direction.UP:
            new_head = Point(self.head.x, self.head.y - BLOCK_SIZE)
        elif self.direction == Direction.DOWN:
            new_head = Point(self.head.x, self.head.y + BLOCK_SIZE)
        self.head = new_head
        self.snake.insert(0, self.head)
    def _check_collision(self):
        if self.head in self.snake[1:] or not (0 <= self.head.x < self.w) or not (0 <= self.head.y < self.h):
            gameover.play()
            self._game_over()
            self.game_started = False
            self.food_counter = 0  # Reset food counter when game ends
            self.special_food = None  # Remove special food when game ends
            self.special_food_timer = 0
            self.special_food_score = 0
            return
        if self.head == self.food:
            eatfood.play()
            self.score += 1
            self._place_food()
        else:
            self.snake.pop()
        if self.special_food and self.head.x < self.special_food.x + SPECIAL_FOOD_SIZE and self.head.x + BLOCK_SIZE > self.special_food.x and self.head.y < self.special_food.y + SPECIAL_FOOD_SIZE and self.head.y + BLOCK_SIZE > self.special_food.y:
            self.score += self.special_food_score
            specialfood.play()
            self.special_food = None
            self.special_food_timer = 0
            self.special_food_score = 0
        
    def _update_ui(self):
        self.display.fill(BLACK)
        for pt in self.snake:
            pygame.draw.rect(self.display, BLUE1, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, BLUE2,
                             pygame.Rect(pt.x + 0.2 * BLOCK_SIZE, pt.y + 0.2 * BLOCK_SIZE, 0.6 * BLOCK_SIZE,
                                         0.6 * BLOCK_SIZE))
        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))
        if self.special_food:
            pygame.draw.rect(self.display, YELLOW, pygame.Rect(self.special_food.x, self.special_food.y, SPECIAL_FOOD_SIZE, SPECIAL_FOOD_SIZE))
            pygame.draw.rect(self.display, RED, pygame.Rect(0, 0, self.special_food_timer, 20))
        text = font.render('Score: ' + str(self.score), True, WHITE)
        self.display.blit(text, [10, 10])
        pygame.display.flip()
    def _game_over(self):
        self.display.fill(BLACK)
        game_over_text = font.render('GAME OVER', True, WHITE)
        score_text = font.render('Score: ' + str(self.score), True, WHITE)
        self.display.blit(game_over_text, [self.w // 2 - game_over_text.get_width() // 2, self.h // 2 - game_over_text.get_height() // 2])
        self.display.blit(score_text, [self.w // 2 - score_text.get_width() // 2, self.h // 2 + game_over_text.get_height() // 2])
        pygame.display.flip()
        pygame.time.wait(2000)
    def run(self):
        while True:
            self.play_step()


if __name__ == '__main__':
    game = SnakeGame()
    game.run()
    pygame.quit()
