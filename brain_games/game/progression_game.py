from random import randint
from random import choice


MESSAGE_GAME = 'What number is missing in the progression?'


def get_progression():
    STEP = randint(2, 5)
    LENGHT_PROGRESSION = randint(5, 10)  # Минимальное значение по условию = 5
    FIRST_NUMBER = randint(0, 50)
    progression = []
    progression.append(FIRST_NUMBER)
    i = 0
    while i < LENGHT_PROGRESSION:
        FIRST_NUMBER += STEP
        progression.append(FIRST_NUMBER)
        i += 1
    return progression


def get_game():
    question = get_progression()
    correct_answer = choice(question)
    index = question.index(correct_answer)
    question[index] = '..'
    question = ' '.join(str(FIRST_NUMBER) for FIRST_NUMBER in question)
    return question, correct_answer
