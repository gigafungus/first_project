import prompt

from brain_games.cli import welcome_user
from brain_games.games.brain_calc import expression
from brain_games.games.brain_even import is_even


def main(func, user):  # аргументом для управляющей функции будет функция выбранной игры
    attempt = 0  # счетчик верных ответов
    max_attempts = 3  # необходимо верных ответов для победы

    while attempt < max_attempts:
        correct_answer = str(func())
        answer = prompt.string('Your answer: ')  
        
        if answer == correct_answer:
            attempt += 1
            print('Correct!')
            if attempt == max_attempts:
                print(f'Congratulations, {user}!')
                break
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user}!")
            break


def start():
    user = welcome_user()
    game = prompt.string('Choose the game: ').lower()  # пользователь выбирает игру
    match game:
        case 'even' | 'brain-even':
            print('Answer "yes" if the number is even, otherwise answer "no".')
            main(is_even, user)
        case 'calc' | 'brain-calc':
            print('What is the result of the expression?')
            main(expression, user)
        case _:
            print('Undefined')


if __name__ == '__main__':
    start()

