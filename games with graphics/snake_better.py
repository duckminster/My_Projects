import sys, pygame, random, time
from dataclasses import dataclass
from enum import Enum
from copy import copy

# inits
pygame.init()
pygame.font.init()

# global variables
WINDOWHEIGHT = 800
WINDOWWIDTH = 1000

# difficulty settings
# easy              ->  10
# normal            ->  25
# hard              ->  40
# a lil harder      ->  60
# very hard         ->  120
DIFFICULTY = 40

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# setting up window
window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Snake - Updated')
window.fill(BLACK)

# score
score = 0
score_font = pygame.font.Font(None, 30)
score_position = [(WINDOWWIDTH - 30), 10]
score_position2 = [WINDOWWIDTH / 2, WINDOWHEIGHT / 2]

# game over
def game_over():
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('YOU DIED', True, RED)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (WINDOWWIDTH/2, WINDOWHEIGHT/4)
    window.fill(BLACK)
    window.blit(game_over_surface, game_over_rect)
    score_surface = score_font.render(str(score), 1, WHITE)
    window.blit(score_surface, score_position2)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()

# other variables
mainClock = pygame.time.Clock()


@dataclass
class Coord:
    x: int
    y: int


class Direction (Enum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3


def is_opposite (one: Direction, two: Direction):
    return (
        (one == Direction.LEFT and two == Direction.RIGHT) or
        (one == Direction.RIGHT and two == Direction.LEFT) or
        (one == Direction.UP and two == Direction.DOWN) or
        (one == Direction.DOWN and two == Direction.UP)
    )


def direction_from_key (key):
    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        return Direction.LEFT
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        return Direction.RIGHT
    if event.key == pygame.K_UP or event.key == pygame.K_w:
        return Direction.UP
    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
        return Direction.DOWN
    return None

class Snake:

    INITIAL_LENGTH = 10
    BODY_SIZE = 20
    STEP_SIZE = 10

    def __init__ (self, position, direction):
        self.direction = direction
        self.body = [ Coord (position.x - self.STEP_SIZE * index, position.y) for index in range (self.INITIAL_LENGTH) ]

    def change_direction (self, direction):
        if direction and not is_opposite (self.direction, direction):
            self.direction = direction

    def move (self, food):
        head = copy (self.body [0])
        match self.direction:
            case Direction.LEFT:
                head.x -= self.STEP_SIZE
            case Direction.RIGHT:
                head.x += self.STEP_SIZE
            case Direction.UP:
                head.y -= self.STEP_SIZE
            case Direction.DOWN:
                head.y += self.STEP_SIZE

        if head.x < 0: head.x += WINDOWWIDTH
        if head.x > WINDOWWIDTH: head.x -= WINDOWWIDTH
        if head.y < 0: head.y += WINDOWHEIGHT
        if head.y > WINDOWHEIGHT: head.y -= WINDOWHEIGHT

        head_rect = pygame.Rect (head.x, head.y, self.BODY_SIZE, self.BODY_SIZE)
        food_rect = pygame.Rect (food.position.x, food.position.y, food.FOOD_SIZE, food.FOOD_SIZE)
        ate = head_rect.colliderect(food_rect)

        self.body.insert (0, head)
        if not ate: self.body.pop ()

        return ate

    def suggest_direction(self, food):
        head = copy(self.body[0])

        if head.y < food.position.y: return Direction.DOWN
        if head.y > food.position.y + food.FOOD_SIZE: return Direction.UP
        if head.x < food.position.x: return Direction.RIGHT
        if head.x > food.position.x + food.FOOD_SIZE: return Direction.LEFT
        return None


    def draw_player (self, window):
        for position in self.body:
            pygame.draw.rect(window, GREEN, pygame.Rect(position.x, position.y, self.BODY_SIZE, self.BODY_SIZE))

    def draw_computer (self, window):
        for position in self.body:
            pygame.draw.rect(window, BLUE, pygame.Rect(position.x, position.y, self.BODY_SIZE, self.BODY_SIZE))

    def collides (self):
        head = self.body [0]
        head_rect = pygame.Rect (head.x, head.y, self.BODY_SIZE, self.BODY_SIZE)
        for chunk in self.body [3:]:
            chunk_rect = pygame.Rect(chunk.x, chunk.y, self.BODY_SIZE, self.BODY_SIZE)
            if head_rect.colliderect(chunk_rect):
                return True
        return False


# snake variables
snake = Snake (Coord (WINDOWWIDTH/2, WINDOWHEIGHT/2), Direction.RIGHT)
computer = Snake (Coord (WINDOWWIDTH/3, WINDOWHEIGHT/3), Direction.LEFT)

# computer movement
# def computer_dir_change():

# exit
def terminate():
    pygame.quit()
    sys.exit()

# food
class Food:
    FOOD_SIZE = 20

    def __init__(self, position):
        self.position = position

    def move(self):
        self.position = Coord (
            random.randint(0, WINDOWWIDTH - self.FOOD_SIZE - 1),
            random.randint(0, WINDOWHEIGHT - self.FOOD_SIZE - 1))

    def draw(self, window):
        pygame.draw.rect(window, RED, pygame.Rect(self.position.x, self.position.y, self.FOOD_SIZE, self.FOOD_SIZE))


# food object
food = Food(Coord (WINDOWWIDTH/2, WINDOWHEIGHT/2))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                terminate()

            snake.change_direction(direction_from_key(event.key))

    ate = snake.move (food)
    if ate:
        score += 1
        food.move ()
    computer.change_direction(computer.suggest_direction(food))
    if computer.move(food):
        score -= 1
        food.move()

    window.fill(BLACK)

    food.draw (window)
    snake.draw_player (window)
    computer.draw_computer (window)

    score_surface = score_font.render(str(score), 1, WHITE)
    window.blit(score_surface, score_position)

    pygame.display.update()

    if snake.collides (): game_over ()

    # FPS
    pygame.time.Clock().tick(DIFFICULTY)
