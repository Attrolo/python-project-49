from random import randint


MESSAGE_GAME = 'What number is missing in the progression?'


def get_progression():
    step = randint(1, 6)
    lenght_progression = randint(5, 21)
    number = randint(0, 50)  # Почему не используется?
    for i in range(1, lenght_progression):
        progression = []  # Создаем пустой список
        progression.append(progression + step)  # Добавляю к списку элементы
        to_hide = randint(0, 6)  # Прячем элемент из списка
        correct_answer = to_hide
        progression_2 = ''.join(str, progression)
        question = progression_2.replace(str(correct_answer)), '...'
        return correct_answer, question
