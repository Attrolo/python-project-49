from random import randint


MESSAGE_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(NUMBER):
    divider = 2
    while NUMBER % divider != 0:
        divider += 1
    return divider == NUMBER


def get_game():
    NUMBER = randint(1, 50)
    if is_prime(NUMBER):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = f'Question: {NUMBER}'
    return question, correct_answer
