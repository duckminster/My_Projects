import pygame, sys, time
from pygame.locals import *

pygame.init()

#okno setup
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animace')

#direction variables
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 4

#barvy
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

class Rectangle:

    def __init__ (self, position, size, color, direction):
        self.color = color
        self.direction = direction
        self.rectangle = pygame.Rect (*position, *size)

    def move (self):
        if self.direction == DOWNLEFT:
            self.rectangle.left -= MOVESPEED
            self.rectangle.top += MOVESPEED
        elif self.direction == DOWNRIGHT:
            self.rectangle.left += MOVESPEED
            self.rectangle.top += MOVESPEED
        elif self.direction == UPLEFT:
            self.rectangle.left -= MOVESPEED
            self.rectangle.top -= MOVESPEED
        elif self.direction == UPRIGHT:
            self.rectangle.left += MOVESPEED
            self.rectangle.top -= MOVESPEED
        else:
            halt ()

    def reverse_horizontal (self):
        if self.direction == DOWNLEFT:
            self.direction = DOWNRIGHT
        elif self.direction == DOWNRIGHT:
            self.direction = DOWNLEFT
        elif self.direction == UPLEFT:
            self.direction = UPRIGHT
        elif self.direction == UPRIGHT:
            self.direction = UPLEFT            
        else:
            halt ()

    def reverse_vertical (self):
        if self.direction == DOWNLEFT:
            self.direction = UPLEFT
        elif self.direction == DOWNRIGHT:
            self.direction = UPRIGHT
        elif self.direction == UPLEFT:
            self.direction = DOWNLEFT
        elif self.direction == UPRIGHT:
            self.direction = DOWNRIGHT
        else:
            halt ()

    def bounce (self, x_min, x_max, y_min, y_max):
        if self.rectangle.left < x_min or self.rectangle.right > x_max:
            self.reverse_horizontal ()
        if self.rectangle.top < y_min or self.rectangle.bottom > y_max:
            self.reverse_vertical ()

    def draw (self):
        pygame.draw.rect(windowSurface, self.color, self.rectangle)


boxes = [
    Rectangle ((300, 80), (50, 100), RED, UPRIGHT),
    Rectangle ((200, 320), (20, 20), GREEN, UPLEFT),
    Rectangle ((100, 150), (60, 60), BLUE, DOWNLEFT),
    Rectangle ((200, 320), (60, 80), BLACK, DOWNRIGHT)
]


#game loop
while True:
    #zkontrolovat quit event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #white pozadi
    windowSurface.fill(WHITE)

    for b in boxes:
        b.move ()
        b.bounce (0, WINDOWHEIGHT, 0, WINDOWWIDTH)
        b.draw ()


    #nakresli okno
    pygame.display.update()
    time.sleep(0.02)
