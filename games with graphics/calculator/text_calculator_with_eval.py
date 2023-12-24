import sys

print('Welcome to the calculator')

def solving_equation():
    equation = input('Please input your equation\n')
    result = ''

    try:
        result = eval(equation)
    except:
        if result == '':
            result = 'Please enter a valid equation'
    finally:
        return(str(result))

def play_again():
    print(solving_equation())
    if not input('Do you want to play again? "Y"es or "N"o\n').lower().startswith('y'):
        sys.exit()

while True:
    play_again()
