from random import randint
import random


MESSAGE_GAME = 'What number is missing in the progression?'


def get_progression():
    list = []
    first_number = randint(0, 50)
    lenght_progression = randint(5, 16)
    step = randint(1, 6)
    list.append(list)
    for i in range(get_progression):
        list.append(i)
        to_hide = random.randint(0, 6)
        correct_answer = str(list[to_hide])
        list[to_hide] = '..'
        number = ''.join(list)
        first_number += step
        list.append(list)
    return ''.join(get_progression)
