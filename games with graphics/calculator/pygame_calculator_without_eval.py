import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 600, 600
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
first_part = ""
second_part = ""
operation = ""

# Text for selecting operation
operation_types = "Operation types:\n1 = addition\n2 = subtraction\n3 = division\n4 = multiplication"
tutorial = 'Enter first number, then press "enter"'

# Drawing multiline text
def multiline_text(multiline_text):
    text_lines = multiline_text.split('\n')
    for i, line in enumerate(text_lines):
        text_surface = font.render(line, True, black)
        text_rect = text_surface.get_rect(center=(width // 2, height // 2 + i * 40))
        screen.blit(text_surface, text_rect)

def text_display(text, font, surface, x, y):
    textobj = font.render(text, 1, black)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Function to update the display
def update_display():
    pygame.draw.rect(screen, white, (0, 0, width, height))  # Clear the screen
    pygame.draw.rect(screen, gray, (20, 50, 400, 50))  # Display area

    expression_surface = font.render(expression, True, black)
    screen.blit(expression_surface, (30, 60))

    result_surface = font.render(str(result), True, black)
    screen.blit(result_surface, (30, 120))

# Main game loop
while True:
    update_display()
    text_display(tutorial, font, screen, 30, 160)
    multiline_text(operation_types)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_RETURN:
                if first_part == "" and expression != "":
                    first_part = expression.replace(" ", "")
                    expression = ""
                    tutorial = 'Enter operation type'
                    pygame.display.update()
                elif first_part != "" and operation == "":
                    operation = expression
                    expression = ""
                    tutorial = 'Enter the second number'
                else:
                    second_part = expression.replace(" ", "")
                    expression = ""
                    tutorial = 'Press enter to restart'

                if result != "":
                    tutorial = 'Enter first number'
                    result = ""
                    first_part = ""
                    expression = ""
                    operation = ""
                    second_part = ""

                if first_part != "" and operation != "" and second_part != "":

                    try:
                        operation = int(operation)

                        match operation:

                            case 1:
                                result = (float(first_part) + float(second_part))

                            case 2:
                                result = (float(first_part) - float(second_part))

                            case 3:
                                if float(second_part) != 0.0:
                                    result = (float(first_part) // float(second_part))
                                else:
                                    result = 'Error, cannot divide by 0'

                            case 4:
                                result = (float(first_part) * float(second_part))

                            case _:
                                result = 'Non valid operation type choice'
                    except:
                        result = "Error"

            elif event.key == pygame.K_BACKSPACE:
                expression = expression[:-1]
            else:
                expression += event.unicode

    pygame.display.update()