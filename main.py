import math
import random
import sys

import pygame
from pygame import mixer

# Intialize the pygame
pygame.init()

# create the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Background
background = pygame.image.load('background.png')

# Sound
mixer.music.load("background.wav")
mixer.music.play(-1)
abilitySound = mixer.Sound("ability.wav")
bulletSound = mixer.Sound("laser.wav")
explosionSound = mixer.Sound("explosion.wav")

# Caption and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Colors
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Player
playerImg = pygame.image.load('player.png')
playerX = (screen_width / 2)#370
playerY = (screen_height - 120)#480
playerX_change = 0
ability_is_avalible = False
happened_once = False

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
enemy_speed = 1

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, (screen_width - 64)))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(enemy_speed)
    enemyY_change.append(40)

# Bullet

# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = (screen_height - 120)
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

# Ability
number_of_abilities = 0
ability_text_color = WHITE
ability_font = pygame.font.Font('freesansbold.ttf', 15)
ability_text = ability_font.render(f"{number_of_abilities} ABILITY/IES READY, PRESS X", True, ability_text_color)

# Explosion, testing
class Explosion(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		for num in range(1, 6):
			img = pygame.image.load(f"exp{num}.png")
			img = pygame.transform.scale(img, (100, 100))
			self.images.append(img)
		self.index = 0
		self.image = self.images[self.index]
		self.rect = self.image.get_rect()
		self.rect.center = [x + 25, y]
		self.counter = 0

	def update(self):
		explosion_speed = 4
		#update explosion animation
		self.counter += 1

		if self.counter >= explosion_speed and self.index < len(self.images) - 1:
			self.counter = 0
			self.index += 1
			self.image = self.images[self.index]

		#if the animation is complete, reset animation index
		if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
			self.kill()


explosion_group = pygame.sprite.Group()

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)

def terminate():
    pygame.quit()
    sys.exit()


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, WHITE)
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, WHITE)
    screen.blit(over_text, (200, 250))

def game_won_text():
    won_text = over_font.render("YOU WON", True, WHITE)
    screen.blit(won_text, (200, 250))

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def ability():
    abilitySound.play()
    for a in range(5):
        screen.fill(ORANGE)
        pygame.display.update()
        pygame.time.wait(50)
        screen.fill(YELLOW)
        pygame.display.update()
        pygame.time.wait(50)
    for i in range(num_of_enemies):
        enemyX[i] = random.randint(0, screen_width - 64)
        enemyY[i] = random.randint(50, 150)

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill(BLACK)
    # Background Image
    screen.blit(background, (0, 0))
    #screen.blit(ability_text, (600, 500))


    # Explosion another stuff i dont understand
    explosion_group.draw(screen)
    explosion_group.update()
	
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            terminate()

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                terminate()
            if event.key == pygame.K_x and number_of_abilities > 0:
                ability()
                number_of_abilities -= 1
            if event.key == pygame.K_f:
                mixer.music.load("easteregg.wav")
                mixer.music.play(-1)
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletSound.play()
                    # Get the current x cordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Ability and enemy speed
    if (score_value % 10) == 0 and score_value != 0 and not happened_once:
        number_of_abilities += 1
        enemy_speed += 1
        happened_once = True

    if (score_value % 5) != 0:
        happened_once = False

    #if number_of_abilities > 0:
    #    screen.blit(ability_text, (600, 500))

    # Winnin
    if score_value == 60:
        game_won_text()
        pygame.display.update()
        mixer.music.load("celebration.wav")
        mixer.music.play(-1)
        break
        
    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy Movement
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > (screen_height - 160):
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = enemy_speed
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= (screen_width - 64):
            enemyX_change[i] = enemy_speed * -1
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion = Explosion(bulletX , bulletY)
            explosion_group.add(explosion)
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, screen_width - 64)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, testY)
    screen.blit(ability_text, (550, 500))
    pygame.display.update()


# Quit after winning or loosing
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                terminate()
