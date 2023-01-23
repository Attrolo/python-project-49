from random import randint


MESSAGE_GAME = 'Find the greatest common divisor of given numbers.'


def get_gcd(NUM1, NUM2):
    while NUM1 != 0 and NUM2 != 0:
        if NUM1 > NUM2:
            NUM1 = NUM1 % NUM2
        else:
            NUM2 = NUM2 % NUM1
    return (NUM1 + NUM2)


def get_game():
    NUM1 = randint(1, 10)
    NUM2 = randint(1, 10)
    result = get_gcd(NUM1, NUM2)
    question = f"{NUM1} {NUM2}"
    return question, result
