from random import randint

from brain_games.cli import welcome_user

import prompt

def is_even(rnd_num):
    return 'yes' if rnd_num % 2 == 0 else 'no'

def main():
    print("Welcome to the Brain Games!")
    welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    attempt = 0  # счетчик верных ответов
    max_attempts = 3  # необходимо верных ответов для победы

    while attempt < max_attempts:
        rnd_num = randint(1, 50)  # произвольный интервал из множества чисел
        print(f'Question: {rnd_num}')
        answer = prompt.string('Your answer: ')  
        
        if answer == is_even(rnd_num):
            attempt += 1
            print('Correct!')
            if attempt == max_attempts:
                return f'Congratulations, {welcome_user()}!'
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{is_even(rnd_num)}'.")
            return f"Let's try again, {welcome_user()}!"
            


