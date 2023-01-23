from random import randint


MESSAGE_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(NUMBER):
    return NUMBER % 2 == 0 and 'yes' or 'no'


def get_game():
    QUESTION = randint(1, 10)
    correct_answer = is_even(QUESTION)
    return QUESTION, correct_answer
