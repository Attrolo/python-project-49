import prompt
from random import randint
from random import choice


def calc(num1, num2, action):
    if action == '+':
        return num1 + num2
    elif action == '-':
        return num1 - num2
    elif action == '*':
        return num1 * num2
    else:
        return 'please choose another action: "+, - or *"'


def get_game_calc():
    action = ('+', '-', '*')
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    action = choice(action)
    answer = calc(num1, num2, action)
    question = f'{num1}{action}{num2}'
    return question, answer
