from brain_games.engine import start
from brain_games.games.game_prime import GAME_TASK, prime


def main():
    start(GAME_TASK, prime)


if __name__ == '__main__':
    main()
