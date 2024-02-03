import pygame, sys, random
from pygame.locals import *

pygame.init()

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# window
WINDOWWIDTH = 600
WINDOWHEIGHT = 600
window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Snake')
window.fill(WHITE)
pygame.display.update()

# snake
playerSize = 20
playerY = 100
playerX = 300
player = []
player.append(pygame.rect.Rect(playerX, playerY, playerSize, playerSize))

#food
ateFood = False
FOODSIZE = 20
food = []
food.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

# other
mainClock = pygame.time.Clock()
FPS = 4
Running = True
fpsTicked = False

# score
score = 0
score_font = pygame.font.Font(None, 30)
score_position = [10, 10]

# movement variables
direction = ''

MOVESPEED = 2

# draw text
def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, RED)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# game over
font = pygame.font.Font('freesansbold.ttf', 60)
def game_over():
    drawText('GAME OVER', font, window, (WINDOWWIDTH / 6), (WINDOWHEIGHT / 2))
    pygame.display.update()
    
# exit
def terminate():
    pygame.quit()
    sys.exit()

# X an Y axis change
def ChangeXandY(direction, playerX, playerY, playerSize):
    if direction == 'LEFT':
        playerX -= (playerSize + 2)
    elif direction == 'RIGHT':
        playerX += (playerSize + 2)
    elif direction == 'UP':
        playerY -= (playerSize + 2)
    else:
        playerY += (playerSize + 2)
    return playerX, playerY

# actually moving lol
def move(player, playerX, playerY):
    player.append(pygame.rect.Rect(playerX, playerY, playerSize, playerSize))
    return player

# game loop
while Running:
    window.fill(WHITE)
    fpsTicked = False
    # events
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                terminate()
            if not fpsTicked:
                if event.key == K_LEFT or event.key == K_a:
                    if direction != 'RIGHT':
                        direction = 'LEFT'
                        fpsTicked = True
                if event.key == K_RIGHT or event.key == K_d:
                    if direction != 'LEFT':
                        direction = 'RIGHT'
                        fpsTicked = True
                if event.key == K_UP or event.key == K_w:
                    if direction != 'DOWN':
                        direction = 'UP'
                        fpsTicked = True
                if event.key == K_DOWN or event.key == K_s:
                    if direction != 'UP':
                        direction = 'DOWN'
                        fpsTicked = True
    
    #print(direction)
    playerX, playerY = ChangeXandY(direction, playerX, playerY, playerSize)
    

    # out of window
    for i in player:
        if i.top > WINDOWHEIGHT:
            if i == player[len(player) - 1]:
                playerY = 1
            i = pygame.rect.Rect(playerX, 1, playerSize, playerSize)
        if i.top < 0:
            if i == player[len(player) - 1]:
                playerY = WINDOWHEIGHT - 1
            i = pygame.rect.Rect(playerX, WINDOWHEIGHT - 1, playerSize, playerSize)
        if i.right < 0:
            if i == player[len(player) - 1]:
                playerX = WINDOWWIDTH - 1
            pygame.rect.Rect(WINDOWWIDTH - 1, playerY, playerSize, playerSize)
        if i.left > WINDOWWIDTH:
            if i == player[len(player) - 1]:
                playerX = 1
            pygame.rect.Rect(1, playerY, playerSize, playerSize)
    
    # food
        if i.colliderect(food[0]):
            ateFood = True
            score += 1
            food.remove(food[0])
            food.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))
    pygame.draw.rect(window, GREEN, food[0])

    # self bump
    for a in range(4, len(player)):
        if player[0] == player[a]:
            game_over()
            Running = False
    
    player = move(player, playerX, playerY)

    if not ateFood:
        player.remove(player[0])
    for i in player:
        pygame.draw.rect(window, BLACK, i)
    
    # score
    score_surface = score_font.render(str(score), 1, (0, 0, 0))
    window.blit(score_surface, score_position)

    if ateFood and (score % 3) == 0:
        FPS += 2
    ateFood = False
        
    pygame.display.update()
    mainClock.tick(FPS)

# quit after loosing
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                terminate()
