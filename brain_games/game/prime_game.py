from random import randint


MESSAGE_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    divider = 2
    while number % divider != 0:
        divider += 1
    return divider == number


def get_game():
    number = randint(1, 50)
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = f'Question: {number}'
    return question, correct_answer
