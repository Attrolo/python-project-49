from random import randint


MESSAGE_GAME = 'Find the greatest common divisor of given numbers.'


def get_gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return (num1 + num2)


def get_game():
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    result = get_gcd(num1, num2)
    question = f"{num1} {num2}"
    return question, result
