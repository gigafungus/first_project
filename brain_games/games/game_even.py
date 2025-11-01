from random import randint


def is_even():
    rnd_num = randint(1, 50)  # произвольный интервал из множества чисел
    print(f'Question: {rnd_num}')
    return 'yes' if rnd_num % 2 == 0 else 'no'


GAME_TASK = 'Answer "yes" if the number is even, otherwise answer "no".'

if __name__ == "__main__":
    is_even()
