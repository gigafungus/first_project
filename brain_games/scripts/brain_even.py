from random import randint

import prompt


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_cntr = 0  # счетчик верных ответов
    correct_to_win = 3  # необходимо верных ответов для победы

    while correct_cntr < correct_to_win:
        rnd_num = randint(1, 50)  # произвольный интервал из множества чисел
        print(f'Question: {rnd_num}')
        answer = prompt.string('Your answer: ')  

        def is_even(rnd_num):
            return 'yes' if rnd_num % 2 == 0 else 'no'
        
        if answer == is_even(rnd_num):
            correct_cntr += 1
            print('Correct!')
            if correct_cntr == correct_to_win:
                print(f'Congratulations, {name}!')
                return
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{is_even(rnd_num)}'.")
            print(f"Let's try again, {name}!")
            return


