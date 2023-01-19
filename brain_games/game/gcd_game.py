from random import randint


MESSAGE_GAME = 'Find the greatest common divisor of given numbers.'


def get_nod(num1, num2):
    num = 0
    for i in range(1, min(num1, num2) + 1):
        if num2 % i == 0 and num1 % i == 0:
            num = max(num, i)
    return num


def get_game():
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    result = get_nod(num1, num2)
    question = f"question: {num1} {num2}"
    return question, result
