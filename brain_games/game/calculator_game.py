from random import randint
from random import choice


MESSAGE_GAME = 'What is the result of the expression?'


MIN = 0
MAX = 10


def calculator(num1, num2, action):
    if action == '+':
        return num1 + num2
    elif action == '-':
        return num1 - num2
    elif action == '*':
        return num1 * num2
    else:
        return 'please choose another action: "+, - or *"'


def get_game():
    action = ('+', '-', '*')
    num1 = randint(MIN, MAX)
    num2 = randint(MIN, MAX)
    action = choice(action)
    answer = calculator(num1, num2, action)
    question = f'{num1} {action} {num2}'
    return question, answer
