from random import choice, randint

import prompt


def expression():
    num1, num2 = randint(0, 25), randint(0, 25)
    operator = choice('+-*')
    print('What is the result of the expression?')
    print(f'Question: {num1} {operator} {num2}')
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    else:
        return num1 * num2


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    attempt = 0
    max_attempts = 3

    while attempt < max_attempts:
        correct_answer = str(expression())
        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            attempt += 1
            print('Correct!')
            if attempt == max_attempts:
                return f'Congratulations, {name}!'
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            return f"Let's try again, {name}!"



