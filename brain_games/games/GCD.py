from random import randint


def gcd():
    a, b = randint(1, 100), randint(1, 100)
    print(f'Question: {a} {b}')
    while b != 0:
        a, b = b, a % b
    return a


GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'


if __name__ == "__main__":
    gcd()

