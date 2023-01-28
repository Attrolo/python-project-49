from random import randint


MESSAGE_GAME = 'Find the greatest common divisor of given numbers.'


MIN = 1
MAX = 10


def get_gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return (num1 + num2)


def get_game():
    num1 = randint(MIN, MAX)
    num2 = randint(MIN, MAX)
    result = get_gcd(num1, num2)
    question = f"{num1} {num2}"
    return question, result
