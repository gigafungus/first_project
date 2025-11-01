import prompt

from brain_games.cli import welcome_user


def start(game_description, game_function):
    user = welcome_user()
    print(game_description)
    attempt = 0
    max_attempts = 3

    while attempt < max_attempts:
        correct_answer = str(game_function())
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


if __name__ == "__main__":
    start()
