# Calculator
import sys
        
print('''Welcome to calculator, please input your equation''')

def get_numbers():
    a = input('Please enter first number')

    while True:
        try:
            a = float(a)
        except ValueError:
            a = input('Please enter a number')
        else:
            break

    b = input('Please enter the second number')

    while True:
        try:
            b = float(b)
        except ValueError:
            b = input('Please enter a number')
        else:
            break

    return a, b

def make_the_calculation(a, b):
    while True:
        print('''What operation do you want to do?
                 1 - addition
                 2 - subtraction
                 3 - multiplication
                 4 - division''')

        try:
            operation = int(input())

            match operation:
                case 1:
                    return a + b
                case 2:
                    return a - b
                case 3:
                    return a * b
                case 4:
                    if b != 0:
                        return a / b
                    else:
                        print('Cannot divide by zero')
                        continue
                case _:
                    print('Please enter a valid choice')
                    continue

        except ValueError:
            print('Please enter a valid option')
            continue

def play_again():
    print('Do you want to play again? ("Y"es or "N"o)')
    if not input().lower().startswith('y'):
        sys.exit()

while True:
    a, b = get_numbers()
    print(make_the_calculation(a, b))
    play_again()

