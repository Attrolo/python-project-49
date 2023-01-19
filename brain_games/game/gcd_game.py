from random import randint


MESSAGE_GAME = 'Find the greatest common divisor of given numbers.'


def get_nod(a, b):
    while b > 0:
        c = a % b
        a = b
        b = c
    else:
        b = 1
    print(a)


def get_game():
    question = randint(1, 10)
    correct_answer = get_nod(question)
    return question, correct_answer
