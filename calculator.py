import math

def start():
    no1 = input('First number: ')
    no2 = input('Second number: ')
    operator = input('Operator (+, -, *, /): ')

    try:
        no1 = float(no1)
        no2 = float(no2)
    except ValueError:
        print('Error: Invalid input')
        start()

    if operator == '+':
        ans = no1 + no2
        print("Answer: " + str(round(ans, 3)))
    elif operator == '-':
        ans = no1 - no2
        print("Answer: " + str(round(ans, 3)))
    elif operator == '*':
        ans = no1 * no2
        print("Answer: " + str(round(ans, 3)))
    elif operator == '/':
        if no2 != 0:
            ans = no1 / no2
            print("Answer: " + str(round(ans, 3)))
        else:
            print("Error: Division by zero")
            start()
    else:
        print("Error: Invalid operator")
        start()

    qn = input('Do you want to restart? (y/n): ')
    if qn == 'y':
        start()
    elif qn == 'n':
        print('Bye')
    else:
        print('Invalid input. Exiting...')

start()
