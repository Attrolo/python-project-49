from random import randint


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


MIN = 0
MAX = 10


def is_even(number):
    return number % 2 == 0 and 'yes' or 'no'


def get_game():
    question = randint(MIN, MAX)
    correct_answer = is_even(question)
    return question, correct_answer
