import pygame, sys, time

# Inits
pygame.init()
pygame.font.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Screen variables
WINDOWWIDTH = 1000
WINDOWHEIGHT = 600
window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Pong Game')
window.fill(BLACK)

# Paddle class
class Paddle:
    HEIGHT = 60
    WIDTH = 10
    SPEED = 3
    SCORE_FONT = pygame.font.Font(None, 200)

    def __init__(self, x_pos, y_pos, score, score_x, score_y, color):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.score = score
        self.score_x = score_x
        self.score_y = score_y
        self.color = color

    def Move(self, keys, up_key, down_key):
        if keys[up_key] and self.y_pos > 0:  # Move up if within bounds
            self.y_pos -= self.SPEED
        if keys[down_key] and self.y_pos < WINDOWHEIGHT - self.HEIGHT:  # Move down if within bounds
            self.y_pos += self.SPEED

    def Draw_paddle(self):
        pygame.draw.rect(window, self.color, (self.x_pos, self.y_pos, self.WIDTH, self.HEIGHT))

    def Draw_score(self):
        score_surface = Paddle.SCORE_FONT.render(str(self.score), True, self.color)
        window.blit(score_surface, (self.score_x, self.score_y))

# Ball class
class Ball:
    SIZE = 20
    SPEED = 2
    blueBall = pygame.image.load("blueBall.png")
    redBall = pygame.image.load("redBall.png")
    blueRect = blueBall.get_rect()
    redRect = redBall.get_rect()
    scaled_image_blue = pygame.transform.scale(blueBall, (SIZE, SIZE))
    scaled_image_red = pygame.transform.scale(redBall, (SIZE, SIZE))

    def __init__(self, x_pos, y_pos, dir_x, dir_y):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.dir_x = dir_x
        self.dir_y = dir_y

    def Move(self):
        if self.dir_x == 'LEFT' and self.dir_y == 'UP':
            self.x_pos -= self.SPEED
            self.y_pos -= self.SPEED
        if self.dir_x == 'LEFT' and self.dir_y == 'DOWN':
            self.x_pos -= self.SPEED
            self.y_pos += self.SPEED
        if self.dir_x == 'RIGHT' and self.dir_y == 'UP':
            self.x_pos += self.SPEED
            self.y_pos -= self.SPEED
        if self.dir_x == 'RIGHT' and self.dir_y == 'DOWN':
            self.x_pos += self.SPEED
            self.y_pos += self.SPEED

    def Dir_change(self):
        if self.y_pos == WINDOWHEIGHT:
            self.dir_y = 'UP'
        if self.y_pos == 0:
            self.dir_y = 'DOWN'
        if pygame.Rect(self.x_pos, self.y_pos, self.SIZE, self.SIZE).colliderect(pygame.Rect(Player_1.x_pos, Player_1.y_pos, Player_1.WIDTH, Player_1.HEIGHT)):
            self.dir_x = 'LEFT'
            Player_1.score += 1
        if pygame.Rect(self.x_pos, self.y_pos, self.SIZE, self.SIZE).colliderect(pygame.Rect(Player_2.x_pos, Player_2.y_pos, Player_2.WIDTH, Player_2.HEIGHT)):
            self.dir_x = 'RIGHT'
            Player_2.score += 1

    def Draw_ball(self):
        if self.x_pos <= WINDOWWIDTH // 2:
            Ball.redRect.topleft = (self.x_pos, self.y_pos)
            window.blit(Ball.scaled_image_red, Ball.redRect)
        else:
            Ball.blueRect.topleft = (self.x_pos, self.y_pos)
            window.blit(Ball.scaled_image_blue, Ball.blueRect)


# Game over screen
def show_game_over():
    window.fill(BLACK)
    font = pygame.font.Font(None, 100)
    text = font.render("Game Over", True, WHITE)
    score_text = font.render(f"Player 1: {Player_1.score}  |  Player 2: {Player_2.score}", True, WHITE)

    window.blit(text, (WINDOWWIDTH // 2 - text.get_width() // 2, WINDOWHEIGHT // 3))
    window.blit(score_text, (WINDOWWIDTH // 2 - score_text.get_width() // 2, WINDOWHEIGHT // 2))

    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()

# All class objects
Player_1 = Paddle(WINDOWWIDTH - (Paddle.WIDTH + 10), WINDOWHEIGHT // 2, 0, 3 * (WINDOWWIDTH // 4), WINDOWHEIGHT // 3, BLUE)
Player_2 = Paddle(10, WINDOWHEIGHT // 2, 0, WINDOWWIDTH // 4, WINDOWHEIGHT // 3, RED)
Ball = Ball(WINDOWWIDTH // 2, WINDOWHEIGHT // 2, 'RIGHT', 'UP')

# Game loop
while True:
    pygame.time.delay(5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    Player_1.Move(keys, pygame.K_UP, pygame.K_DOWN)
    Player_2.Move(keys, pygame.K_w, pygame.K_s)

    window.fill(BLACK)

    Player_1.Draw_paddle()
    Player_2.Draw_paddle()
    Player_1.Draw_score()
    Player_2.Draw_score()

    Ball.Draw_ball()
    Ball.Move()
    Ball.Dir_change()

    # Check if a player misses
    if Ball.x_pos <= 0 or Ball.x_pos >= WINDOWWIDTH:
        show_game_over()

    pygame.display.flip()
