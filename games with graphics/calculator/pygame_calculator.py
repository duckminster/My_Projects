import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 300, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Calculator")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)

# Define font
font = pygame.font.Font(None, 36)

# Initialize calculator variables
expression = ""
result = ""

# Function to update the display
def update_display():
    pygame.draw.rect(screen, white, (0, 0, width, height))  # Clear the screen
    pygame.draw.rect(screen, gray, (20, 50, 260, 50))  # Display area

    text_surface = font.render(expression, True, black)
    screen.blit(text_surface, (30, 60))

    result_surface = font.render(result, True, black)
    screen.blit(result_surface, (30, 120))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_RETURN:
                try:
                    result = str(eval(expression))
                except:
                    result = "Error"
                expression = ""
            elif event.key == pygame.K_BACKSPACE:
                expression = expression[:-1]
            else:
                expression += event.unicode

    update_display()
    pygame.display.flip()
    pygame.time.Clock().tick(30)
