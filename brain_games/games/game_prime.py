from math import sqrt
from random import randint


def prime():
    num = randint(2, 1000)
    finish = int(sqrt(num))
    print(f"Question: {num}")
    for i in range(2, finish + 1):
        if num % i == 0:
            return "no"
    return "yes"


GAME_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
