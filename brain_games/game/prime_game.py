from random import randint


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


MIN = 0
MAX = 50


def is_prime(number):
    divider = 2
    while number % divider != 0:
        divider += 1
    return divider == number


def get_game():
    number = randint(MIN, MAX)
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = number
    return question, correct_answer
