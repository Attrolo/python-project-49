from random import randint
from random import choice


MESSAGE_GAME = 'What number is missing in the progression?'


MIN = 0
MAX = 50
RANDOM_STEP_MIN = 2
RANDOM_STEP_MAX = 5


def get_progression():
    step = randint(RANDOM_STEP_MIN, RANDOM_STEP_MAX)
    lenght_progression = randint(5, 10)  # Минимальное значение по условию = 5
    first_number = randint(MIN, MAX)
    progression = []
    progression.append(first_number)
    i = 0
    while i < lenght_progression:
        first_number += step
        progression.append(first_number)
        i += 1
    return progression


def get_game():
    question = get_progression()
    correct_answer = choice(question)
    index = question.index(correct_answer)
    question[index] = '..'
    question = ' '.join(str(first_number) for first_number in question)
    return question, correct_answer
