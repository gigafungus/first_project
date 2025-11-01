from random import choice, randint


def expression():
    num1, num2 = randint(0, 25), randint(0, 25)
    operator = choice('+-*')
    print(f'Question: {num1} {operator} {num2}')
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    else:
        return num1 * num2


GAME_TASK = 'What is the result of the expression?'


if __name__ == "__main__":
    expression()
