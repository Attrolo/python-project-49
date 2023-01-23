from random import randint
from random import choice


MESSAGE_GAME = 'What is the result of the expression?'


def calc(NUM1, NUM2, ACTION):
    if ACTION == '+':
        return NUM1 + NUM2
    elif ACTION == '-':
        return NUM1 - NUM2
    elif ACTION == '*':
        return NUM1 * NUM2
    else:
        return 'please choose another action: "+, - or *"'


def get_game():
    ACTION = ('+', '-', '*')
    NUM1 = randint(1, 10)
    NUM2 = randint(1, 10)
    ACTION = choice(ACTION)
    answer = calc(NUM1, NUM2, ACTION)
    question = f'{NUM1} {ACTION} {NUM2}'
    return question, answer
