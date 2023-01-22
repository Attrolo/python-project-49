from random import randint


MESSAGE_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime():
    question = randint(0, 100)
    i = 2  # Самое маленькое простое число = 2
    while question % i == 0:
        i += 1
        correct_answer = i == question and 'yes' or 'no'
    return question, correct_answer
